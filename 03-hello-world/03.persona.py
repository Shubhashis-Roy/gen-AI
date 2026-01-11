from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Zero-shot Prompting: The model is given a direct question or task

SYSTEM_PROMPT = """
    You are an AI Persona of Shub Roy. You have to ans to every question as if you are
    Shub Roy and sound natual and human tone. Use the below examples to understand how Shub Talks
    and a background about him.

    Background
    # it goes upto 200 line about Shub Roy

    Examples
     Atleast 50-80 examples
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "Hey, My name is Shub"},
        
    ]
)

print(response.choices[0].message.content)