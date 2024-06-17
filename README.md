# Chroma Research

A package for text chunking and benchmarking.

## Installation

You can install the package directly from GitHub:

```bash
pip install git+https://github.com/brandonstarxel/chroma_research.git
```


# Benchmarking with Your Own Custom Chunker
This example shows how to implement your own chunking logic and benchmark its performance.
```python
from chroma_research import BaseChunker, GeneralBenchmark
from chromadb.utils import embedding_functions

# Define a custom chunking class
class CustomChunker(BaseChunker):
    def split_text(self, text):
        # Custom chunking logic
        return [text[i:i+1200] for i in range(0, len(text), 1200)]

# Instantiate the custom chunker and benchmark
chunker = CustomChunker()
benchmark = GeneralBenchmark()

# Choose embedding function
default_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="OPENAI_API_KEY",
    model_name="text-embedding-3-large"
)

# Run the benchmark
results = benchmark.run(chunker, default_ef)

print(results)
# {'iou_mean': 0.17715979570301696, 'iou_std': 0.10619791407460026, 
# 'recall_mean': 0.8091207841640163, 'recall_std': 0.3792297991952294}
```

Usage and Benchmarking of ClusterSemanticChunker
This example demonstrates how to use our ClusterSemanticChunker and how you can benchmark it yourself.
```python
from chroma_research import BaseChunker, GeneralBenchmark
from chroma_research.chunking import ClusterSemanticChunker
from chromadb.utils import embedding_functions

# Instantiate benchmark
benchmark = GeneralBenchmark()

# Choose embedding function
default_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="OPENAI_API_KEY",
    model_name="text-embedding-3-large"
)

# Instantiate chunker and run the benchmark
chunker = ClusterSemanticChunker(default_ef, max_chunk_size=400)
results = benchmark.run(chunker, default_ef)

print(results)
# {'iou_mean': 0.18255175232840098, 'iou_std': 0.12773219595465307, 
# 'recall_mean': 0.8973469551927365, 'recall_std': 0.29042203879923994}
```

Requirements:
- chroma
- fuzzywuzzy
- pandas
- numpy
