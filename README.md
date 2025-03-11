# Lilypad RAG Agent

Lilypad RAG Support Agent is a Retrieval-Augmented Generation (RAG) AI agent designed to process and answer queries efficiently.

## **How It Works**

The agent follows a Retrieval-Augmented Generation (RAG) approach to improve response accuracy and relevance. It operates through the following steps:

1. **Embedding Text with `all-MiniLM`**

   - The agent uses `all-MiniLM-L6-v2` to convert input queries and stored knowledge into dense vector embeddings.
   - These embeddings enable efficient similarity-based retrieval.

2. **Retrieving Relevant Context**

   - The agent searches a pre-indexed database to retrieve the most relevant pieces of information based on the query.

3. **Generating Responses with Llama3 via Lilypad API**
   - The retrieved context is sent to the **Lilypad API**, which processes the query using **Llama3 8b**.
   - The AI model generates a detailed response based on the retrieved information.

This combination of embedding-based retrieval and advanced language model generation ensures **precise, context-aware responses**.

## **Expanding to Your Own Support Agent**

The Lilypad RAG Support Agent can be customized to work for different projects or knowledge bases by updating the context it uses for retrieval.

### **Modifying the Context Source (`issues.md`)**

By default, the agent retrieves relevant information from `issues.md`, a markdown file containing documented issues and troubleshooting steps. To tailor the agent for your own use case:

1. Open `issues.md` in the repository.
2. Replace or expand the content with relevant support information for your specific project.
3. Ensure the new content is structured clearly, as better formatting improves retrieval accuracy.
4. Restart the agent to index the updated knowledge base.

## **Usage**

### **1. Clone the Repository**

To get started, clone this repository to your local machine:

```sh
git clone https://github.com/PBillingsby/lilypad-rag-agent.git
```

### **2. Set Up Your API Key**

This agent requires an API key to function. Go to https://anura.lilypad.tech and sign up to get an API key.

Export your API key as an environment variable:
`export LILYPAD_API_TOKEN="your-api-key-here"`

### **3. Install Dependencies**

Ensure you have Python 3 installed, then install the required dependencies:
`pip install -r ./lilypad-rag-agent/requirements.txt`

### **4. Run the Agent**

Run the agent from the root directory of the repository:
`python3 -m lilypad_rag_agent.cli`

## **Contributing**

If you find bugs or have suggestions, feel free to open an issue or submit a pull request.

## **License**

This project is licensed under the MIT License. See the LICENSE file for details.
