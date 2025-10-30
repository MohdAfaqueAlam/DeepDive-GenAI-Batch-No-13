from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-2.5-pro")

response = llm.invoke("Can you write a poem about a sunset in 50 words?")

print(response)