# Chroma Research

A package for text chunking and benchmarking.

## Installation

You can install the package directly from GitHub:

```bash
pip install git+https://github.com/brandonstarxel/chroma_research.git
```


# usage.py
Below is an example of how you could immediately benchmark any chunking method.
```python
from chroma_research import BaseChunker, GeneralBenchmark
from langchain_text_splitters import RecursiveCharacterTextSplitter
import tiktoken
import os

# Count the number of tokens in each page_content
def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(string, disallowed_special=()))
    return num_tokens

# Define a custom chunking class
class CustomChunker(BaseChunker):
    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=400,
            chunk_overlap=0,
            length_function=num_tokens_from_string
        )

    def split_text(self, text):
        # Custom chunking logic
        return self.text_splitter.split_text(text)

# Instantiate the custom chunker and benchmark
chunker = CustomChunker()
benchmark = GeneralBenchmark()

OPENAI_API_KEY = os.getenv("YOUR_OPENAI_API_KEY")

# Run the benchmark
results = benchmark.run(chunker, OPENAI_API_KEY=OPENAI_API_KEY)

print(results)
# {'ioc_mean': 0.1783035441859945, 'ioc_std': 0.1310294333718983, 'recall_mean': 0.8160979986557657, 'recall_std': 0.37950832386967387}
```

Requirements:
- tiktoken
- fuzzywuzzy
- chroma
- pandas
