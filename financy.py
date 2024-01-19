import streamlit as st
import yfinance as yf
from datetime import datetime
import pandas as pd

df = pd.read_csv("data/bats_symbols.csv")
simbols = df['Name'].unique()

st.subheader("Stocks App")
symbol = st.selectbox("Select Action", simbols)
start_date = st.date_input("Insert start date").strftime('%Y-%m-%d')
end_date = st.date_input("Insert end date").strftime('%Y-%m-%d')
if st.button("Get Quote"):
    amzn = yf.Ticker(symbol)
    amzn_hist = amzn.history(start=start_date, end=end_date)
    st.table(amzn_hist)

