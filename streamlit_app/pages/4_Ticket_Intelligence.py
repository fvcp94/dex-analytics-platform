import sys
from pathlib import Path

# Add repo root to PYTHONPATH so "src" imports work on Streamlit Cloud
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import plotly.express as px
from src.io import load_table

st.set_page_config(layout="wide")
st.title("Ticket Intelligence")

tickets = load_table("tickets")

st.subheader("Ticket Volume by Category")
by_cat = tickets.groupby("category", as_index=False).size()
st.plotly_chart(
    px.bar(by_cat, x="category", y="size", title="Tickets by Category"),
    use_container_width=True,
)

st.subheader("Priority Distribution")
by_priority = tickets.groupby("priority", as_index=False).size()
st.plotly_chart(
    px.bar(by_priority, x="priority", y="size", title="Tickets by Priority"),
    use_container_width=True,
)

st.subheader("MTTR Distribution (Hours)")
st.plotly_chart(
    px.histogram(tickets, x="mttr_hours", nbins=30, title="MTTR Distribution"),
    use_container_width=True,
)
