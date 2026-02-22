from config import LLM_PROVIDER
from ingest import build_vector_store
from retrieval_chain import build_chain

# Select embeddings according to provider
if LLM_PROVIDER == "openai":
    from langchain_openai import OpenAIEmbeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

elif LLM_PROVIDER == "gemini":
    from langchain_google_genai import GoogleGenerativeAIEmbeddings
    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001"
    )

# Build vector store
vector_store = build_vector_store(embeddings)

# Build Retrieval Chain
qa_chain = build_chain(vector_store)

print("\nRAG system ready. Type 'exit' to quit.\n")

while True:
    query = input("Ask a question: ")

    if query.lower() == "exit":
        break

    response = qa_chain.run(query)
    print("\nAnswer:\n")
    print(response)