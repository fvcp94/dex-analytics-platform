import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
import plotly.express as px

from src.bootstrap_data import bootstrap
from src.io import load_table
from src.anomaly import detect

st.set_page_config(layout="wide")
st.title("Anomaly Detection")

bootstrap()

df = load_table("endpoint_daily").groupby("date", as_index=False)["app_latency_ms"].mean()
df = detect(df, "app_latency_ms")

df["anomaly_flag"] = df["anomaly"].astype(str)

st.plotly_chart(
    px.line(df, x="date", y="app_latency_ms", color="anomaly_flag", title="App Latency (Anomaly Flag)"),
    use_container_width=True,
)
