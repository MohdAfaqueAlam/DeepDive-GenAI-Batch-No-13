from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

model = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=model)

response = model.invoke("Can you write a short story on friendship in about 100 words?")  

print(response.content)