import streamlit as st
import yfinance as yf
from datetime import datetime
import pandas as pd

df = pd.read_csv("data/bats_symbols.csv")
simbols = df['Name'].unique()

st.subheader("Stocks App")
symbol = st.selectbox("Select Action", simbols)
if st.button("Get Quote"):
    amzn = yf.Ticker(symbol)
    end_date = datetime.now().strftime('%Y-%m-%d')
    amzn_hist = amzn.history(start='2024-01-01',end=end_date)
    st.table(amzn_hist)
