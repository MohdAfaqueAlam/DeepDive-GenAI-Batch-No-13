from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv(override=True)

model = HuggingFaceEndpoint(
    repo_id="openai/gpt-oss-120b",
    task="Text-generation",
)

chat = ChatHuggingFace(llm=model)

response = chat.invoke("Can you write a poem about a sunset in 50 words?")  

print(response.content)

