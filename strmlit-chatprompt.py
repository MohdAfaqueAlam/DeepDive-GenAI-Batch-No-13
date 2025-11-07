from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

#----------------------Streamlit UI----------------------#

st.title("Get Key Achievements")
st.header("You can find key achievements of any person in any category using Llama3.2 model")
st.write("Enter the details below:")

#----------------------Input Fields----------------------#

person = st.text_input("Enter Person's Name:")
category = st.text_input("Enter Category e.g., science, sports, literature:")

#----------------------Button and Output----------------------#
if st.button("Clear Fields"):
    st.write("Please remove the fields manually")
if st.button("copy the result"):
    st.write("To copy the result, please select the text and use Ctrl+C (Cmd+C on Mac) to copy it.")
if st.button("Get Achievements"):
    with st.spinner("Fetching achievements..."):
        if not person or not category:
            st.warning("Please enter both person's name and category.")
        else:
            try:
                prompt = ChatPromptTemplate.from_template("Tell me 4 key achievements of {person} in {category}.")

                llm = ChatOllama(model="llama3.2:latest")

                chain = prompt | llm

                response = chain.invoke({"person": person, "category": category})
                st.subheader("Key Achievements:")    
                st.write(response.content)
            except Exception as e:
                st.error(f"An error occurred: {e}")
