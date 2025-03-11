import os

# Configuration settings
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DOCUMENT_PATH = os.path.join(BASE_DIR, "docs", "lilypadIssues.md")
VECTOR_STORE_DIR = "./chroma_db"
DEFAULT_EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
LILYPAD_API_URL = "https://anura-testnet.lilypad.tech/api/v1/chat/completions"
DEFAULT_MODEL = "llama3.1:8b"
DEFAULT_MAX_TOKENS = 1024
DEFAULT_TEMPERATURE = 0.0

# Get API token from environment or set None
DEFAULT_LILYPAD_API_TOKEN = os.getenv("LILYPAD_API_TOKEN")
