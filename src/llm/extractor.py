from src.llm.groq_client import GroqClient
from src.llm.prompts import EXTRACTION_PROMPT, SUMMARY_PROMPT
import json


class ClauseExtractor:
    """
    Extracts legal clauses and generates contract summaries.
    """

    def __init__(self):
        self.client = GroqClient()

    def extract(self, query: str, context: str):

        prompt = EXTRACTION_PROMPT.format(
            query=query,
            context=context
        )

        response = self.client.generate(prompt)
        response = response.replace("```json", "").replace("```", "").strip()

        try:
            response = json.loads(response)

            print("\n========== LLM RESPONSE ==========")
            print(response)
            print("==================================\n")

        except json.JSONDecodeError:
            response = {
                "raw_response": response
            }

        return response

    def summarize(self, context: str):

     prompt = SUMMARY_PROMPT.format(
        context=context
     )

     summary = self.client.generate(prompt)

     print("\n========== SUMMARY ==========")
     print(repr(summary))
     print("=============================\n")

     return summary.strip() if summary else "Summary generation failed."