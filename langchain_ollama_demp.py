from langchain_ollama import ChatOllama

llm = ChatOllama(model="phi3:latest")
response = llm.invoke("What is agentic AI?. describe in 50 words")

print(response.content)
