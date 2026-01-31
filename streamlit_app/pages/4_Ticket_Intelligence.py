import streamlit as st
import plotly.express as px
from src.io import load_table

tickets = load_table("tickets")
st.title("Ticket Intelligence")

by_cat = tickets.groupby("category",as_index=False).size()
st.plotly_chart(px.bar(by_cat,x="category",y="size"))
