import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import pandas as pd

from src.bootstrap_data import bootstrap
from src.io import load_table
from src.metrics import dex_score
from src.llm_openrouter import chat

st.set_page_config(layout="wide")
st.title("AI Insights (Digital Employee Experience)")

bootstrap()

endpoint = dex_score(load_table("endpoint_daily"))
tickets = load_table("tickets")

daily_kpis = endpoint.groupby("date", as_index=False).agg(
    avg_dex=("dex_score", "mean"),
    avg_latency_ms=("app_latency_ms", "mean"),
    avg_login_s=("login_time_s", "mean"),
    crash_rate=("crash_rate", "mean"),
    device_health=("device_health", "mean"),
    users=("user_id", "nunique"),
)

ticket_daily = tickets.groupby("date", as_index=False).agg(
    tickets=("ticket_id", "count"),
    avg_mttr_h=("mttr_hours", "mean"),
)

daily = (
    daily_kpis.merge(ticket_daily, on="date", how="left")
    .fillna({"tickets": 0, "avg_mttr_h": 0})
    .sort_values("date")
)

st.caption("GenAI is used for explainability only. DEX = Digital Employee Experience (not crypto).")
st.dataframe(daily.tail(10), use_container_width=True)

latest_date = pd.to_datetime(daily["date"].max()).date()
picked = st.date_input("Date to analyze", value=latest_date)

question = st.text_area(
    "Ask about workplace DEX changes (endpoint/app experience)",
    value="Why did the DEX score drop last night?"
)

if st.button("Generate AI Explanation"):
    picked_ts = pd.to_datetime(picked)
    window = daily[(daily["date"] >= picked_ts - pd.Timedelta(days=7)) & (daily["date"] <= picked_ts)].copy()

    prompt = f"""
You are a Digital Workplace / IT Service Governance analytics assistant.
IMPORTANT: "DEX" means Digital Employee Experience (endpoint/app experience), not crypto exchanges.

Answer the user's question using ONLY the KPI table provided (aggregated metrics).
If you cannot conclude, state what additional data is needed.

User question:
{question}

KPI window (CSV):
{window.to_csv(index=False)}

Focus date: {picked_ts.date()}

Return format:
1) Executive summary (2-3 bullets)
2) What changed in DEX score (numbers)
3) Likely drivers with evidence (latency/login/crash/device health/tickets)
4) Recommended next actions (safe, human-in-the-loop)
"""

    with st.spinner("Generating..."):
        try:
            response = chat(prompt)
            st.subheader("AI Explanation (data-grounded)")
            st.write(response)
        except Exception as e:
            st.error(f"GenAI request failed: {e}")
            st.info("Check Streamlit Cloud → Settings → Secrets for [openrouter] api_key and model.")
