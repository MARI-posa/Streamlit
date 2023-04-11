import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Графики, построенные с использованием данных о котировках компании Apple c помощью библиотеки yfinance:


""")
         
st.write("""
# 


""")

tickerSymbol = 'AAPL'

tickerData = yf.Ticker(tickerSymbol)

tickerDF = tickerData.history(period='id', start='2010-5-31', end='2020-5-31')


st.line_chart(tickerDF.Close)
st.line_chart(tickerDF.Volume)