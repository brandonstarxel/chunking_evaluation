# This script is adapted from the Greg Kamradt's notebook on chunking.
# Original code can be found at: https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/main/tutorials/LevelsOfTextSplitting/5_Levels_Of_Text_Splitting.ipynb

from typing import Optional
from .base_chunker import BaseChunker
from .recursive_token_chunker import RecursiveTokenChunker
from chunking_evaluation.utils import openai_token_count, get_openai_embedding_function
from chromadb.api.types import (
    Embeddable,
    EmbeddingFunction,
)

import numpy as np

class KamradtModifiedChunker(BaseChunker):
    """
    A chunker that splits text into chunks of approximately a specified average size based on semantic similarity.

    This was adapted from Greg Kamradt's notebook on chunking but with the modification of including an average chunk size parameter. The original code can be found at: https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/main/tutorials/LevelsOfTextSplitting/5_Levels_Of_Text_Splitting.ipynb

    This class extends the functionality of the `BaseChunker` by incorporating a method to combine sentences based on a buffer size, calculate cosine distances between combined sentences, and perform a binary search on similarity thresholds to achieve chunks of desired average size.

    Attributes:
        avg_chunk_size (int): The desired average chunk size in terms of token count. Default is 400.
        min_chunk_size (int): The minimum chunk size in terms of token count. Default is 50.
        embedding_function (EmbeddingFunction[Embeddable], optional): A function that converts text to embeddings. Default is the OpenAI embedding function.
        length_function (function): A function that calculates the number of tokens in a text. Default is `openai_token_count`.

    Methods:
        combine_sentences(sentences, buffer_size=1):
            Combines sentences with a specified buffer size to create context-rich sentence groups.

        calculate_cosine_distances(sentences):
            Calculates cosine distances between combined sentences using their embeddings.

        split_text(text):
            Splits the input text into chunks based on the calculated cosine distances and the specified average chunk size.

    Example:
        chunker = KamradtModifiedChunker(avg_chunk_size=300)
        text = "Your text to be chunked."
        chunks = chunker.split_text(text)
    """
    def __init__(
        self, 
        avg_chunk_size:int=400, 
        min_chunk_size:int=50, 
        embedding_function: Optional[EmbeddingFunction[Embeddable]] = None, 
        length_function=openai_token_count
        ):
        """
        Initializes the KamradtModifiedChunker with the specified parameters.

        Args:
            avg_chunk_size (int, optional): The desired average chunk size in tokens. Defaults to 400.
            min_chunk_size (int, optional): The minimum chunk size in tokens. Defaults to 50.
            embedding_function (EmbeddingFunction[Embeddable], optional): A function to obtain embeddings for text. Defaults to OpenAI's embedding function if not provided.
            length_function (function, optional): A function to calculate token length of a text. Defaults to `openai_token_count`.
        """
        
        
        self.splitter = RecursiveTokenChunker(
            chunk_size=min_chunk_size,
            chunk_overlap=0,
            length_function=length_function
            )
        
        self.avg_chunk_size = avg_chunk_size
        if embedding_function is None:
            embedding_function = get_openai_embedding_function()
        self.embedding_function = embedding_function
        self.length_function = length_function

    def combine_sentences(self, sentences, buffer_size=1):
        # Go through each sentence dict
        for i in range(len(sentences)):

            # Create a string that will hold the sentences which are joined
            combined_sentence = ''

            # Add sentences before the current one, based on the buffer size.
            for j in range(i - buffer_size, i):
                # Check if the index j is not negative (to avoid index out of range like on the first one)
                if j >= 0:
                    # Add the sentence at index j to the combined_sentence string
                    combined_sentence += sentences[j]['sentence'] + ' '

            # Add the current sentence
            combined_sentence += sentences[i]['sentence']

            # Add sentences after the current one, based on the buffer size
            for j in range(i + 1, i + 1 + buffer_size):
                # Check if the index j is within the range of the sentences list
                if j < len(sentences):
                    # Add the sentence at index j to the combined_sentence string
                    combined_sentence += ' ' + sentences[j]['sentence']

            # Then add the whole thing to your dict
            # Store the combined sentence in the current sentence dict
            sentences[i]['combined_sentence'] = combined_sentence

        return sentences

    def calculate_cosine_distances(self, sentences):
        BATCH_SIZE = 500
        distances = []
        embedding_matrix = None
        for i in range(0, len(sentences), BATCH_SIZE):
            batch_sentences = sentences[i:i+BATCH_SIZE]
            batch_sentences = [sentence['combined_sentence'] for sentence in batch_sentences]
            embeddings = self.embedding_function(batch_sentences)

            # Convert embeddings list of lists to numpy array
            batch_embedding_matrix = np.array(embeddings)

            # Append the batch embedding matrix to the main embedding matrix
            if embedding_matrix is None:
                embedding_matrix = batch_embedding_matrix
            else:
                embedding_matrix = np.concatenate((embedding_matrix, batch_embedding_matrix), axis=0)

        # Normalize each vector to be a unit vector
        norms = np.linalg.norm(embedding_matrix, axis=1, keepdims=True)
        embedding_matrix = embedding_matrix / norms

        similarity_matrix = np.dot(embedding_matrix, embedding_matrix.T)
        
        for i in range(len(sentences) - 1):
            # Calculate cosine similarity
            similarity = similarity_matrix[i, i + 1]
            
            # Convert to cosine distance
            distance = 1 - similarity

            # Append cosine distance to the list
            distances.append(distance)

            # Store distance in the dictionary
            sentences[i]['distance_to_next'] = distance

        # Optionally handle the last sentence
        # sentences[-1]['distance_to_next'] = None  # or a default value

        return distances, sentences

    def split_text(self, text):
        """
        Splits the input text into chunks of approximately the specified average size based on semantic similarity.

        Args:
            text (str): The input text to be split into chunks.

        Returns:
            list of str: The list of text chunks.
        """
                
        sentences_strips = self.splitter.split_text(text)

        sentences = [{'sentence': x, 'index' : i} for i, x in enumerate(sentences_strips)]

        sentences = self.combine_sentences(sentences, 3)

        combined_sentences = [x['combined_sentence'] for x in sentences]

        distances, sentences = self.calculate_cosine_distances(sentences)

        total_tokens = sum(self.length_function(sentence['sentence']) for sentence in sentences)
        avg_chunk_size = self.avg_chunk_size
        number_of_cuts = total_tokens // avg_chunk_size

        # Define threshold limits
        lower_limit = 0.0
        upper_limit = 1.0

        # Convert distances to numpy array
        distances_np = np.array(distances)

        # Binary search for threshold
        while upper_limit - lower_limit > 1e-6:
            threshold = (upper_limit + lower_limit) / 2.0
            num_points_above_threshold = np.sum(distances_np > threshold)
            
            if num_points_above_threshold > number_of_cuts:
                lower_limit = threshold
            else:
                upper_limit = threshold

        indices_above_thresh = [i for i, x in enumerate(distances) if x > threshold] 
        
        # Initialize the start index
        start_index = 0

        # Create a list to hold the grouped sentences
        chunks = []

        # Iterate through the breakpoints to slice the sentences
        for index in indices_above_thresh:
            # The end index is the current breakpoint
            end_index = index

            # Slice the sentence_dicts from the current start index to the end index
            group = sentences[start_index:end_index + 1]
            combined_text = ' '.join([d['sentence'] for d in group])
            chunks.append(combined_text)
            
            # Update the start index for the next group
            start_index = index + 1

        # The last group, if any sentences remain
        if start_index < len(sentences):
            combined_text = ' '.join([d['sentence'] for d in sentences[start_index:]])
            chunks.append(combined_text)

        return chunks