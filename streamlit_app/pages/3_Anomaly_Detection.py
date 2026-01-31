import streamlit as st
import plotly.express as px
from src.io import load_table
from src.anomaly import detect

df = load_table("endpoint_daily").groupby("date",as_index=False)["app_latency_ms"].mean()
df = detect(df,"app_latency_ms")

st.title("Anomaly Detection")
st.plotly_chart(px.line(df,x="date",y="app_latency_ms", color=df["anomaly"].astype(str)))
