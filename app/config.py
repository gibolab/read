import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL")
DATABASE_URL = os.getenv("DATABASE_URL")