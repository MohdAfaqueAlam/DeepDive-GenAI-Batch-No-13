from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template("Tell me 4 key achievements of {person} in {category}.")

llm = ChatOllama(model="llama3.2:latest")

chain = prompt | llm

response = chain.invoke({"person": "Albert Einstein", "category": "science"})

print(response.content)