from google import genai
from dotenv import load_dotenv
load_dotenv()
client = genai.Client()
chat = client.chats.create(model="gemini-2.5-flash")

response = chat.send_message("I have to learn about low level system design")
print(response.text)

response = chat.send_message("can you please provide the link of Martin Fowler, Google Engineering, Netflix Tech Blog, Uber Engineering, Medium articles on software design")
print(response.text)
for message in chat.get_history():
    print(f'role - {message.role}',end=": ")
    print(message.parts[0].text)