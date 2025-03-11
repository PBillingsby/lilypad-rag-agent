import argparse
import os
import sys
from lilypad-rag-agent.rag_agent import LilypadRAGAgent
from lilypad-rag-agent.logger import setup_logging, logger  # ✅ Import both logger and setup_logging
from lilypad-rag-agent.ui import ThinkingAnimation
from lilypad-rag-agent.config import DEFAULT_DOCUMENT_PATH

# ✅ Call logging setup FIRST
setup_logging()

# ✅ Now logging will work
logger.info(f"Working Directory: {os.getcwd()}")
logger.info(f"Python Path: {sys.path}")
def parse_args():
    """Parse command line arguments with default values"""
    parser = argparse.ArgumentParser(description="Lilypad RAG Support Agent")
    parser.add_argument("--doc", type=str, default=DEFAULT_DOCUMENT_PATH, help="Path to document file")
    parser.add_argument("--token", type=str, default=os.getenv("LILYPAD_API_TOKEN"), help="Lilypad API token")
    parser.add_argument("--no-embeddings", action="store_true", help="Use keyword-based retrieval instead of embeddings")
    return parser.parse_args()

def main():
    """Main entry point"""
    args = parse_args()
    setup_logging()

    print("🐸 Lilypad RAG Support Agent 🐸\n" + "-" * 40)
    # Check if document exists
    if not os.path.exists(args.doc):
        print(f"❌ Error: Document not found at {args.doc}")
        return

    use_embeddings = not args.no_embeddings

    # Create and initialize the RAG agent
    rag_agent = LilypadRAGAgent(document_path=args.doc, api_token=args.token, use_embeddings=use_embeddings)

    if not rag_agent.initialize():
        print("❌ Failed to initialize agent. Exiting.")
        return

    print("✅ System ready\n" + "-" * 40 + "\nAsk a question or type 'quit' to exit.")

    while True:
        query = input("\n🐸 Question: ").strip()
        if query.lower() in ["quit", "exit"]:
            print("\nThank you for using Lilypad RAG Support Agent. Goodbye!")
            break

        result = rag_agent.process_query(query)
        answer = result.get("answer", "❌ No valid answer received.")
        print("\n🐸 Answer:", answer)

if __name__ == "__main__":
    main()
