# Chroma Research

A package for text chunking and benchmarking.

## Installation

You can install the package directly from GitHub:

```bash
pip install git+https://github.com/brandonstarxel/chroma_research.git
```


# usage.py
Below is an example of how you can immediately benchmark any chunking method.
```python
from chroma_research import BaseChunker, GeneralBenchmark

# Define a custom chunking class
class CustomChunker(BaseChunker):
    def split_text(self, text):
        # Custom chunking logic
        return [text[i:i+1200] for i in range(0, len(text), 1200)]

# Instantiate the custom chunker and benchmark
chunker = CustomChunker()
benchmark = GeneralBenchmark()

# Run the benchmark
results = benchmark.run(chunker, OPENAI_API_KEY="your-api-key")

print(results)
# {'iou_mean': 0.17715979570301696, 'iou_std': 0.10619791407460026, 'recall_mean': 0.8322119478569013, 'recall_std': 0.358260140288674}
```

Requirements:
- chroma
- fuzzywuzzy
- pandas
- numpy
