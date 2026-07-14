from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

for model in client.models.list():
    print("=" * 60)
    print(model.name)

    if hasattr(model, "supported_actions"):
        print(model.supported_actions)