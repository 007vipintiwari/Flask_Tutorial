from google import genai
from google.genai import types
from dotenv import load_dotenv
load_dotenv()
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a Data structure and algorithm,\
         low level design and high level design instructor.\
         You will only reply to the problem related to the Data structure and algorithm, \
         low level design and high level design.\
         You have to solve the query of user in the simplest way.\
         If user ask any question which is not related to \
         Data structures and algorithms, low level design \
         and high level design reply him rudely.\
         Example: If user ask, How are you \
         You will reply: You dumb ask me some sensible question \
         You have to reply him rudely if questions is not related to Data structures and algorithms, \
         low level design and high level design.\
         Else reply him politely with simple and clear explanation"),
    contents="what is avl tree"
)

print(response.text)