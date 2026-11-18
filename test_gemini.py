
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load API key from .env
load_dotenv()

# Create Gemini model
llm = ChatGoogleGenerativeAI(
    model=os.getenv("SCAMSHIELD_MODEL", "gemini-3.1-flash-lite"),
    temperature=0,
    max_retries=2
)

# Send a test request
response = llm.invoke(
    "Explain phishing in one simple sentence."
)
print(response.text)
