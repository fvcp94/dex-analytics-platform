import requests, streamlit as st

def chat(prompt):
    key = st.secrets["openrouter"]["api_key"]
    headers = {"Authorization":f"Bearer {key}"}
    payload = {
        "model":"openai/gpt-4o-mini",
        "messages":[{"role":"user","content":prompt}]
    }
    r = requests.post("https://openrouter.ai/api/v1/chat/completions",
                      headers=headers,json=payload)
    return r.json()["choices"][0]["message"]["content"]
