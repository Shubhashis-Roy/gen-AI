from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

response = client.responses.create(
  model="gpt-5-nano",
  input="Hi there! How are you?",
  store=True,
)

print(response.output_text)
