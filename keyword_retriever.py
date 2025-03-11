import os
import re
import numpy as np
from lilypad-rag-agent.logger import logger
from langchain.docstore.document import Document
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from typing import List, Dict


class KeywordRetriever:
    """Improved keyword-based document retriever using TF-IDF similarity."""

    def __init__(self, document_path: str):
        """Initialize keyword retriever"""
        self.document_path = document_path
        self.chunks = []
        self.chunk_size = 2000  # Larger chunks to capture full sections
        self.chunk_overlap = 500  # Overlapping for contextual continuity
        self.top_k = 10  # Retrieve more relevant chunks

        if not os.path.exists(document_path):
            raise FileNotFoundError(f"Document not found at {document_path}")

    def initialize(self) -> bool:
        """Process document into chunks for retrieval"""
        try:
            with open(self.document_path, "r", encoding="utf-8") as file:
                content = file.read()

            self.chunks = self._create_overlapping_chunks(content, self.chunk_size, self.chunk_overlap)
            logger.info(f"✅ Created {len(self.chunks)} chunks for retrieval")
            return True
        except Exception as e:
            logger.exception(f"❌ Error initializing keyword retriever: {str(e)}")
            return False

    def _create_overlapping_chunks(self, content: str, chunk_size: int, overlap: int) -> List[Dict]:
        """Create larger, overlapping chunks to improve retrieval"""
        chunks = []
        stride = chunk_size - overlap
        content_len = len(content)

        for i in range(0, content_len, stride):
            chunk_text = content[i:i + chunk_size].strip()
            if chunk_text:
                chunks.append({
                    "text": chunk_text,
                    "metadata": {"start_char": i, "end_char": min(i + chunk_size, content_len)}
                })
        return chunks

    def retrieve(self, query: str) -> str:
        """Retrieve relevant chunks using TF-IDF similarity"""
        if not self.chunks:
            return self.get_full_document()

        # Prepare TF-IDF vectorizer with n-grams for better phrase matching
        vectorizer = TfidfVectorizer(ngram_range=(1,2), stop_words="english")
        doc_texts = [chunk["text"] for chunk in self.chunks]
        vectors = vectorizer.fit_transform(doc_texts + [query])

        # Compute cosine similarity between query and document chunks
        scores = cosine_similarity(vectors[-1], vectors[:-1])[0]
        top_indices = np.argsort(scores)[-self.top_k:][::-1]  # Get top_k most relevant chunks

        # Filter low-confidence results
        retrieved_chunks = [self.chunks[i] for i in top_indices if scores[i] > 0.1]

        # Debugging: Print retrieved chunks
        print(f"🔍 Retrieved Chunks:\n{retrieved_chunks}")

        # Merge consecutive chunks for a complete response
        merged_context = self._merge_chunks(retrieved_chunks)

        return merged_context if merged_context else self.get_full_document()

    def _merge_chunks(self, chunks: List[Dict]) -> str:
        """Merge consecutive chunks for better coherence."""
        merged_text = ""
        last_end = -1

        for chunk in sorted(chunks, key=lambda x: x["metadata"]["start_char"]):
            start = chunk["metadata"]["start_char"]
            text = chunk["text"]

            # Merge only if chunks are close together
            if last_end != -1 and start - last_end < 200:
                merged_text += " " + text
            else:
                merged_text += "\n\n" + text

            last_end = chunk["metadata"]["end_char"]

        return merged_text.strip()

    def get_full_document(self) -> str:
        """Get the full document content as a fallback"""
        try:
            with open(self.document_path, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            logger.exception(f"❌ Error reading full document: {e}")
            return ""
