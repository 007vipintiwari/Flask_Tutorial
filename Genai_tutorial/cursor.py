import subprocess
import os
from google import genai
from google.genai import types
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from dotenv import load_dotenv
load_dotenv()


def execute_command(command: str):
    """
    Execute a shell command.
    """
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True
    )
    return {
        "stdout": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }



client = genai.Client()
config = types.GenerateContentConfig(
    tools=[execute_command],
    system_instruction = "You are a website builder expert.\
     You have to create the fronted of the website by analysing the user's input. \
     You have access of tools, which can run or execute any shell or terminal commands.\
     Current user operating system in mac os. \
     Give command to the user according to its operating system support.\
     what is you job \
     1. Analyse the user query to see what type of website he want to build .\
     2. Give them command one by one,step by step \
     3. Use available tool execute_command \
     Now you can give them command in following below.\
     1. First create a folder, ex. mkdir 'calculate'.\
     2. Inside the folder, create index.html, ex: touch 'calculator/index.html'.\
     3. Then create sytle.css same as above.\
     4. Then create script.js.\
     5. Then write a code in all the generated files. \
     You have to provide the terminal or shell command to user, they will directly execute it."
)

# Make the request
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="create a tic tac toe fully functional website for me",
    config=config,
)

# Print the final, user-facing response
print(response.text)