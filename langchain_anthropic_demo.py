from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model_name="claude-2")

try:
    response = llm.invoke("Can you write a poem about a sunset in 50 words?")
    print(response)
except Exception as e:
    print(f"Error: {e}")