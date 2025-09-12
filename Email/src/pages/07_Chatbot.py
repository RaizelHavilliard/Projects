# src/pages/07_Chatbot.py
import streamlit as st
from llama_cpp import Llama
import os

st.title("🤖 AI Chatbot")

# Path to your downloaded model
MODEL_PATH = "/home/raizel11/Projects/Projects/Models/llama-2-7b-chat.gguf"

# Load model only once and cache it
@st.cache_resource
def load_model():
    return Llama(
        model_path=MODEL_PATH,
        n_ctx=1024,
        n_threads=8
    )

llm = load_model()

# Conversation memory
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Show past messages
for role, text in st.session_state["messages"]:
    with st.chat_message(role):
        st.markdown(text)

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # User message
    st.session_state["messages"].append(("user", prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            output = llm(prompt, max_tokens=50, stop=["</s>"])
            response = output["choices"][0]["text"].strip()
            st.markdown(response)

    st.session_state["messages"].append(("assistant", response))
