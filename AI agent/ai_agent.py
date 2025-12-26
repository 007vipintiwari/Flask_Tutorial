from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
#
#
load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini")
llm2 = ChatAnthropic(model="claude-3.5-sonnet-20241022")
response = llm2.invoke("what is the meaning of life ?")
print(f"response from anthropic : {response}")
from openai import OpenAI
from pydantic import BaseModel
from google import genai
import os
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="I have to appear for SDE-2 interview at Amazon in 1 week,please suggest day by day plan to prepare how to prepare for LLD, HLD and coding rounds with problems and solutions also",
)

print(response.text)
import google.generativeai as genai

Step 1: Authenticate
genai.configure()

Step 2: Initialize the model
model = genai.GenerativeModel(model_name="gemini-pro")

Step 3: Generate content
response = model.generate_content("Write a poem about artificial intelligence.")

Step 4: Print the response
print(response.text)

import google.generativeai as genai

Step 1: Authenticate
genai.configure()

Step 2: Initialize the Gemini model
model = genai.GenerativeModel('gemini-pro')

Step 3: Start a chat
chat = model.start_chat()

Step 4: Send a message and get response
response = chat.send_message("Tell me a joke about programmers.")

Step 5: Print response
print(response.text)

client = OpenAI()

class Step(BaseModel):
    explanation: str
    output: str

class MathReasoning(BaseModel):
    steps: list[Step]
    final_answer: str

response = client.responses.parse(
    model="gpt-4o-2024-08-06",
    input=[
        {
            "role": "system",
            "content": "You are a helpful math tutor. Guide the user through the solution step by step.",
        },
        {"role": "user", "content": "how can I solve 8x + 7 = -23"},
    ],
    text_format=MathReasoning,
)

math_reasoning = response.output_parsed



