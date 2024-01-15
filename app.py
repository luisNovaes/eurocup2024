from datetime import datetime as dt
import pytz
import streamlit as st
import pandas as pd

df = pd.read_csv('data/dados_qualify_eruocup_2024.csv')
st.title("Euro Cup 2024")
st.table(df)