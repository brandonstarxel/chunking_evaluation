from typing import List, Dict, Tuple, Optional
import os
import json
import random

from chunking_evaluation.utils import rigorous_document_search
from .base_evaluation import BaseEvaluation

import pandas as pd
import numpy as np
from importlib import resources

from openai import OpenAI  

class SyntheticEvaluation(BaseEvaluation):
    """
    Class for generating synthetic evaluation data by creating synthetic questions
    and references using OpenAI's GPT models.
    """

    def __init__(
        self,
        corpora_paths: List[str],
        queries_csv_path: str,
        chroma_db_path: Optional[str] = None,
        openai_api_key: Optional[str] = None,
    ):
        """
        Initialize the SyntheticEvaluation class.

        Args:
            corpora_paths: List of paths to the corpora files.
            queries_csv_path: Path to the CSV file where the generated queries will be saved.
            chroma_db_path: Optional path to the ChromaDB database.
            openai_api_key: OpenAI API key for accessing GPT models.
        """
        super().__init__(
            questions_csv_path=queries_csv_path, chroma_db_path=chroma_db_path
        )
        self.corpora_paths = corpora_paths
        self.questions_csv_path = queries_csv_path

        self.client = OpenAI(api_key=openai_api_key)

        self.synth_questions_df = None

        # Load prompts
        with resources.as_file(
            resources.files("chunking_evaluation.evaluation_framework") / "prompts"
        ) as prompt_path:
            self.question_maker_system_prompt = self._read_prompt_file(
                os.path.join(prompt_path, "question_maker_system.txt")
            )
            self.question_maker_approx_system_prompt = self._read_prompt_file(
                os.path.join(prompt_path, "question_maker_approx_system.txt")
            )
            self.question_maker_user_prompt = self._read_prompt_file(
                os.path.join(prompt_path, "question_maker_user.txt")
            )
            self.question_maker_approx_user_prompt = self._read_prompt_file(
                os.path.join(prompt_path, "question_maker_approx_user.txt")
            )

    def _read_prompt_file(self, file_path: str) -> str:
        """
        Read the content of a prompt file.

        Args:
            file_path: Path to the prompt file.

        Returns:
            The content of the prompt file as a string.
        """
        with open(file_path, "r") as f:
            return f.read()

    def _save_questions_df(self):
        """
        Save the synthetic questions DataFrame to CSV.
        """
        self.synth_questions_df.to_csv(self.questions_csv_path, index=False)

    def _tag_text(self, text: str) -> Tuple[str, List[int]]:
        """
        Tag the text by splitting it into chunks and adding start and end tags.

        Args:
            text: The text to be tagged.

        Returns:
            A tuple containing the tagged text and a list of tag indices.
        """
        chunk_length = 100
        chunks = []
        tag_indexes = [0]
        start = 0
        while start < len(text):
            end = start + chunk_length
            chunk = text[start:end]
            if end < len(text):
                # Find the last space within the chunk to avoid splitting a word
                space_index = chunk.rfind(" ")
                if space_index != -1:
                    end = start + space_index + 1  # Include the space in the chunk
                    chunk = text[start:end]
            chunks.append(chunk)
            tag_indexes.append(end)
            start = end  # Move start to end to continue splitting

        tagged_text = ""
        for i, chunk in enumerate(chunks):
            tagged_text += f"<start_chunk_{i}>" + chunk + f"<end_chunk_{i}>"

        return tagged_text, tag_indexes

    def _extract_question_and_approx_references(
        self, corpus: str, document_length: int = 4000, prev_questions: Optional[List[str]] = None
    ) -> Tuple[str, List[Dict]]:
        """
        Extract a question and approximate references from the corpus.

        Args:
            corpus: The corpus text.
            document_length: Length of the document to consider.
            prev_questions: List of previous questions.

        Returns:
            A tuple containing the question and a list of references.
        """
        if len(corpus) > document_length:
            start_index = random.randint(0, len(corpus) - document_length)
            document = corpus[start_index : start_index + document_length]
        else:
            start_index = 0
            document = corpus

        if prev_questions:
            if len(prev_questions) > 20:
                questions_sample = random.sample(prev_questions, 20)
            else:
                questions_sample = prev_questions
            prev_questions_str = "\n".join(questions_sample)
        else:
            prev_questions_str = ""

        tagged_text, tag_indexes = self._tag_text(document)

        completion = self.client.chat.completions.create(
            model="gpt-4-turbo",
            max_tokens=600,
            messages=[
                {"role": "system", "content": self.question_maker_approx_system_prompt},
                {
                    "role": "user",
                    "content": self.question_maker_approx_user_prompt.replace(
                        "{document}", tagged_text
                    ).replace("{prev_questions_str}", prev_questions_str),
                },
            ],
        )

        content = completion.choices[0].message.content.strip()
        json_response = json.loads(content)

        try:
            text_references = json_response["references"]
            question = json_response["question"]
        except KeyError as e:
            raise ValueError(f"The response does not contain a '{e.args[0]}' field.")

        references = []
        for reference in text_references:
            if not all(k in reference for k in ["content", "start_chunk", "end_chunk"]):
                raise ValueError(
                    "Each reference must contain 'content', 'start_chunk', and 'end_chunk' keys."
                )

            start_chunk_index = reference["start_chunk"]
            end_chunk_index = reference["end_chunk"]

            start_ref_index = start_index + tag_indexes[start_chunk_index]
            end_ref_index = start_index + tag_indexes[end_chunk_index + 1]

            ref_text = corpus[start_ref_index:end_ref_index]
            references.append(
                {
                    "content": ref_text,
                    "start_index": start_ref_index,
                    "end_index": end_ref_index,
                }
            )

        return question, references

    def _extract_question_and_references(
        self, corpus: str, document_length: int = 4000, prev_questions: Optional[List[str]] = None
    ) -> Tuple[str, List[Dict]]:
        """
        Extract a question and references from the corpus.

        Args:
            corpus: The corpus text.
            document_length: Length of the document to consider.
            prev_questions: List of previous questions.

        Returns:
            A tuple containing the question and a list of references.
        """
        if len(corpus) > document_length:
            start_index = random.randint(0, len(corpus) - document_length)
            document = corpus[start_index : start_index + document_length]
        else:
            document = corpus

        if prev_questions:
            if len(prev_questions) > 20:
                questions_sample = random.sample(prev_questions, 20)
            else:
                questions_sample = prev_questions
            prev_questions_str = "\n".join(questions_sample)
        else:
            prev_questions_str = ""

        completion = self.client.chat.completions.create(
            model="gpt-4-turbo",
            max_tokens=600,
            messages=[
                {"role": "system", "content": self.question_maker_system_prompt},
                {
                    "role": "user",
                    "content": self.question_maker_user_prompt.replace(
                        "{document}", document
                    ).replace("{prev_questions_str}", prev_questions_str),
                },
            ],
        )

        content = completion.choices[0].message.content.strip()
        json_response = json.loads(content)

        try:
            text_references = json_response["references"]
            question = json_response["question"]
        except KeyError as e:
            raise ValueError(f"The response does not contain a '{e.args[0]}' field.")

        references = []
        for reference in text_references:
            if not isinstance(reference, str):
                raise ValueError(
                    f"Expected reference to be of type str, but got {type(reference).__name__}"
                )
            target = rigorous_document_search(corpus, reference)
            if target is not None:
                ref_text, start_idx, end_idx = target
                references.append(
                    {"content": ref_text, "start_index": start_idx, "end_index": end_idx}
                )
            else:
                raise ValueError(
                    f"No match found in the document for the given reference.\nReference: {reference}"
                )

        return question, references

    def _generate_corpus_questions(
        self, corpus_id: str, approx: bool = False, n: int = 5
    ):
        """
        Generate synthetic questions and references for a given corpus.

        Args:
            corpus_id: Identifier for the corpus.
            approx: Whether to use approximate references.
            n: Number of questions to generate.
        """
        with open(corpus_id, "r") as file:
            corpus = file.read()

        i = 0
        while i < n:
            while True:
                try:
                    print(f"Trying Query {i} for corpus {corpus_id}")
                    questions_list = self.synth_questions_df[
                        self.synth_questions_df["corpus_id"] == corpus_id
                    ]["question"].tolist()
                    if approx:
                        question, references = self._extract_question_and_approx_references(
                            corpus, 4000, questions_list
                        )
                    else:
                        question, references = self._extract_question_and_references(
                            corpus, 4000, questions_list
                        )
                    if len(references) > 5:
                        raise ValueError("The number of references exceeds 5.")

                    new_question = {
                        "question": question,
                        "references": json.dumps(references),
                        "corpus_id": corpus_id,
                    }

                    new_df = pd.DataFrame([new_question])
                    self.synth_questions_df = pd.concat(
                        [self.synth_questions_df, new_df], ignore_index=True
                    )
                    self._save_questions_df()

                    break
                except (ValueError, json.JSONDecodeError) as e:
                    print(f"Error occurred: {e}")
                    continue
            i += 1

    def _get_synth_questions_df(self) -> pd.DataFrame:
        """
        Load or initialize the synthetic questions DataFrame.

        Returns:
            The synthetic questions DataFrame.
        """
        if os.path.exists(self.questions_csv_path):
            synth_questions_df = pd.read_csv(self.questions_csv_path)
        else:
            synth_questions_df = pd.DataFrame(
                columns=["question", "references", "corpus_id"]
            )
        return synth_questions_df

    def generate_queries_and_excerpts(
        self,
        approximate_excerpts: bool = False,
        num_rounds: int = -1,
        queries_per_corpus: int = 5,
    ):
        """
        Generate synthetic queries and excerpts.

        Args:
            approximate_excerpts: Whether to use approximate excerpts.
            num_rounds: Number of rounds to run. If -1, runs indefinitely.
            queries_per_corpus: Number of queries to generate per corpus.
        """
        self.synth_questions_df = self._get_synth_questions_df()

        rounds = 0
        while num_rounds == -1 or rounds < num_rounds:
            for corpus_id in self.corpora_paths:
                self._generate_corpus_questions(
                    corpus_id, approx=approximate_excerpts, n=queries_per_corpus
                )
            rounds += 1

    def _get_sim(self, target: str, references: List[str]) -> List[float]:
        """
        Compute cosine similarity between the target and reference texts.

        Args:
            target: The target text.
            references: List of reference texts.

        Returns:
            A list of cosine similarity scores.
        """
        response = self.client.embeddings.create(
            input=[target] + references, model="text-embedding-3-large"
        )
        embeddings = [np.array(data["embedding"]) for data in response["data"]]

        target_embedding = embeddings[0]
        reference_embeddings = embeddings[1:]

        full_sim = []
        for ref_embedding in reference_embeddings:
            cosine_similarity = np.dot(target_embedding, ref_embedding) / (
                np.linalg.norm(target_embedding) * np.linalg.norm(ref_embedding)
            )
            full_sim.append(cosine_similarity)

        return full_sim

    def _corpus_filter_poor_highlights(
        self, corpus_id: str, synth_questions_df: pd.DataFrame, threshold: float
    ):
        """
        Filter out poor highlights from the synthetic questions DataFrame for a corpus.

        Args:
            corpus_id: Identifier for the corpus.
            synth_questions_df: The synthetic questions DataFrame.
            threshold: Threshold for filtering.
        """
        corpus_questions_df = synth_questions_df[
            synth_questions_df["corpus_id"] == corpus_id
        ].copy()

        def edit_row(row):
            question = row["question"]
            references = [ref["content"] for ref in json.loads(row["references"])]
            similarity_scores = self._get_sim(question, references)
            worst_ref_score = min(similarity_scores)
            row["worst_ref_score"] = worst_ref_score
            return row

        # Apply the function to each row
        corpus_questions_df = corpus_questions_df.apply(edit_row, axis=1)

        count_before = len(corpus_questions_df)

        corpus_questions_df = corpus_questions_df[
            corpus_questions_df["worst_ref_score"] >= threshold
        ]
        corpus_questions_df = corpus_questions_df.drop(columns=["worst_ref_score"])

        count_after = len(corpus_questions_df)

        print(
            f"Corpus: {corpus_id} - Removed {count_before - count_after} poor highlights."
        )

        full_questions_df = pd.read_csv(self.questions_csv_path)
        full_questions_df = full_questions_df[
            full_questions_df["corpus_id"] != corpus_id
        ]

        full_questions_df = pd.concat(
            [full_questions_df, corpus_questions_df], ignore_index=True
        )
        # Drop unnecessary columns if they exist
        for col in ["fixed", "worst_ref_score", "diff_score"]:
            if col in full_questions_df.columns:
                full_questions_df = full_questions_df.drop(columns=col)

        full_questions_df.to_csv(self.questions_csv_path, index=False)

    def filter_poor_excerpts(
        self, threshold: float = 0.36, corpora_subset: Optional[List[str]] = None
    ):
        """
        Filter out poor excerpts from the synthetic questions DataFrame.

        Args:
            threshold: Threshold for filtering.
            corpora_subset: Optional list of corpora to filter.
        """
        if os.path.exists(self.questions_csv_path):
            synth_questions_df = pd.read_csv(self.questions_csv_path)
            if len(synth_questions_df) > 0:
                corpus_list = synth_questions_df["corpus_id"].unique().tolist()
                if corpora_subset:
                    corpus_list = [c for c in corpus_list if c in corpora_subset]
                for corpus_id in corpus_list:
                    self._corpus_filter_poor_highlights(
                        corpus_id, synth_questions_df, threshold
                    )

    def _corpus_filter_duplicates(
        self, corpus_id: str, synth_questions_df: pd.DataFrame, threshold: float
    ):
        """
        Filter out duplicate questions from the synthetic questions DataFrame for a corpus.

        Args:
            corpus_id: Identifier for the corpus.
            synth_questions_df: The synthetic questions DataFrame.
            threshold: Threshold for filtering.
        """
        corpus_questions_df = synth_questions_df[
            synth_questions_df["corpus_id"] == corpus_id
        ].copy()

        count_before = len(corpus_questions_df)

        corpus_questions_df.drop_duplicates(subset="question", keep="first", inplace=True)

        questions = corpus_questions_df["question"].tolist()

        response = self.client.embeddings.create(
            input=questions, model="text-embedding-3-large"
        )
        embeddings = [np.array(data["embedding"]) for data in response["data"]]

        embeddings_matrix = np.array(embeddings)

        # Normalize embeddings to unit vectors
        norm_embeddings = embeddings_matrix / np.linalg.norm(embeddings_matrix, axis=1, keepdims=True)

        sim_matrix = np.dot(norm_embeddings, norm_embeddings.T)

        def filter_vectors(sim_matrix, threshold):
            n = sim_matrix.shape[0]  # Number of vectors
            remaining = np.ones(n, dtype=bool)  # Initialize all vectors as remaining

            for i in range(n):
                if remaining[i]:  # Only check for vectors that are still remaining
                    for j in range(i + 1, n):
                        if remaining[j] and sim_matrix[i, j] > threshold:
                            remaining[j] = False  # Remove vector j because it's too similar to vector i

            return remaining

        rows_to_keep = filter_vectors(sim_matrix, threshold)

        corpus_questions_df = corpus_questions_df.iloc[rows_to_keep]

        count_after = len(corpus_questions_df)

        print(f"Corpus: {corpus_id} - Removed {count_before - count_after} duplicates.")

        full_questions_df = pd.read_csv(self.questions_csv_path)
        full_questions_df = full_questions_df[
            full_questions_df["corpus_id"] != corpus_id
        ]

        full_questions_df = pd.concat(
            [full_questions_df, corpus_questions_df], ignore_index=True
        )
        # Drop unnecessary columns if they exist
        for col in ["fixed", "worst_ref_score", "diff_score"]:
            if col in full_questions_df.columns:
                full_questions_df = full_questions_df.drop(columns=col)

        full_questions_df.to_csv(self.questions_csv_path, index=False)

    def filter_duplicates(
        self, threshold: float = 0.78, corpora_subset: Optional[List[str]] = None
    ):
        """
        Filter out duplicate questions from the synthetic questions DataFrame.

        Args:
            threshold: Threshold for filtering.
            corpora_subset: Optional list of corpora to filter.
        """
        if os.path.exists(self.questions_csv_path):
            synth_questions_df = pd.read_csv(self.questions_csv_path)
            if len(synth_questions_df) > 0:
                corpus_list = synth_questions_df["corpus_id"].unique().tolist()
                if corpora_subset:
                    corpus_list = [c for c in corpus_list if c in corpora_subset]
                for corpus_id in corpus_list:
                    self._corpus_filter_duplicates(
                        corpus_id, synth_questions_df, threshold
                    )

    def question_ref_filter(self):
        """
        Placeholder for future implementation of question-reference filtering.
        """
        self.synth_questions_df = self._get_synth_questions_df()
