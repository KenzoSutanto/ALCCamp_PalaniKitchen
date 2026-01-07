import streamlit as st
from openai import OpenAI
st.set_page_config(
    page_title="Help"
)

client = OpenAI(
    api_key=""
)


st.title("Need Help with your order? Our assistant has you")
texts = st.container()
if prompt := st.chat_input("Insert your queries here", max_chars=6767):
    texts.chat_message("user").write(prompt)
    response = client.responses.create(
    model="gpt-5-nano",
    instructions="Customer Service Agent",
    input=prompt,)
    texts.chat_message("Customer Service").write(response.output_text)
