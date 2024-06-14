from base_chunker import BaseChunker
from typing import List

class ClusterSemanticChunker(BaseChunker):
    def split_text(self, text: str) -> List[str]:
        return text.split()  # Simple example that splits text by whitespace
