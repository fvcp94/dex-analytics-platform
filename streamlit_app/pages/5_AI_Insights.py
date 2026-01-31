import streamlit as st
from src.llm_openrouter import chat

st.title("AI Insights")

q = st.text_area("Ask about DEX issues")
if st.button("Ask AI") and q:
    st.write(chat(q))
