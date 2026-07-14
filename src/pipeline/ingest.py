from src.loaders.pdf_loader import load_contracts
from src.preprocessing.chunker import ContractChunker
from src.embeddings.embedder import EmbeddingGenerator
from src.embeddings.vector_store import VectorStore
from src.utils.logger import logger


def build_vector_database(contract_folder: str = "data/contracts"):
    """
    Load contracts, generate embeddings, and store them in ChromaDB.
    """

    logger.info("Starting ingestion pipeline...")

    contracts = load_contracts(contract_folder)

    chunker = ContractChunker()
    embedder = EmbeddingGenerator()
    vector_store = VectorStore()

    total_chunks = 0

    for contract in contracts:

        chunks = chunker.split_text(contract.text)

        embeddings = embedder.embed(chunks)

        ids = []
        documents = []
        metadatas = []

        for idx, chunk in enumerate(chunks):

            ids.append(f"{contract.contract_id}_{idx}")

            documents.append(chunk)

            metadatas.append(
                {
                    "contract_id": contract.contract_id,
                    "filename": contract.filename,
                    "chunk_id": idx,
                }
            )

        vector_store.add_embeddings(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )

        total_chunks += len(chunks)

    logger.info("===================================")
    logger.info(f"Contracts Indexed : {len(contracts)}")
    logger.info(f"Chunks Indexed    : {total_chunks}")
    logger.info("===================================")

    return vector_store