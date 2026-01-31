import streamlit as st
import plotly.express as px
from src.bootstrap_data import bootstrap
from src.io import load_table
from src.metrics import dex_score

st.set_page_config(layout="wide")
bootstrap()

endpoint = dex_score(load_table("endpoint_daily"))
tickets = load_table("tickets")

st.title("DEX Intelligence Platform")

daily = endpoint.groupby("date",as_index=False)["dex_score"].mean()
st.plotly_chart(px.line(daily,x="date",y="dex_score"), use_container_width=True)

st.metric("Avg DEX Score", round(endpoint["dex_score"].mean(),1))
st.metric("Total Tickets", len(tickets))
