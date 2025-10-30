from openai import OpenAI
from dotenv import load_dotenv
load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-oss-120b",
    input="Can you write a poem about a sunset in 50 words?",
)

print(response.output_text)