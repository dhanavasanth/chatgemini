import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="GenAI", page_icon=":robot_face:", layout="wide")

st.title("Google gemini chatbot")


api_key = st.secrets["gemini_api_key"]

genai.configure(api_key = api_key)

model = genai.GenerativeModel('gemini-pro')

prompt = st.chat_input("Enter a prompt:")

if prompt is not None:
    response = model.generate_content()

    st.write(response.text)