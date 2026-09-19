import requests
import streamlit as st
st.title("Message Processor")
message = st.text_input("Enter your message")

if st.button("Process Message"):
    response = requests.post("http://localhost:8000/process", json={"message": message})
    result = response.json()
    st.subheader(result)

    st.write(result["message"])
    st.write(message)
    st.warning(f"Length of the message: {result['length']}")
    st.info(f"Reversed message: {result['reversed']}")  