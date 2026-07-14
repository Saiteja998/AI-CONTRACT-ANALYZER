import re


def remove_non_printable(text: str) -> str:
    """
    Remove non-printable control characters.
    """
    return re.sub(r"[\x00-\x1F\x7F]", " ", text)


def normalize_whitespace(text: str) -> str:
    """
    Replace multiple spaces/newlines with a single space.
    """
    return re.sub(r"\s+", " ", text).strip()


def clean_text(text: str) -> str:
    """
    Complete preprocessing pipeline.
    """
    text = remove_non_printable(text)
    text = normalize_whitespace(text)

    return text



