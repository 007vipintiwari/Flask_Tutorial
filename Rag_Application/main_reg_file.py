import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv
from pinecone import Pinecone
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_pinecone import PineconeVectorStore
class Setup:
    def __init__(self):
        load_dotenv()
        self.pdf_name = "Dsa.pdf"
    def loading_pdf(self):
        # Loading the pdf
        loader = PyPDFLoader(self.pdf_name)
        docs = loader.load()
        return docs
    def making_chunk(self, docs):
        # making the chunks of document
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200)
        chunk_data = text_splitter.split_text(" ".join(doc.page_content for doc in docs))
        return chunk_data
    def define_embedding(self):
        # embedding the model
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004",
            google_api_key=os.getenv("GOOGLE_API_KEY"))
        return embeddings
    def vector_database_connection(self):
        index_name = "ragapplication"
        pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        dense_index = pc.Index(index_name)
        return dense_index

    def store_in_database(self,dense_index,embeddings,docs):
        vector_store = PineconeVectorStore(index=dense_index, embedding=embeddings)
        vector_store.add_documents(documents=docs)

if __name__ == "__main__":
    obj = Setup()
    docs = obj.loading_pdf()
    chunk_data = obj.making_chunk(docs)
    embedding = obj.define_embedding()
    index = obj.vector_database_connection()
    obj.store_in_database(index,embedding,docs)
