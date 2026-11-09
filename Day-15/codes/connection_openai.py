from openai import OpenAI
from config import openai_api_key1
openai_api_key = openai_api_key1
client = OpenAI(api_key=openai_api_key)

response = client.responses.create(
    model="gpt-4o-mini",
    input="Write a one-sentence about agentic ai"
)

print(response.output_text)