# from langchain_google_genai import GoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# llm = GoogleGenerativeAI(model="gemini-2.5-pro")

# response = llm.invoke("Can you write a poem about a sunset in 50 words?")

# print(response)

# create a basic model to generate text using LangChain and Google Gemini 2.5 Flash
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

from dotenv import load_dotenv  
load_dotenv()

#---------------------------Streamlit Interface---------------------------#
st.title("Google Gemini 2.5 Flash Poem Generator")
st.header("Generate a Poem about a Sunset")
st.write("This app uses Google Gemini 2.5 Flash model to generate a poem about a sunset based on your input prompt.")

#---------------------------LangChain Google Gemini 2.5 Flash Integration---------------------------#

topic = st.text_input("Enter your topic:", "Can you write a poem about a sunset in 50 words?")
WordCount = st.slider("Select the word count for the poem:", 10, 100, 50)

#---------------------------Generate Poem on Button Click---------------------------#
if st.button("Generate Poem"):
     prompt = f"Can you write a poem about {topic} in {WordCount} words?"
     
     llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
     response = llm.invoke(prompt)
     
     st.subheader("Generated Poem:")
     st.write(response.content)






# llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# response = llm.invoke("Can you write a poem about a sunset in 50 words?")
# print(response.content)

# # adding streamlit interface

# st.title("Google Gemini 2.5 Flash Poem Generator")
# user_input = st.text_input("Enter your prompt:", "Can you write a poem about a sunset in 50 words?")
# if st.button("Generate Poem"):
#     response = llm.invoke(user_input)
#     st.write(response.content)  

