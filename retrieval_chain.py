from config import LLM_PROVIDER
from langchain_classic.chains import RetrievalQA

def build_chain(vector_store):

    if LLM_PROVIDER == "openai":
        from langchain_openai import ChatOpenAI, OpenAIEmbeddings

        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-large"
        )

        llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )

    elif LLM_PROVIDER == "gemini":
        from langchain_google_genai import (
            ChatGoogleGenerativeAI,
            GoogleGenerativeAIEmbeddings
        )

        embeddings = GoogleGenerativeAIEmbeddings(
            model="gemini-embedding-001"
        )

        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite",
            temperature=0
        )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vector_store.as_retriever(),
    )

    return qa_chain