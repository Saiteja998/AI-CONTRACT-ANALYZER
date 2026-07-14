EXTRACTION_PROMPT = """
You are an expert legal contract analyzer.

Analyze the contract context carefully.

IMPORTANT:
You MUST return ALL of the following fields.
Do NOT omit any field.
Do NOT return markdown.
Return ONLY valid JSON.

{{
  "clause_type": "",
  "clause_text": "",
  "summary": "",
  "important_points": []
}}

Rules:

1. Answer ONLY using the provided contract context.

2. The summary should briefly explain the extracted clause.

3. important_points MUST contain at least 4 concise bullet points.

Question:
{query}

Contract Context:
{context}
"""
SUMMARY_PROMPT = """
You are an expert legal contract analyst.

Using ONLY the contract context below, generate a concise summary between 100 and 150 words.

Include:
- Purpose of the agreement
- Key obligations of each party
- Major risks or penalties

Return ONLY the summary text.

Context:
{context}
"""