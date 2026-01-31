import sys
from pathlib import Path

# Add repo root to PYTHONPATH so "src" imports work on Streamlit Cloud
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import pandas as pd

from src.io import load_table
from src.metrics import dex_score
from src.llm_openrouter import chat

st.set_page_config(layout="wide")
st.title("AI Insights (Digital Employee Experience)")

st.caption("GenAI is used for explainability only. Analytics remain deterministic and data-grounded.")

# Load data
endpoint = dex_score(load_table("endpoint_daily"))
tickets = load_table("tickets")

# Build daily KPI table (ground truth for the LLM)
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

daily = daily_kpis.merge(ticket_daily, on="date", how="left").fillna({"tickets": 0, "avg_mttr_h": 0})
daily = daily.sort_values("date")

st.subheader("Latest DEX KPIs (ground truth)")
st.dataframe(daily.tail(10), use_container_width=True)

# Pick "last night" date (latest date in dataset)
latest_date = pd.to_datetime(daily["date"].max()).date()
picked = st.date_input("Date to analyze (defaults to latest)", value=latest_date)

query = st.text_area(
    "Ask a question about Digital Employee Experience (DEX) trends, incidents, or anomalies",
    value="Why did the DEX score drop last night?",
)

if st.button("Generate AI Explanation"):
    picked_ts = pd.to_datetime(picked)

    # Context window around picked date
    window = daily[(daily["date"] >= picked_ts - pd.Timedelta(days=7)) & (daily["date"] <= picked_ts)].copy()

    # Pull yesterday vs day-before comparison if possible
    y = window[window["date"] == picked_ts]
    prev = window[window["date"] == picked_ts - pd.Timedelta(days=1)]

    prompt = f"""
You are a Digital Workplace / IT Service Governance analytics assistant.
IMPORTANT: In this app, "DEX" means Digital Employee Experience (not crypto exchanges).

Answer the user's question using ONLY the provided KPI table (aggregated metrics).
If you cannot conclude, say exactly what additional data would be needed.

User question:
{query}

KPI window (CSV):
{window.to_csv(index=False)}

Focus date: {picked_ts.date()}
If available, compare this date to the previous day and last 7-day baseline.

Return format:
1) Executive summary (2-3 bullets)
2) What changed in DEX score (numbers)
3) Likely drivers (latency/login/crash/device health/tickets) with evidence
4) Recommended next actions (safe, human-in-the-loop)
"""

    with st.spinner("Generating..."):
        response = chat(prompt)
    st.subheader("AI Explanation (data-grounded)")
    st.write(response)
