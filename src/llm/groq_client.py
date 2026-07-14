from groq import Groq

from src.utils.config import settings
from src.utils.logger import logger


class GroqClient:

    def __init__(self):

        self.client = Groq(
            api_key=settings.GROQ_API_KEY
        )

        logger.info("Groq initialized successfully.")

    def generate(self, prompt: str):

        response = self.client.chat.completions.create(
            model=settings.MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,
        )

        return response.choices[0].message.content