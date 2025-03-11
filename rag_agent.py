from support_agent.document_processing import DocumentProcessor
from support_agent.vector_store import VectorStore
from support_agent.keyword_retriever import KeywordRetriever
from support_agent.api_client import LilypadClient
from support_agent.config import DEFAULT_LILYPAD_API_TOKEN
from support_agent.logger import logger
from typing import Dict, Any

class LilypadRAGAgent:
    """Manages the RAG system"""

    def __init__(self, document_path, api_token=None, use_embeddings=True):
        self.document_processor = DocumentProcessor(document_path)
        self.use_embeddings = use_embeddings

        if use_embeddings:
            self.retriever = VectorStore()
        else:
            self.retriever = KeywordRetriever(document_path)

        # Use provided API token or default from environment
        self.lilypad_client = LilypadClient(api_token or DEFAULT_LILYPAD_API_TOKEN)

    def initialize(self):
        try:
            logger.info("Processing document...")
            docs = self.document_processor.process()
            
            if not docs:
                logger.error("No document chunks were created.")
                return False

            logger.info("Initializing vector store...")
            if self.use_embeddings:
                success = self.retriever.initialize(docs)
            else:
                success = self.retriever.initialize()

            if not success:
                logger.error("Failed to initialize the retriever.")
            else:
                logger.info("Agent initialized successfully.")
                
            return success

        except Exception as e:
            logger.exception(f"Initialization error: {e}")
            return False

    def retrieve_context(self, query: str) -> str:
        """Retrieve relevant context for the query"""
        try:
            logger.info(f"🔍 Retrieving context for query: '{query}'")
            
            if self.use_embeddings:
                context = self.retriever.hybrid_search(query)
            else:
                context = self.retriever.retrieve(query)

            if not context or len(context) < 100:
                logger.warning("⚠️ Retrieval returned insufficient content, using full document")
                context = self.document_processor.get_full_document()

            logger.info(f"📄 Retrieved Context:\n{context[:1000]}")
            return context

        except Exception as e:
            logger.exception(f"❌ Error retrieving context: {str(e)}")
            return self.document_processor.get_full_document()



    def process_query(self, query: str) -> Dict[str, Any]:
        """Process user query step-by-step to isolate where it hangs"""
        logger.info(f"🔍 Processing query: {query}")

        context = self.retrieve_context(query)

        if not context:
            logger.error("❌ Retrieval failed. No context was returned.")
            return {"answer": "❌ Retrieval failed. No context available.", "context": ""}
        try:
            answer = self.lilypad_client.query(query, context)
        except Exception as e:
            logger.error(f"❌ API call failed: {e}")
            return {"answer": f"❌ API call failed: {e}", "context": context}

        if not answer:
            logger.error("❌ Lilypad API returned an empty response.")
            return {"answer": "❌ Lilypad API returned an empty response.", "context": context}

        return {"answer": answer, "context": context}
