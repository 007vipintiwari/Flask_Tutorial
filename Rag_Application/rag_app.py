from google import genai
from google.genai import types
import httpx
import  pathlib

client = genai.Client(api_key="AIzaSyDT7j3KFs9tRMbJ4-r664bM5wbkovBExUo")

# doc_url = "https://discovery.ucl.ac.uk/id/eprint/10089234/1/343019_3_art_0_py4t4l_convrt.pdf"
# doc_url ="https://drive.google.com/file/d/1QAOL..."
# Retrieve and encode the PDF byte
file_path = pathlib.Path("Dsa.pdf")
# doc_data = httpx.get(doc_url).content

prompt = "Summarize this document"
response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[
      types.Part.from_bytes(
        data=file_path.read_bytes(),
        mime_type='application/pdf',
      ),
      prompt])
print(response.text)