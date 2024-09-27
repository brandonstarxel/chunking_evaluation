from enum import Enum
import re
from typing import List, Optional
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import os
from chromadb.utils import embedding_functions
import tiktoken
import time

def find_query_despite_whitespace(document, query):

    # Normalize spaces and newlines in the query
    normalized_query = re.sub(r'\s+', ' ', query).strip()
    
    # Create a regex pattern from the normalized query to match any whitespace characters between words
    pattern = r'\s*'.join(re.escape(word) for word in normalized_query.split())
    
    # Compile the regex to ignore case and search for it in the document
    regex = re.compile(pattern, re.IGNORECASE)
    match = regex.search(document)
    
    if match:
        return document[match.start(): match.end()], match.start(), match.end()
    else:
        return None

def rigorous_document_search(document: str, target: str):
    """
    This function performs a rigorous search of a target string within a document. 
    It handles issues related to whitespace, changes in grammar, and other minor text alterations.
    The function first checks for an exact match of the target in the document. 
    If no exact match is found, it performs a raw search that accounts for variations in whitespace.
    If the raw search also fails, it splits the document into sentences and uses fuzzy matching 
    to find the sentence that best matches the target.
    
    Args:
        document (str): The document in which to search for the target.
        target (str): The string to search for within the document.

    Returns:
        tuple: A tuple containing the best match found in the document, its start index, and its end index.
        If no match is found, returns None.
    """
    if target.endswith('.'):
        target = target[:-1]
    
    if target in document:
        start_index = document.find(target)
        end_index = start_index + len(target)
        return target, start_index, end_index
    else:
        raw_search = find_query_despite_whitespace(document, target)
        if raw_search is not None:
            return raw_search

    # Split the text into sentences
    sentences = re.split(r'[.!?]\s*|\n', document)

    # Find the sentence that matches the query best
    best_match = process.extractOne(target, sentences, scorer=fuzz.token_sort_ratio)

    if best_match[1] < 98:
        return None
    
    reference = best_match[0]

    start_index = document.find(reference)
    end_index = start_index + len(reference)

    return reference, start_index, end_index

def get_openai_embedding_function():
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if openai_api_key is None:
        raise ValueError("You need to set an embedding function or set an OPENAI_API_KEY environment variable.")
    embedding_function = embedding_functions.OpenAIEmbeddingFunction(
        api_key=os.getenv('OPENAI_API_KEY'),
        model_name="text-embedding-3-large"
    )
    return embedding_function

# Count the number of tokens in each page_content
def openai_token_count(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(string, disallowed_special=()))
    return num_tokens

class Language(str, Enum):
    """Enum of the programming languages."""

    CPP = "cpp"
    GO = "go"
    JAVA = "java"
    KOTLIN = "kotlin"
    JS = "js"
    TS = "ts"
    PHP = "php"
    PROTO = "proto"
    PYTHON = "python"
    RST = "rst"
    RUBY = "ruby"
    RUST = "rust"
    SCALA = "scala"
    SWIFT = "swift"
    MARKDOWN = "markdown"
    LATEX = "latex"
    HTML = "html"
    SOL = "sol"
    CSHARP = "csharp"
    COBOL = "cobol"
    C = "c"
    LUA = "lua"
    PERL = "perl"

class RateLimiter:
    def __init__(
        self,
        max_tokens_per_minute: Optional[int] = None,
        max_requests_per_minute: Optional[int] = None,
        model_name: str = 'cl100k_base' # OpenAI Tokenizer
    ):
        """
        Initialize the rate limiter.

        Args:
            max_tokens_per_minute: Maximum tokens allowed per minute (optional).
            max_requests_per_minute: Maximum requests allowed per minute (optional).
            model_name: The name of the model used for token estimation.
        """
        self.max_tokens_per_minute = max_tokens_per_minute * .8 # Temporary fix for rate limiting issue here: https://community.openai.com/t/discrepancy-between-tiktoken-token-count-and-openai-embeddings-api-token-count-exceeding-tpm-limit-in-tier-2-account/959298
        self.max_requests_per_minute = max_requests_per_minute
        self.tokenizer = tiktoken.get_encoding(model_name)
        self._reset_counters()

    def _reset_counters(self):
        """Reset the rate limiter counters and timing."""
        self.tokens_used = 0
        self.requests_made = 0
        self.window_start = time.time()

    def wait_for_available_quota(self, num_tokens: int = 0, num_requests: int = 0):
        """
        Wait until there is enough quota to proceed.

        Args:
            num_tokens: Number of tokens required.
            num_requests: Number of requests required.
        """
        while True:
            elapsed = time.time() - self.window_start
            if elapsed >= 60:
                self._reset_counters()
                break

            tokens_remaining = (self.max_tokens_per_minute - self.tokens_used) if self.max_tokens_per_minute else float('inf')
            requests_remaining = (self.max_requests_per_minute - self.requests_made) if self.max_requests_per_minute else float('inf')

            if tokens_remaining >= num_tokens and requests_remaining >= num_requests:
                break  # Enough quota is available
            else:
                sleep_time = 60 - elapsed
                print(f"Rate limit reached. Sleeping for {sleep_time:.2f} seconds. Tokens used: {self.tokens_used}, Tokens remaining: {tokens_remaining}, Requests made: {self.requests_made}, Requests remaining: {requests_remaining}")
                time.sleep(sleep_time)
                self._reset_counters()

        self.tokens_used += num_tokens
        self.requests_made += num_requests

    def count_tokens(self, texts: List[str]) -> int:
        """Estimate the total number of tokens in the list of texts."""
        return sum(len(self.tokenizer.encode(text, disallowed_special=())) for text in texts)
