from typing import Dict, List, Optional, Tuple
from chunking_evaluation.utils import (
    RateLimiter,
    rigorous_document_search,
    get_openai_embedding_function,
)
import os
import pandas as pd
import json
import chromadb
import numpy as np
from importlib import resources
from .evaluation_utils import (
    sum_of_ranges,
    union_ranges,
    intersect_two_ranges,
    difference,
)
from tqdm.auto import tqdm


class BaseEvaluation:
    """
    Base class for evaluation of chunkers with respect to retrieval tasks.
    """

    def __init__(
        self,
        questions_csv_path: str,
        chroma_db_path: Optional[str] = None,
        corpora_id_paths: Optional[Dict[str, str]] = None,
    ):
        self.questions_csv_path = questions_csv_path
        self.corpora_id_paths = corpora_id_paths
        self.corpus_list = []
        self.is_general = False

        self._load_questions_df()

        if chroma_db_path is not None:
            self.chroma_client = chromadb.PersistentClient(path=chroma_db_path)
        else:
            self.chroma_client = chromadb.Client()

    def _load_questions_df(self):
        """
        Load the questions DataFrame from the CSV path.
        """
        if os.path.exists(self.questions_csv_path):
            self.questions_df = pd.read_csv(self.questions_csv_path)
            self.questions_df["references"] = self.questions_df["references"].apply(
                json.loads
            )
        else:
            self.questions_df = pd.DataFrame(
                columns=["question", "references", "corpus_id"]
            )

        self.corpus_list = self.questions_df["corpus_id"].unique().tolist()

    def _get_chunks_and_metadata(self, splitter) -> Tuple[List[str], List[Dict]]:
        """
        Get chunks and their metadata from the corpus using the provided splitter.

        Args:
            splitter: The text splitter/chunker.

        Returns:
            A tuple of (documents, metadatas).
        """
        documents = []
        metadatas = []

        for corpus_id in self.corpus_list:
            corpus_path = corpus_id
            if self.corpora_id_paths is not None:
                corpus_path = self.corpora_id_paths[corpus_id]

            with open(corpus_path, "r") as file:
                corpus = file.read()

            current_documents = splitter.split_text(corpus)
            current_metadatas = []
            for document in current_documents:
                try:
                    _, start_index, end_index = rigorous_document_search(
                        corpus, document
                    )
                except Exception as e:
                    print(f"Error in finding {document} in {corpus_id}: {e}")
                    raise Exception(f"Error in finding {document} in {corpus_id}")

                current_metadatas.append(
                    {
                        "start_index": start_index,
                        "end_index": end_index,
                        "corpus_id": corpus_id,
                    }
                )

            documents.extend(current_documents)
            metadatas.extend(current_metadatas)

        return documents, metadatas

    def _full_precision_score(
        self, chunk_metadatas: List[Dict]
    ) -> Tuple[List[float], List[int]]:
        """
        Compute the full precision (ω) score for each question.

        Args:
            chunk_metadatas: List of chunk metadata dictionaries.

        Returns:
            A tuple containing list of ω scores and list of highlighted chunk counts per question.
        """
        omega_scores = []
        highlighted_chunks_counts = []

        for index, row in self.questions_df.iterrows():
            references = row["references"]
            corpus_id = row["corpus_id"]

            numerator_sets = []
            denominator_chunks_sets = []
            unused_highlights = [(x["start_index"], x["end_index"]) for x in references]

            highlighted_chunk_count = 0

            for metadata in chunk_metadatas:
                chunk_start, chunk_end, chunk_corpus_id = (
                    metadata["start_index"],
                    metadata["end_index"],
                    metadata["corpus_id"],
                )

                if chunk_corpus_id != corpus_id:
                    continue

                contains_highlight = False

                for ref_obj in references:
                    ref_start, ref_end = (
                        int(ref_obj["start_index"]),
                        int(ref_obj["end_index"]),
                    )
                    intersection = intersect_two_ranges(
                        (chunk_start, chunk_end), (ref_start, ref_end)
                    )

                    if intersection is not None:
                        contains_highlight = True
                        unused_highlights = difference(unused_highlights, intersection)
                        numerator_sets = union_ranges([intersection] + numerator_sets)
                        denominator_chunks_sets = union_ranges(
                            [(chunk_start, chunk_end)] + denominator_chunks_sets
                        )

                if contains_highlight:
                    highlighted_chunk_count += 1

            highlighted_chunks_counts.append(highlighted_chunk_count)

            denominator_sets = union_ranges(denominator_chunks_sets + unused_highlights)

            if numerator_sets:
                omega_score = sum_of_ranges(numerator_sets) / sum_of_ranges(
                    denominator_sets
                )
            else:
                omega_score = 0

            omega_scores.append(omega_score)

        return omega_scores, highlighted_chunks_counts

    def _scores_from_dataset_and_retrievals(
        self, question_metadatas: List[Dict], highlighted_chunks_counts: List[int]
    ) -> Tuple[List[float], List[float], List[float]]:
        """
        Compute the IOU, recall, and precision scores based on retrievals.

        Args:
            question_metadatas: List of metadata dictionaries per question.
            highlighted_chunks_counts: List of highlighted chunk counts per question.

        Returns:
            A tuple containing lists of IOU scores, recall scores, and precision scores.
        """
        iou_scores = []
        recall_scores = []
        precision_scores = []

        for index, row in self.questions_df.iterrows():
            references = row["references"]
            corpus_id = row["corpus_id"]
            metadatas = question_metadatas[index]
            highlighted_chunk_count = highlighted_chunks_counts[index]

            numerator_sets = []
            denominator_chunks_sets = []
            unused_highlights = [(x["start_index"], x["end_index"]) for x in references]

            for metadata in metadatas[:highlighted_chunk_count]:
                chunk_start, chunk_end, chunk_corpus_id = (
                    metadata["start_index"],
                    metadata["end_index"],
                    metadata["corpus_id"],
                )

                if chunk_corpus_id != corpus_id:
                    continue

                for ref_obj in references:
                    ref_start, ref_end = (
                        int(ref_obj["start_index"]),
                        int(ref_obj["end_index"]),
                    )
                    intersection = intersect_two_ranges(
                        (chunk_start, chunk_end), (ref_start, ref_end)
                    )

                    if intersection is not None:
                        unused_highlights = difference(unused_highlights, intersection)
                        numerator_sets = union_ranges([intersection] + numerator_sets)
                        denominator_chunks_sets = union_ranges(
                            [(chunk_start, chunk_end)] + denominator_chunks_sets
                        )

            numerator_value = sum_of_ranges(numerator_sets) if numerator_sets else 0
            recall_denominator = sum_of_ranges(
                [(x["start_index"], x["end_index"]) for x in references]
            )
            precision_denominator = sum_of_ranges(
                [
                    (metadata["start_index"], metadata["end_index"])
                    for metadata in metadatas[:highlighted_chunk_count]
                ]
            )
            iou_denominator = precision_denominator + sum_of_ranges(unused_highlights)

            recall_score = (
                numerator_value / recall_denominator if recall_denominator else 0
            )
            recall_scores.append(recall_score)

            precision_score = (
                numerator_value / precision_denominator if precision_denominator else 0
            )
            precision_scores.append(precision_score)

            iou_score = numerator_value / iou_denominator if iou_denominator else 0
            iou_scores.append(iou_score)

        return iou_scores, recall_scores, precision_scores

    def _add_documents_to_collection(
    self,
    collection,
    documents: List[str],
    metadatas: List[Dict],
    ids: List[str],
    use_tqdm: bool = False,
    rate_limiter: Optional[RateLimiter] = None,
):
        """
        Add documents to the collection, handling rate limiting if necessary.

        Args:
            collection: The ChromaDB collection to add documents to.
            documents: List of documents to add.
            metadatas: List of metadata dictionaries corresponding to the documents.
            ids: List of IDs corresponding to the documents.
            use_tqdm: Whether to use tqdm progress bar (default: False).
            rate_limiter: An instance of RateLimiter to manage rate limits (optional).
        """
        total_documents = len(documents)
        index = 0

        if use_tqdm:
            pbar = tqdm(total=total_documents, desc="Adding documents")

        while index < total_documents:
            # Determine the maximum number of documents we can process in this batch
            if rate_limiter:
                batch_tokens = 0
                batch_docs = []
                batch_metas = []
                batch_ids = []
                batch_requests = 1  # Assuming one request per batch

                tokens_remaining = (
                    rate_limiter.max_tokens_per_minute - rate_limiter.tokens_used
                    if rate_limiter.max_tokens_per_minute
                    else float("inf")
                )
                requests_remaining = (
                    rate_limiter.max_requests_per_minute - rate_limiter.requests_made
                    if rate_limiter.max_requests_per_minute
                    else float("inf")
                )

                # Check if there are enough requests remaining for the current batch
                if requests_remaining < batch_requests:
                    rate_limiter.wait_for_available_quota(num_requests=batch_requests)
                    continue

                # Build a batch while respecting the token limit
                while index < total_documents:
                    doc_tokens = rate_limiter.count_tokens([documents[index]])
                    potential_batch_tokens = batch_tokens + doc_tokens

                    # If adding the document stays within token limits, add it to the batch
                    if potential_batch_tokens <= tokens_remaining:
                        batch_tokens = potential_batch_tokens
                        batch_docs.append(documents[index])
                        batch_metas.append(metadatas[index])
                        batch_ids.append(ids[index])
                        index += 1
                    else:
                        # Reached token limit for this batch
                        break

                # If we couldn't add any documents to the batch due to token limit
                if not batch_docs:
                    # Handle a single document that might exceed token limits
                    single_doc_tokens = rate_limiter.count_tokens([documents[index]])
                    if single_doc_tokens > rate_limiter.max_tokens_per_minute:
                        print(f"Document at index {index} exceeds the token limit.")
                        index += 1  # Skip this document or handle differently
                    else:
                        # Wait for quota if the document itself doesn't exceed limit
                        rate_limiter.wait_for_available_quota(
                            num_tokens=single_doc_tokens, num_requests=batch_requests
                        )
                    continue

                # Wait for available quota before processing the batch
                rate_limiter.wait_for_available_quota(
                    num_tokens=batch_tokens, num_requests=batch_requests
                )
            else:
                # No rate limiting; process all remaining documents
                batch_docs = documents[index:]
                batch_metas = metadatas[index:]
                batch_ids = ids[index:]
                index = total_documents

            collection.add(documents=batch_docs, metadatas=batch_metas, ids=batch_ids)

            if use_tqdm:
                pbar.update(len(batch_docs))

        if use_tqdm:
            pbar.close()

    def _chunker_to_collection(
        self,
        chunker,
        embedding_function,
        chroma_db_path: Optional[str] = None,
        collection_name: Optional[str] = None,
        use_tqdm: bool = False,
        rate_limiter: Optional[RateLimiter] = None,
    ):
        """
        Convert the chunked documents into a ChromaDB collection.

        Args:
            chunker: The chunker to use.
            embedding_function: The embedding function to use.
            chroma_db_path: Optional path to save the ChromaDB.
            collection_name: Optional name for the collection.
            use_tqdm: Whether to use tqdm progress bar (default: False).
            rate_limiter: An instance of RateLimiter to manage rate limits (optional).

        Returns:
            The created ChromaDB collection.
        """
        collection = None

        if chroma_db_path and collection_name:
            try:
                chunk_client = chromadb.PersistentClient(path=chroma_db_path)
                collection = chunk_client.create_collection(
                    collection_name,
                    embedding_function=embedding_function,
                    metadata={"hnsw:search_ef": 50},
                )
                print("Created collection:", collection_name)
            except Exception as e:
                print("Failed to create collection:", e)

        if collection is None:
            collection_name = "auto_chunk"
            try:
                self.chroma_client.delete_collection(collection_name)
            except ValueError:
                pass
            collection = self.chroma_client.create_collection(
                collection_name,
                embedding_function=embedding_function,
                metadata={"hnsw:search_ef": 50},
            )

        documents, metadatas = self._get_chunks_and_metadata(chunker)
        ids = [str(i) for i in range(len(documents))]

        # Add documents to the collection
        self._add_documents_to_collection(
            collection,
            documents,
            metadatas,
            ids,
            use_tqdm=use_tqdm,
            rate_limiter=rate_limiter,
        )

        return collection

    def _get_chunk_collection(
        self, 
        chunker, 
        embedding_function, 
        db_to_save_chunks, 
        use_tqdm: bool, 
        rate_limiter: Optional[RateLimiter]
    ):
        """
        Get or create the chunk collection.
        """
        collection = None
        if db_to_save_chunks:
            collection_name = self._generate_collection_name(
                chunker, embedding_function
            )
            try:
                chunk_client = chromadb.PersistentClient(path=db_to_save_chunks)
                collection = chunk_client.get_collection(
                    collection_name, embedding_function=embedding_function
                )
            except Exception:
                collection = self._chunker_to_collection(
                    chunker,
                    embedding_function,
                    chroma_db_path=db_to_save_chunks,
                    collection_name=collection_name,
                    use_tqdm=use_tqdm,
                    rate_limiter=rate_limiter,
                )
        else:
            collection = self._chunker_to_collection(
                chunker, 
                embedding_function, 
                use_tqdm=use_tqdm,
                rate_limiter=rate_limiter
            )

        return collection

    def _generate_collection_name(self, chunker, embedding_function) -> str:
        """
        Generate a unique collection name based on chunker and embedding function.
        """
        chunk_size = getattr(chunker, "_chunk_size", "0")
        chunk_overlap = getattr(chunker, "_chunk_overlap", "0")
        embedding_function_name = embedding_function.__class__.__name__
        if embedding_function_name == "SentenceTransformerEmbeddingFunction":
            embedding_function_name = "SentEmbFunc"
        collection_name = f"{embedding_function_name}_{chunker.__class__.__name__}_{int(chunk_size)}_{int(chunk_overlap)}"
        return collection_name

    def _get_question_collection(self, embedding_function, use_tqdm: bool, rate_limiter: Optional[RateLimiter]):
        """
        Get or create the question collection.
        """
        question_collection = None

        if self.is_general:
            question_collection = self._load_precomputed_question_collection(
                embedding_function
            )

        if not self.is_general or question_collection is None:
            question_collection = self._create_question_collection(embedding_function, use_tqdm=use_tqdm, rate_limiter=rate_limiter)

        return question_collection

    def _load_precomputed_question_collection(self, embedding_function):
        """
        Load precomputed question embeddings if available.
        """
        with resources.as_file(
            resources.files("chunking_evaluation.evaluation_framework")
            / "general_evaluation_data"
        ) as general_benchmark_path:
            questions_client = chromadb.PersistentClient(
                path=os.path.join(general_benchmark_path, "questions_db")
            )
            try:
                if embedding_function.__class__.__name__ == "OpenAIEmbeddingFunction":
                    if embedding_function._model_name == "text-embedding-3-large":
                        return questions_client.get_collection(
                            "auto_questions_openai_large",
                            embedding_function=embedding_function,
                        )
                    elif embedding_function._model_name == "text-embedding-3-small":
                        return questions_client.get_collection(
                            "auto_questions_openai_small",
                            embedding_function=embedding_function,
                        )
                elif (
                    embedding_function.__class__.__name__
                    == "SentenceTransformerEmbeddingFunction"
                ):
                    return questions_client.get_collection(
                        "auto_questions_sentence_transformer",
                        embedding_function=embedding_function,
                    )
            except Exception as e:
                print(
                    "Warning: Failed to use frozen embeddings. Generating new embeddings. Error:",
                    e,
                )
                return None

    def _create_question_collection(
        self,
        embedding_function,
        use_tqdm=False,
        rate_limiter: Optional[RateLimiter] = None,
    ):
        """
        Create a new question collection with embeddings.

        Args:
            embedding_function: The embedding function to use.
            use_tqdm: Whether to use tqdm progress bar (default: False).
            rate_limiter: An instance of RateLimiter to manage rate limits (optional).

        Returns:
            The created ChromaDB collection.
        """
        try:
            self.chroma_client.delete_collection("auto_questions")
        except ValueError:
            pass
        question_collection = self.chroma_client.create_collection(
            "auto_questions",
            embedding_function=embedding_function,
            metadata={"hnsw:search_ef": 50},
        )

        documents = self.questions_df["question"].tolist()
        metadatas = [{"corpus_id": x} for x in self.questions_df["corpus_id"].tolist()]
        ids = [str(i) for i in self.questions_df.index]

        # Add documents to the collection
        self._add_documents_to_collection(
            question_collection,
            documents,
            metadatas,
            ids,
            use_tqdm=use_tqdm,
            rate_limiter=rate_limiter,
        )

        return question_collection

    def _compute_corpora_scores(
        self, omega_scores, iou_scores, recall_scores, precision_scores
    ):
        """
        Compute the corpora scores.
        """
        corpora_scores = {}
        for index, row in self.questions_df.iterrows():
            corpus_id = row["corpus_id"]
            if corpus_id not in corpora_scores:
                corpora_scores[corpus_id] = {
                    "omega_scores": [],
                    "iou_scores": [],
                    "recall_scores": [],
                    "precision_scores": [],
                }

            corpora_scores[corpus_id]["omega_scores"].append(omega_scores[index])
            corpora_scores[corpus_id]["iou_scores"].append(iou_scores[index])
            corpora_scores[corpus_id]["recall_scores"].append(recall_scores[index])
            corpora_scores[corpus_id]["precision_scores"].append(
                precision_scores[index]
            )

        return corpora_scores

    def run(
        self,
        chunker,
        embedding_function=None,
        retrieve: int = 5,
        db_to_save_chunks: Optional[str] = None,
        use_tqdm: bool = False,
        rate_limiter: Optional[RateLimiter] = None,
    ) -> Dict[str, Dict]:
        """
        Run the evaluation over the provided chunker.

        Args:
            chunker: The chunker to evaluate.
            embedding_function: The embedding function for nearest neighbour retrieval. Defaults to OpenAI's embedding function.
            retrieve: The number of chunks to retrieve per question. If set to -1, retrieves the minimum number of chunks containing excerpts.
            db_to_save_chunks: Optional path to save the chunked documents in ChromaDB.
            use_tqdm: Whether to use tqdm progress bar (default: False).
            rate_limiter: An instance of RateLimiter to manage rate limits (optional).

        Returns:
            A dictionary with 'scores' and 'stats' keys containing the evaluation results.
        """
        self._load_questions_df()
        if embedding_function is None:
            embedding_function = get_openai_embedding_function()

        # Get or create chunk collection
        collection = self._get_chunk_collection(
            chunker,
            embedding_function,
            db_to_save_chunks,
            use_tqdm,
            rate_limiter=rate_limiter,
        )

        # Get or create question collection
        question_collection = self._get_question_collection(
            embedding_function, 
            use_tqdm=use_tqdm, 
            rate_limiter=rate_limiter
        )

        # Retrieve question embeddings
        question_db = question_collection.get(include=["embeddings"])
        question_db["ids"] = [int(id) for id in question_db["ids"]]
        _, sorted_embeddings = zip(
            *sorted(zip(question_db["ids"], question_db["embeddings"]))
        )

        self.questions_df = self.questions_df.sort_index()

        # Compute omega scores
        omega_scores, highlighted_chunks_counts = self._full_precision_score(
            collection.get()["metadatas"]
        )

        # Determine maximum_n
        if retrieve == -1:
            maximum_n = min(20, max(highlighted_chunks_counts))
        else:
            highlighted_chunks_counts = [retrieve] * len(highlighted_chunks_counts)
            maximum_n = retrieve

        # Query the collection
        retrievals = collection.query(
            query_embeddings=list(sorted_embeddings), n_results=maximum_n
        )

        # Compute scores
        iou_scores, recall_scores, precision_scores = (
            self._scores_from_dataset_and_retrievals(
                retrievals["metadatas"], highlighted_chunks_counts
            )
        )

        # Build corpora scores
        corpora_scores = self._compute_corpora_scores(
            omega_scores, iou_scores, recall_scores, precision_scores
        )

        # Compute stats
        stats = {
            "iou_mean": np.mean(iou_scores),
            "iou_std": np.std(iou_scores),
            "recall_mean": np.mean(recall_scores),
            "recall_std": np.std(recall_scores),
            "precision_mean": np.mean(precision_scores),
            "precision_std": np.std(precision_scores),
            "omega_mean": np.mean(omega_scores),
            "omega_std": np.std(omega_scores),
        }

        scores = {
            "corpora_scores": corpora_scores,
            "iou_scores": iou_scores,
            "recall_scores": recall_scores,
            "precision_scores": precision_scores,
            "omega_scores": omega_scores,
            "highlighted_chunks_counts": highlighted_chunks_counts,
        }

        return {"scores": scores, "stats": stats}