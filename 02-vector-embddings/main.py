from openai import OpenAI
from dotenv import load_dotenv
# import os

load_dotenv()
# print(os.getenv("OPENAI_API_KEY"))

client = OpenAI()
 
text = "Dog chases cat"

response = client.embeddings.create(
    model="text-embedding-3-small", 
    input=text,
)

print(response)

print("length:", response.data[0].embedding.__len__()) 
