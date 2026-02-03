import sys
from pathlib import Path

# Ensure repo root is on PYTHONPATH (fixes "No module named src" on Streamlit Cloud)
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import plotly.express as px

from src.bootstrap_data import bootstrap
from src.io import load_table
from src.metrics import dex_score

st.set_page_config(page_title="DEX Intelligence Platform", layout="wide")

# Ensure synthetic demo data exists
bootstrap()

endpoint = dex_score(load_table("endpoint_daily"))
tickets = load_table("tickets")

st.title("DEX Intelligence Platform")

# Daily DEX score trend
daily = endpoint.groupby("date", as_index=False)["dex_score"].mean()
st.plotly_chart(px.line(daily, x="date", y="dex_score", title="Daily Avg DEX Score"), use_container_width=True)

c1, c2 = st.columns(2)
c1.metric("Avg DEX Score", round(endpoint["dex_score"].mean(), 1))
c2.metric("Total Tickets", int(len(tickets)))
