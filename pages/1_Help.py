import streamlit as st
from openai import OpenAI
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.agents import AgentState, create_agent
from langchain.agents.middleware import dynamic_prompt, ModelRequest
st.set_page_config(
    page_title="Help"
)

client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

with open("/SOP/palanis_kitchen_menu") as menu:
    None
with open("/SOP/palanis_kitchen_customer_service_rules") as rules:
    None
vector_store = Chroma.from_texts(
    texts=[menu,rules],
)

def contexting_prompt(request: ModelRequest) -> str:
    sources = vector_store.similarity_search(request, k=20)
    sys_msg = (f"You are a customer service agent for the restaurant Palani's Kitchen use the following context in your response {sources}")

    return sys_msg
model = ChatOpenAI(model = 'gpt-5-nano')
qa_agent = create_agent(model, tools=[], middleware=[contexting_prompt])

def invoke_qa_agent(prompt):
    return qa_agent.invoke({"messages": [{"role":"user", "content":prompt}]})



st.title("Need Help with your order? Our assistant has you")
texts = st.container()
if prompt := st.chat_input("Insert your queries here", max_chars=6767):
    texts.chat_message("user").write(prompt)
    response = invoke_qa_agent(prompt)
    texts.chat_message("Customer Service").write(response['messages'][1].content)

