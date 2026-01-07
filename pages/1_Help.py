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

with open(r"pages/SOP/palanis_kitchen_menu.txt" , "r" ,encoding="utf-8") as menu:
    MenuData = menu.read()
with open(r"pages/SOP/palanis_kitchen_customer_service_rules.txt" , "r" ,encoding="utf-8") as rules:
    Ruleset = rules.read()
vector_store = Chroma.from_texts(
    texts=[MenuData,Ruleset],
)

@dynamic_prompt
def contexting_prompt(request: ModelRequest) -> str:
    last_query = request.state["messages"][-1].text
    sources = vector_store.similarity_search(last_query, k=20)
    docs_content = "\n\n".join(doc.page_content for doc in sources)
    print(docs_content)
    sys_msg = (f"You are a customer service agent for the restaurant Palani's Kitchen use the following context in your response {docs_content}")

    return sys_msg
model = ChatOpenAI(model = 'gpt-4o-mini', api_key=st.secrets["OPENAI_API_KEY"])
qa_agent = create_agent(model, tools=[], middleware=[contexting_prompt])

def invoke_qa_agent(prompt):
    return qa_agent.invoke({"messages": [{"role":"user", "content":prompt}]})


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

st.title("Need Help with your order? Our assistant has you")
texts = st.container()
if prompt := st.chat_input("Insert your queries here", max_chars=6767):
    st.session_state.messages.append({"role":"user", "content":prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = invoke_qa_agent(prompt)
        stream = texts.chat_message("Customer Service").write(response['messages'][1].content)
        st.write(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

#new stuff
