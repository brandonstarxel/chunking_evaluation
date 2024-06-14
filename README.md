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
from chroma_research import BaseChunker, SimpleBenchmark

# Define a custom chunking class
class CustomChunker(BaseChunker):
    def split_text(self, text):
        # Custom chunking logic
        return text.split('\n')

# Instantiate the custom chunker and benchmark
chunker = CustomChunker()
benchmark = SimpleBenchmark(chunker)

# Run the benchmark
results = benchmark.run('path/to/question_df.csv', 'path/to/markdown_files')

# Print the results
print(f"IoU Mean: {results['iou_mean']}, IoU Std: {results['iou_std']}")
print(f"Recall Mean: {results['recall_mean']}, Recall Std: {results['recall_std']}")
```

Requirements:
- tiktoken
- fuzzywuzzy
- chroma
