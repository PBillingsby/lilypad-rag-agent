import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from logger import logger
from typing import List


class DocumentProcessor:
    """Handles document loading and chunking"""

    def __init__(self, document_path: str):
        self.document_path = document_path
        if not os.path.exists(document_path):
            raise FileNotFoundError(f"Document not found at {document_path}")

    def process(self) -> List[Document]:
        """Process document and return chunks"""
        try:
            loader = TextLoader(self.document_path, encoding="utf-8")
            raw_documents = loader.load()
            raw_content = raw_documents[0].page_content

            all_docs = []

            # Ensure correct function names are used
            all_docs.extend(self._create_chunks(raw_content, chunk_size=300, overlap=150, chunk_type="small"))
            all_docs.extend(self._create_chunks(raw_content, chunk_size=800, overlap=200, chunk_type="medium"))
            all_docs.extend(self._create_line_chunks(raw_content))

            if not all_docs:
                logger.error("❌ No document chunks were created.")
                return []

            logger.info(f"📄 Total document chunks created: {len(all_docs)}")

            # Log first few chunks for debugging
            for i, doc in enumerate(all_docs[:3]):
                logger.info(f"🔹 Chunk {i+1}: {doc.page_content[:500]}...")

            return all_docs

        except Exception as e:
            logger.exception(f"❌ Error processing document: {str(e)}")
            return []

    def _create_chunks(self, content: str, chunk_size: int, overlap: int, chunk_type: str) -> List[Document]:
        """Create document chunks with the given size and overlap"""
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=overlap,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        chunks = splitter.split_text(content)
        return [
            Document(page_content=chunk, metadata={"source": self.document_path, "chunk_type": chunk_type})
            for chunk in chunks
        ]
    def get_full_document(self) -> str:
        """Get the full document content as a fallback"""
        try:
            with open(self.document_path, "r", encoding="utf-8") as file:
                return file.read()
        except Exception as e:
            logger.exception(f"❌ Error reading full document: {e}")
            return ""

    def _create_line_chunks(self, content: str) -> List[Document]:
        """Create line-based document chunks"""
        lines = content.split("\n")
        line_docs = []
        window_size = 10
        stride = 5

        for i in range(0, len(lines), stride):
            window = lines[i : i + window_size]
            if window:
                chunk_text = "\n".join(window).strip()
                if chunk_text:
                    doc = Document(
                        page_content=chunk_text,
                        metadata={
                            "source": self.document_path,
                            "chunk_type": "line",
                            "start_line": i + 1,
                            "end_line": min(i + len(window), len(lines)),
                        }
                    )
                    line_docs.append(doc)

        logger.info(f"📄 Created {len(line_docs)} line-based chunks")
        return line_docs
