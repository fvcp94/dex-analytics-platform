import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import plotly.express as px

from src.bootstrap_data import bootstrap
from src.io import load_table

st.set_page_config(layout="wide")
st.title("Ticket Intelligence")

bootstrap()

tickets = load_table("tickets")

st.subheader("Tickets by Category")
by_cat = tickets.groupby("category", as_index=False).size()
st.plotly_chart(px.bar(by_cat, x="category", y="size"), use_container_width=True)

st.subheader("Tickets by Priority")
by_priority = tickets.groupby("priority", as_index=False).size()
st.plotly_chart(px.bar(by_priority, x="priority", y="size"), use_container_width=True)

st.subheader("MTTR Distribution (hours)")
st.plotly_chart(px.histogram(tickets, x="mttr_hours", nbins=30), use_container_width=True)
