import os
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model=os.getenv("SCAMSHIELD_MODEL", "gemini-2.5-flash"),
    temperature=0
)