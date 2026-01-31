import sys
from pathlib import Path

# Add repo root to PYTHONPATH so "src" imports work on Streamlit Cloud
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from src.llm_openrouter import chat

st.set_page_config(layout="wide")
st.title("AI Insights (GenAI-assisted)")

st.markdown(
    """
This page uses **GenAI via OpenRouter** to provide **explainability and insights**
on Digital Employee Experience (DEX) trends.

- Analytics and anomaly detection remain deterministic
- LLMs are used only for summarization and reasoning
- No raw endpoint-level data is exposed
"""
)

query = st.text_area(
    "Ask a question about DEX trends, incidents, or anomalies",
    placeholder="Why did DEX score drop last week?"
)

if st.button("Generate Insight"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating insight..."):
            try:
                response = chat(query)
                st.markdown("### AI Explanation")
                st.write(response)
            except Exception as e:
                st.error(
                    "GenAI is not configured. Please add OpenRouter secrets in Streamlit Cloud."
                )
