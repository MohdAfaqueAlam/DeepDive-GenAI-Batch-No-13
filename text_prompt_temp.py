from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("Write a story about {person} in {number} words.")

llm = ChatOllama(model="llama3.2:latest")

chain = prompt | llm

response = chain.invoke({"person": "Alice", "number": 100})

print(response.content)