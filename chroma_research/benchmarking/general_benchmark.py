from typing import Callable
from chroma_research.utils import harsh_doc_search
import chromadb.utils.embedding_functions as embedding_functions
import os
import pandas as pd
import json
import chromadb
import numpy as np

def sum_of_ranges(ranges):
    return sum(end - start for start, end in ranges)

def union_ranges(ranges):
    # Sort ranges based on the starting index
    sorted_ranges = sorted(ranges, key=lambda x: x[0])
    
    # Initialize with the first range
    merged_ranges = [sorted_ranges[0]]
    
    for current_start, current_end in sorted_ranges[1:]:
        last_start, last_end = merged_ranges[-1]
        
        # Check if the current range overlaps or is contiguous with the last range in the merged list
        if current_start <= last_end:
            # Merge the two ranges
            merged_ranges[-1] = (last_start, max(last_end, current_end))
        else:
            # No overlap, add the current range as new
            merged_ranges.append((current_start, current_end))
    
    return merged_ranges

def intersect_two_ranges(range1, range2):
    # Unpack the ranges
    start1, end1 = range1
    start2, end2 = range2
    
    # Calculate the maximum of the starting indices and the minimum of the ending indices
    intersect_start = max(start1, start2)
    intersect_end = min(end1, end2)
    
    # Check if the intersection is valid (the start is less than or equal to the end)
    if intersect_start <= intersect_end:
        return (intersect_start, intersect_end)
    else:
        return None  # Return an None if there is no intersection
    
# Define the difference function
def difference(ranges, target):
    """
    Takes a set of ranges and a target range, and returns the difference.
    
    Args:
    - ranges (list of tuples): A list of tuples representing ranges. Each tuple is (a, b) where a <= b.
    - target (tuple): A tuple representing a target range (c, d) where c <= d.
    
    Returns:
    - List of tuples representing ranges after removing the segments that overlap with the target range.
    """
    result = []
    target_start, target_end = target

    for start, end in ranges:
        if end < target_start or start > target_end:
            # No overlap
            result.append((start, end))
        elif start < target_start and end > target_end:
            # Target is a subset of this range, split it into two ranges
            result.append((start, target_start))
            result.append((target_end, end))
        elif start < target_start:
            # Overlap at the start
            result.append((start, target_start))
        elif end > target_end:
            # Overlap at the end
            result.append((target_end, end))
        # Else, this range is fully contained by the target, and is thus removed

    return result

def find_target_in_document(document, target):
    start_index = document.find(target)
    if start_index == -1:
        return None
    end_index = start_index + len(target)
    return start_index, end_index

class GeneralBenchmark:
    # def __init__(self, name: str, description: str, benchmark: Callable):
    def __init__(self, chroma_db_path=None, corpus_list=None):
        self.general_benchmark_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'general_benchmark_data')
        questions_df_path = os.path.join(self.general_benchmark_path, 'questions_df.csv')
        self.questions_df = pd.read_csv(questions_df_path)
        self.questions_df['references'] = self.questions_df['references'].apply(json.loads)
        
        if corpus_list is None:
            self.corpus_list = self.questions_df['corpus_id'].unique().tolist()
        else:
            self.corpus_list = corpus_list
            self.questions_df = self.questions_df[self.questions_df['corpus_id'].isin(corpus_list)]

        if chroma_db_path is not None:
            self.chroma_client = chromadb.PersistentClient(path=chroma_db_path)
        else:
            self.chroma_client = chromadb.Client()
    

    def _get_chunks_and_metadata(self, splitter):
        # Warning: metadata will be incorrect if a chunk is repeated since we use .find() to find the start index. This isn't pratically an issue for chunks over 1000 characters.
        documents = []
        metadatas = []
        for corpus_id in self.corpus_list:
            with open(os.path.join(self.general_benchmark_path, 'corpora', f'{corpus_id}.md'), 'r') as file:
                corpus = file.read()

            current_documents = splitter.split_text(corpus)
            current_metadatas = []
            for document in current_documents:
                try:
                    _, start_index, end_index = harsh_doc_search(corpus, document)
                except:
                    print(f"Error in finding {document} in {corpus_id}")
                    raise Exception(f"Error in finding {document} in {corpus_id}")
                # start_index, end_index = find_target_in_document(corpus, document)
                current_metadatas.append({"start_index": start_index, "end_index": end_index, "corpus_id": corpus_id})
            documents.extend(current_documents)
            metadatas.extend(current_metadatas)
        return documents, metadatas

    def _full_precision_score(self, chunk_metadatas):
        ioc_scores = []
        recall_scores = []
        for index, row in self.questions_df.iterrows():
            # Unpack question and references
            # question, references = question_references
            question = row['question']
            references = row['references']
            corpus_id = row['corpus_id']

            ioc_score = 0
            numerator_sets = []
            denominator_chunks_sets = []
            unused_highlights = [(x['start_index'], x['end_index']) for x in references]

            for metadata in chunk_metadatas:
                # Unpack chunk start and end indices
                chunk_start, chunk_end, chunk_corpus_id = metadata['start_index'], metadata['end_index'], metadata['corpus_id']

                if chunk_corpus_id != corpus_id:
                    continue
                
                for ref_obj in references:
                    reference = ref_obj['content']
                    ref_start, ref_end = int(ref_obj['start_index']), int(ref_obj['end_index'])
                    # Calculate intersection between chunk and reference
                    intersection = intersect_two_ranges((chunk_start, chunk_end), (ref_start, ref_end))
                    
                    if intersection is not None:
                        # Remove intersection from unused highlights
                        unused_highlights = difference(unused_highlights, intersection)

                        # Add intersection to numerator sets
                        numerator_sets = union_ranges([intersection] + numerator_sets)
                        
                        # Add chunk to denominator sets
                        denominator_chunks_sets = union_ranges([(chunk_start, chunk_end)] + denominator_chunks_sets)
            
            # Combine unused highlights and chunks for final denominator
            denominator_sets = union_ranges(denominator_chunks_sets + unused_highlights)
            
            # Calculate ioc_score if there are numerator sets
            if numerator_sets:
                ioc_score = sum_of_ranges(numerator_sets) / sum_of_ranges(denominator_sets)
            
            ioc_scores.append(ioc_score)

            recall_score = 1 - (sum_of_ranges(unused_highlights) / sum_of_ranges([(x['start_index'], x['end_index']) for x in references]))
            recall_scores.append(recall_score)

        return ioc_scores, recall_scores

    def _scores_from_dataset_and_retrievals(self, question_metadatas):
        ioc_scores = []
        recall_scores = []
        for (index, row), metadatas in zip(self.questions_df.iterrows(), question_metadatas):
            # Unpack question and references
            # question, references = question_references
            question = row['question']
            references = row['references']
            corpus_id = row['corpus_id']

            ioc_score = 0
            numerator_sets = []
            denominator_chunks_sets = []
            unused_highlights = [(x['start_index'], x['end_index']) for x in references]

            for metadata in metadatas:
                # Unpack chunk start and end indices
                chunk_start, chunk_end, chunk_corpus_id = metadata['start_index'], metadata['end_index'], metadata['corpus_id']

                if chunk_corpus_id != corpus_id:
                    continue
                
                # for reference, ref_start, ref_end in references:
                for ref_obj in references:
                    reference = ref_obj['content']
                    ref_start, ref_end = int(ref_obj['start_index']), int(ref_obj['end_index'])
                    
                    # Calculate intersection between chunk and reference
                    intersection = intersect_two_ranges((chunk_start, chunk_end), (ref_start, ref_end))
                    
                    if intersection is not None:
                        # Remove intersection from unused highlights
                        unused_highlights = difference(unused_highlights, intersection)

                        # Add intersection to numerator sets
                        numerator_sets = union_ranges([intersection] + numerator_sets)
                        
                        # Add chunk to denominator sets
                        denominator_chunks_sets = union_ranges([(chunk_start, chunk_end)] + denominator_chunks_sets)
            
            # Combine unused highlights and chunks for final denominator
            denominator_sets = union_ranges(denominator_chunks_sets + unused_highlights)
            
            # Calculate ioc_score if there are numerator sets
            if numerator_sets:
                ioc_score = sum_of_ranges(numerator_sets) / sum_of_ranges(denominator_sets)
            
            ioc_scores.append(ioc_score)

            recall_score = 1 - (sum_of_ranges(unused_highlights) / sum_of_ranges([(x['start_index'], x['end_index']) for x in references]))
            recall_scores.append(recall_score)

        return ioc_scores, recall_scores

    def _chunker_to_collection(self, chunker, embedding_function):
        collection_name = "auto_chunk"
        
        try:
            self.chroma_client.delete_collection(collection_name)
        except ValueError as e:
            pass

        collection = self.chroma_client.create_collection(collection_name, embedding_function=embedding_function)

        docs, metas = self._get_chunks_and_metadata(chunker)

        BATCH_SIZE = 500
        for i in range(0, len(docs), BATCH_SIZE):
            batch_docs = docs[i:i+BATCH_SIZE]
            batch_metas = metas[i:i+BATCH_SIZE]
            batch_ids = [str(i) for i in range(i, i+len(batch_docs))]
            collection.add(
                documents=batch_docs,
                metadatas=batch_metas,
                ids=batch_ids
            )

        return collection

    def run(self, chunker, embedding_function):
        collection = self._chunker_to_collection(chunker, embedding_function)
        
        try:
            self.chroma_client.delete_collection("auto_questions")
        except ValueError as e:
            pass
        question_collection = self.chroma_client.create_collection("auto_questions", embedding_function=embedding_function)

        question_collection.add(
            documents=self.questions_df['question'].tolist(),
            metadatas=[{"corpus_id": x} for x in self.questions_df['corpus_id'].tolist()],
            ids=[str(i) for i in self.questions_df.index]
        )
        
        question_db = question_collection.get(include=['embeddings'])

        # Convert ids to integers for sorting
        question_db['ids'] = [int(id) for id in question_db['ids']]
        # Sort both ids and embeddings based on ids
        _, sorted_embeddings = zip(*sorted(zip(question_db['ids'], question_db['embeddings'])))

        # Sort questions_df in ascending order
        self.questions_df = self.questions_df.sort_index()

        # Retrieve the documents based on sorted embeddings
        retrievals = collection.query(query_embeddings=list(sorted_embeddings), n_results=5)
        # print("Retrieval Complete")

        ioc_scores, recall_scores = self._scores_from_dataset_and_retrievals(retrievals['metadatas'])
        brute_ioc_scores, brute_recall_scores = self._full_precision_score(collection.get()['metadatas'])

        # ioc_mean = np.mean(ioc_scores)
        # ioc_std = np.std(ioc_scores)
        # # ioc_text = f"{ioc_mean:.5f} ± {ioc_std:.5f}"
        # ioc_text = f"{ioc_mean:.3f} ± {ioc_std:.3f}"

        brute_ioc_mean = np.mean(brute_ioc_scores)
        brute_ioc_std = np.std(brute_ioc_scores)
        # brute_ioc_text = f"{brute_ioc_mean:.3f} ± {brute_ioc_std:.3f}"

        recall_mean = np.mean(recall_scores)
        recall_std = np.std(recall_scores)
        # recall_text = f"{recall_mean:.5f} ± {recall_std:.5f}"
        # recall_text = f"{recall_mean:.3f} ± {recall_std:.3f}"

        # brute_recall_mean = np.mean(brute_recall_scores)
        # brute_recall_std = np.std(brute_recall_scores)
        # brute_recall_text = f"{brute_recall_mean:.3f} ± {brute_recall_std:.3f}"

        # return ioc_text, recall_text, brute_ioc_text, brute_recall_text
        return {
            "iou_mean": brute_ioc_mean,
            "iou_std": brute_ioc_std,
            "recall_mean": recall_mean,
            "recall_std": recall_std,
        }