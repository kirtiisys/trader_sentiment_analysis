import streamlit as st
import pandas as pd

st.title("Trader Performance Dashboard")

df = pd.read_csv("historical_data.csv")

df.rename(columns={'Closed PnL':'PnL'}, inplace=True)

st.write(df.head())

sentiment = st.selectbox("Select Sentiment", ["All","Fear","Greed"])

if sentiment != "All":
    df = df[df['Sentiment'] == sentiment]

st.bar_chart(df['PnL'])

st.write("Average PnL:", df['PnL'].mean())
st.write("Total Trades:", len(df))