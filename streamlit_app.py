import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def main():
    api_key = st.text_input("Enter API key")
    if not api_key:
        with st.sidebar:
            api_key = st.text_input("Enter the Open AI api key here")
    
    input_text = st.text_area("Enter the input for JIRA story creation")

    if st.button("Create task"):
        with st.spinner("Creating the task"):
            llm = ChatOpenAI(model = "gpt-4o-mini", api_key = api_key, temperature = 0.7, max_tokens = 1024)

            prompt = ChatPromptTemplate.from_messages([
                ("system", """Act as a helpful expert scrum master and create task for the story defined, you will not use extremely technique terms, just be generic. The task should have the following structure.

    Title : Title goes here

    Description : Description goes here

    Acceptance criteria : Acceptance goes here"""),
                ("human", "{input_text}"),
            ])

            chain = prompt | llm
            result = chain.invoke({
                "input_text": input_text
            })

            st.write(result.content) 

if __name__ == "__main__":
    main()