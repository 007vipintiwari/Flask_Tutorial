from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os
from pinecone import Pinecone
from langchain_pinecone import PineconeVectorStore
from google import genai
from google.genai import types
class Query:
    def __init__(self):
        load_dotenv()
        self.history = []

    def get_query(self):
        dense_index = self.vector_database_connection()
        self.define_embedding()
        while True:
            input_value = input("Hi there, ask my anything,type 'exit' or 'stop' to getout:\n")
            if input_value.lower() == "stop" or input_value.lower() == "exit":
                break
            else:
                self.history.append({"role":'user',
                "parts":[{'text':input_value}]
                })
                query_vector = self.convert_query_into_embedding(input_value)
                response = self.search_in_database(dense_index,query_vector)
                self.call_to_llm(response)
        print(self.history)



    def define_embedding(self):
        # embedding the model
        self.embeddings = GoogleGenerativeAIEmbeddings(
            model="models/text-embedding-004",
            google_api_key=os.getenv("GOOGLE_API_KEY"))

    def convert_query_into_embedding(self,query):
        query_vector = self.embeddings.embed_query(query)
        return query_vector

    def vector_database_connection(self):
        index_name = "ragapplication"
        pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        dense_index = pc.Index(index_name)
        return dense_index

    def search_in_database(self,dense_index,query_vector):
        results = dense_index.query(
            vector=query_vector,
            top_k=5,
            include_metadata=True
        )
        response = [x["metadata"]["text"] for x in results.matches]
        return " ".join(response)

    def call_to_llm(self,input_query):
        client = genai.Client()

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=self.history,
            config=types.GenerateContentConfig(
                system_instruction=f"You have to behave like a Data Structure and Algorithm Expert.\
                                    You will be given a context of relevant information and a user question. \
                                    Your task is to answer the user's question based ONLY on the provided context. \
                                    If the answer is not in the context, you must say 'I could not find the answer in the provided document.' \
                                    Keep your answers clear, concise, and educational. Context: ${input_query} "
        )
        )
        self.history.append({'role': 'model',
            'parts': [{'text':response.text}]})




if __name__ == "__main__":
    obj = Query()
    obj.get_query()


