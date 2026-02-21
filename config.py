import os
from dotenv import load_dotenv

load_dotenv()

LLM_PROVIDER = None

if os.getenv("OPENAI_API_KEY"):
    LLM_PROVIDER = "openai"
elif os.getenv("GOOGLE_API_KEY"):
    LLM_PROVIDER = "gemini"
else:
    raise RuntimeError("No API key found (OPENAI_API_KEY or GOOGLE_API_KEY required)")

print(f"[+] Using provider: {LLM_PROVIDER}")