from src.preprocessing.cleaner import clean_text
from pathlib import Path
from typing import List

import fitz

from src.models.contract import Contract
from src.utils.logger import logger


def extract_text(pdf_path: str) -> str:
    """
    Extract all text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF.

    Returns:
        str: Extracted text.
    """
    try:
        logger.info(f"Reading PDF: {pdf_path}")

        document = fitz.open(pdf_path)

        text = ""

        for page in document:
            text += page.get_text()

        document.close()

        logger.info(f"Successfully extracted text from {pdf_path}")

        return text

    except Exception as e:
        logger.error(f"Failed to read {pdf_path}: {e}")
        return ""


def load_contracts(folder_path: str) -> List[Contract]:
    """
    Load all PDF contracts recursively from the dataset.

    Args:
        folder_path (str): Root contracts folder.

    Returns:
        List[Contract]: List of Contract objects.
    """

    contracts = []

    root = Path(folder_path)

    pdf_files = list(root.rglob("*.pdf"))

    logger.info(f"Found {len(pdf_files)} PDF files.")

    for pdf_file in pdf_files:

        text = extract_text(str(pdf_file))
        text = clean_text(text)

        if not text:
          continue

        contract = Contract(
            contract_id=pdf_file.stem,
            filename=pdf_file.name,
            text=text,
        )

        contracts.append(contract)

    logger.info(f"Loaded {len(contracts)} contracts successfully.")

    return contracts
