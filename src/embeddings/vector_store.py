import chromadb
from chromadb.config import Settings

from src.utils.logger import logger


class VectorStore:
    """
    ChromaDB wrapper for storing and retrieving contract embeddings.
    """

    def __init__(
        self,
        collection_name: str = "contracts",
        persist_directory: str = "chroma_db",
    ):

        logger.info("Initializing ChromaDB...")

        self.client = chromadb.PersistentClient(path=persist_directory)

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

        logger.info("ChromaDB initialized successfully.")

    def add_embeddings(
        self,
        ids,
        embeddings,
        documents,
        metadatas,
    ):
        """
        Store embeddings inside ChromaDB.
        """

        self.collection.add(
            ids=ids,
            embeddings=embeddings.tolist(),
            documents=documents,
            metadatas=metadatas,
        )

        logger.info(f"Stored {len(ids)} chunks in ChromaDB.")

    def search(self, query_embedding, top_k=5):

      results = self.collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k,
      )

      return results