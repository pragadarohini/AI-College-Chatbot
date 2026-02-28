import streamlit as st
import json

# Load data
with open("data.json", "r") as file:
    data = json.load(file)

st.title("AI Based College Enquiry Chatbot")

user_input = st.text_input("Ask your question:")

if user_input:
    user_input = user_input.lower()

    if "hello" in user_input:
        st.write(data["greeting"])
    elif "course" in user_input:
        st.write(data["courses"])
    elif "admission" in user_input:
        st.write(data["admission"])
    elif "contact" in user_input:
        st.write(data["contact"])
    else:
        st.write("Sorry, I don't understand your question.")