from sentence_transformers import SentenceTransformer

from src.utils.logger import logger


class EmbeddingGenerator:
    """
    Generates embeddings using Sentence Transformers.
    """

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):

        logger.info(f"Loading embedding model: {model_name}")

        self.model = SentenceTransformer(model_name)

        logger.info("Embedding model loaded successfully.")

    def embed(self, texts: list[str]):

        embeddings = self.model.encode(
            texts,
            convert_to_numpy=True,
            show_progress_bar=True
        )

        logger.info(f"Generated embeddings for {len(texts)} chunks.")

        return embeddings