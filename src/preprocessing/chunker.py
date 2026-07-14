from langchain_text_splitters import RecursiveCharacterTextSplitter

from src.utils.logger import logger


class ContractChunker:
    """
    Splits contract text into overlapping chunks for embedding.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split_text(self, text: str):
        """
        Split a contract into chunks.
        """

        chunks = self.splitter.split_text(text)

        logger.info(f"Created {len(chunks)} chunks.")

        return chunks
    
