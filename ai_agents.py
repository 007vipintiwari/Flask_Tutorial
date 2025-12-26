from openai import OpenAI
from pydantic import BaseModel

import google.generativeai as genai

# Step 1: Authenticate
genai.configure(api_key=GOOGLE_API_KEY)

# Step 2: Initialize the Gemini model
model = genai.GenerativeModel('gemini-pro')

# Step 3: Start a chat
chat = model.start_chat()

# Step 4: Send a message and get response
response = chat.send_message("Tell me a joke about programmers.")

# Step 5: Print response
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