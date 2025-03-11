import os
import requests
import json
from config import LILYPAD_API_URL, DEFAULT_MODEL, DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE
from logger import logger
from ui import ThinkingAnimation

class LilypadClient:
    """Handles interaction with Lilypad API"""

    def __init__(self, api_token=None):
        self.api_url = LILYPAD_API_URL
        self.api_token = api_token or os.getenv("LILYPAD_API_TOKEN")

    def query(self, query: str, context: str) -> str:
        """Query Lilypad API with the given query and context"""

        system_prompt = """You are an AI assistant that answers questions using only the provided context.

1. Read ALL provided context carefully before answering.
2. ONLY use information present in the context.
3. Provide a clear and direct answer using the most relevant details.
4. If the answer is NOT in the context, say 'NO MATCH FOUND'.
5. DO NOT mention 'chunks', 'CHUNK X', 'Issue X', 'Issue', or any metadata related to document retrieval.
6. If the context includes issue numbers, REWRITE the response to exclude them.
7. Instead of referencing "Issue X," rephrase the information naturally. 
   - Example: Instead of saying "Using multiple GPUs (Issue 2)," say "A common issue is configuring multiple GPUs correctly."
8. Summarize issues in a way that is natural and avoids referencing the original structure of the document."""

        # **Remove chunk identifiers from context**
        cleaned_context = self._clean_context(context)

        user_prompt = f"""Context:
    {cleaned_context}

    Question: {query}

    Answer strictly based on the context above:
    """

        payload = {
            "model": DEFAULT_MODEL,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "max_tokens": DEFAULT_MAX_TOKENS,
            "temperature": DEFAULT_TEMPERATURE
        }

        headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

        thinking = ThinkingAnimation()
        thinking.start()

        try:
            response = requests.post(self.api_url, headers=headers, json=payload, stream=True)

            if response.status_code == 401:
                logger.error("❌ Unauthorized (401) - Check API Token and Headers.")
                return "❌ Unauthorized. Please check your API token."

            return self._process_streaming_response(response)
        finally:
            thinking.stop()

    def _clean_context(self, context: str) -> str:
        """Remove chunk references from the retrieved context"""
        import re
        # Remove any references like [CHUNK X - TYPE: XYZ]
        return re.sub(r"\[CHUNK \d+.*?\]", "", context).strip()


    def _process_streaming_response(self, response: requests.Response) -> str:
        """Process streaming response from Lilypad API"""
        full_response = ""
        current_event = None
        
        for line in response.iter_lines():
            if not line:
                continue
                
            line_str = line.decode("utf-8").strip()
            # Track the current event type
            if line_str.startswith("event:"):
                current_event = line_str[6:].strip()
                continue
                
            # Process data lines
            if line_str.startswith("data:"):
                data_str = line_str[5:].strip()
                
                # Skip completion marker
                if data_str == "[DONE]":
                    continue
                    
                # Process based on the current event type
                if current_event == "delta":
                    try:
                        data = json.loads(data_str)
                        
                        # Extract content from the completion structure
                        if "choices" in data and len(data["choices"]) > 0:
                            message = data["choices"][0].get("message", {})
                            content = message.get("content", "")
                            
                            if content:
                                full_response += content
                    except json.JSONDecodeError:
                        # Log but continue on parse errors
                        logger.debug(f"Failed to parse JSON in delta event: {data_str[:100]}...")
                
                # Skip other data types (status updates, etc.)
        
        return full_response.strip()