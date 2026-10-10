import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Read GOOGLE_API_KEY from the .env file (which Git ignores)
ENV_PATH = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(ENV_PATH)

# Print only True/False, never the key itself
print("API key loaded:", bool(os.getenv("GOOGLE_API_KEY")))

llm = ChatGoogleGenerativeAI(model="gemini-3.1-flash-lite", temperature=0)
response = llm.invoke("Reply with exactly: connection OK")
print("Model replied:", response.text)