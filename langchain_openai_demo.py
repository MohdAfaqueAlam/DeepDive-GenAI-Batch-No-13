# from langchain_openai import OpenAI
# from dotenv import load_dotenv  
# load_dotenv()

# llm = OpenAI(model="gpt-oss-120b")
# response = llm.predict("Can you write a poem about a sunset in 50 words?")
# print(response.text)

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-oss-120b")

response = llm.invoke("ECan you write a poem about a sunset in 50 words?")

print(response.content)

#response = client.responses.create(
#    model="gpt-4o-mini",
#    input="Explain the theory of relativity in simple terms.",