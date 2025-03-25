import streamlit as st
from chatbotAssignment import generate_response


st.title("GPT Chatbot")
user_input = st.text_input("You: ")
if user_input:
    response = generate_response(user_input)
    st.text_area("Bot:", value=response, height=200)


