import os
from dotenv import load_dotenv

load_dotenv()


class Config:
   GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
   GROQ_API_KEY = os.getenv("GROQ_API_KEY")
   MODEL_NAME = os.getenv("MODEL_NAME") 

   EMBEDDING_MODEL = os.getenv(
        "EMBEDDING_MODEL",
        "all-MiniLM-L6-v2"
    )

   CHROMA_DB_PATH = os.getenv(
        "CHROMA_DB_PATH",
        "./chroma_db"
    )

   DATA_PATH = os.getenv(
        "DATA_PATH",
        "./data/contracts"
    )

   OUTPUT_PATH = os.getenv(
        "OUTPUT_PATH",
        "./data/outputs"
    )


# Create a global instance
settings = Config()