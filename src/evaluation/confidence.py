class ConfidenceCalculator:
    """
    Calculates a simple confidence score based on
    the number of retrieved chunks.
    """

    def calculate(self, retrieved_chunks: int) -> float:

        if retrieved_chunks >= 5:
            return 0.95
        elif retrieved_chunks >= 3:
            return 0.85
        elif retrieved_chunks >= 1:
            return 0.70
        else:
            return 0.50