from src.llm.extractor import ClauseExtractor

extractor = ClauseExtractor()

context = """
This agreement is between Company A and Company B.
Company A supplies software.
Company B pays monthly fees.
Either party may terminate with 90 days notice.
Confidential information must be protected.
"""

summary = extractor.summarize(context)

print(summary)