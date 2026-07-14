from src.embeddings.embedder import EmbeddingGenerator
from src.embeddings.vector_store import VectorStore
from src.utils.logger import logger


class Retriever:
    """
    Retrieves the most relevant contract chunks using semantic search.
    """

    def __init__(self):

        self.embedder = EmbeddingGenerator()
        self.vector_store = VectorStore()

    def retrieve(self, query: str, top_k: int = 5):

        logger.info(f"Searching for: {query}")

        query_embedding = self.embedder.embed([query])[0]

        results = self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k,
        )

        logger.info(f"Retrieved {top_k} relevant chunks.")

        return results