import streamlit as st
from openai import OpenAI
import chromadb

st.set_page_config(page_title="Help")
st.title("Need Help with your order? Our assistant has you")

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

with open(r"pages/SOP/palanis_kitchen_menu.txt", "r", encoding="utf-8") as f:
    menu = f.read()

with open(r"pages/SOP/palanis_kitchen_customer_service_rules.txt", "r", encoding="utf-8") as f:
    rules = f.read()

chroma = chromadb.PersistentClient(path=".chroma")
col = chroma.get_or_create_collection(name="palanis_kitchen")

def embed(text):
    return client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    ).data[0].embedding

if col.count() == 0:
    col.add(
        ids=["menu", "rules"],
        documents=[menu, rules],
        embeddings=[embed(menu), embed(rules)],
        metadatas=[{"source": "menu"}, {"source": "rules"}]
    )

def retrieve(query, k=8):
    res = col.query(
        query_embeddings=[embed(query)],
        n_results=k
    )
    docs = res["documents"][0] if res.get("documents") else []
    return "\n\n".join(docs)

if "messages" not in st.session_state:
    st.session_state.messages = []

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

prompt = st.chat_input("Insert your queries here", max_chars=6767)

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    context = retrieve(prompt, k=8)

    system = (
        "You are a customer service agent for the restaurant Palani's Kitchen. "
        "Use ONLY the context provided. If the answer is not in the context, say you don't know.\n\n"
        "CONTEXT:\n"
        f"{context}"
    )

    msgs = [{"role": "system", "content": system}] + st.session_state.messages

    with st.chat_message("assistant"):
        def gen():
            stream = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=msgs,
                stream=True
            )
            for event in stream:
                delta = event.choices[0].delta
                if delta and delta.content:
                    yield delta.content

        full = st.write_stream(gen())

    st.session_state.messages.append({"role": "assistant", "content": full})
