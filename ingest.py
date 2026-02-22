from bs4.filter import SoupStrainer
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

def build_vector_store(embeddings):

    loader = WebBaseLoader(
        web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
        bs_kwargs={
            "parse_only": SoupStrainer(
                class_=("post-content", "post-title", "post-header")
            )
        },
    )

    docs = loader.load()
    print(f"[+] Loaded {len(docs)} docs")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    splits = text_splitter.split_documents(docs)
    print(f"[+] Split into {len(splits)} chunks")

    vector_store = Chroma.from_documents(
        splits,
        embedding=embeddings
    )
    

    print("[+] Vector store created")

    return vector_store