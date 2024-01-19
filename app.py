from datetime import datetime as dt
import pytz
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

df = pd.read_csv('data/dados_qualify_eruocup_2024.csv')

with st.sidebar:
    st.title('Groups')
    groupList = {'Group A', 'Group B', 'Group C', 'Group D', 'Group E', 'Group F', 'Group G', 'Group H', 'Group I', 'Group J'}
    selected = st.selectbox('Select Group',  df['Group'].unique().tolist())

st.title("Euro Cup 2024")
groupByGroup = df.groupby('Group')
st.header(selected)
groupByGroup = pd.DataFrame(groupByGroup.get_group(selected))
st.table(groupByGroup)


groupByGroup = df.groupby('Group')
grupo = pd.DataFrame(groupByGroup.get_group(selected))

c = (
    alt.Chart(grupo)
    .mark_circle()
    .encode(x="Wins", y="Teams", size="Points", color="Points", tooltip=["Points", "Wins", "Points"])
)

st.altair_chart(c, use_container_width=True)
