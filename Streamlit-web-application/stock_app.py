import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime

# Title of the app
st.title('Stock Price Visualizer')
st.write("This is a simple web application built using [Streamlit](https://streamlit.io/) that allows users to visualize historical stock prices for a given stock ticker symbol. Users can enter a stock ticker, select a date range, and view the stock's closing prices plotted on a chart.")

# Input for the stock ticker
ticker_symbol = st.text_input('Enter Stock Ticker Symbol', 'AAPL')

# Input for start and end dates
start_date = st.date_input('Start Date', datetime(2020, 1, 1))
end_date = st.date_input('End Date', datetime.today())

# Button to trigger data loading
if st.button('Show Stock Prices'):
    if start_date >= end_date:
        st.error('Error: End date must fall after start date.')
    else:
        # Fetching the stock data
        stock_data = yf.download(ticker_symbol, start=start_date, end=end_date)
        
        # Displaying the stock data in a table
        st.write(stock_data)

        # Plotting the closing price
        st.subheader('Closing Price')
        plt.figure(figsize=(10, 4))
        plt.plot(stock_data['Close'])
        plt.xlabel('Date')
        plt.ylabel('Closing Price (USD)')
        plt.title(f'Closing Price of {ticker_symbol}')
        st.pyplot(plt)
