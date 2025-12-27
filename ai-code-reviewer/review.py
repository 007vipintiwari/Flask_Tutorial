from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0.2
)

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/text-embedding-004"
)

vectorstore = PineconeVectorStore(
    index_name="ai-code-reviewer",
    embedding=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k": 6})
REVIEW_PROMPT = """
You are a senior software engineer performing a professional code review.

Review the following code and identify:
1. Bugs or logical errors
2. Performance issues
3. Security vulnerabilities
4. Code quality improvements

Provide clear, actionable feedback.
Code:
{context}
"""

def review_code(query):
    # 1. Retrieve relevant code
    docs = retriever.get_relevant_documents(query)
    # 2. Convert docs to text
    context = "\n\n".join(
        f"File: {doc.metadata['file']}\n{doc.page_content}"
        for doc in docs
    )
    # 3. Build final prompt
    prompt = REVIEW_PROMPT.format(context=context)
    # 4. Ask LLM
    response = llm.invoke(prompt)
    return response.content
print(review_code("Review this repository for security issues"))
