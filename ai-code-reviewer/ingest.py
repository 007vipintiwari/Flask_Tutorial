import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
from utils.loader import load_code_files
from utils.chunker import chunk_code

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004"
)

docs = load_code_files("./sample_repo")
chunks = chunk_code(docs)

texts = [c["text"] for c in chunks]
metadatas = [c["metadata"] for c in chunks]

vectorstore = PineconeVectorStore.from_texts(
    texts=texts,
    embedding=embeddings,
    metadatas=metadatas,
    index_name="ai-code-reviewer"
)

print("✅ Codebase indexed successfully")
