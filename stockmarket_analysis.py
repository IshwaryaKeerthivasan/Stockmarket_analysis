# -*- coding: utf-8 -*-
"""Stockmarket analysis Amazon .ipynb

# Amazon Stock Market Analysis

## This Project focuses on getting to know about yfinance and analyzing the company's stock market.

Step 1: Look for the yfinance website check for data and decide whether it is suitable for your analysis.

Step 2: Install and load the necessary libraries.

Step 3: Load the data and prepare them for further analysis.

# Install and load libraries
"""
import sys
print(sys.version)

#Download, install, and load all the necessary libraries!
!pip install yfinance
!pip install TA-Lib

import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import talib
import plotly.express as px
import plotly.graph_objects as go



"""# Look for the data and choose the company that you want to analyze. Further, Load that data with the required columns."""
ticket_symbol = "AMZN"
amazon_data = yf.Ticker(ticket_symbol)
historical_data = amazon_data.history(period="1y")
historical_data.head()



"""# Amazon Stock Price Analysis - Loading and Preprocessing"""
amazon_share_price_data=amazon_data.history(period='max')
amazon_share_price_data.head()
amazon_share_price_data.reset_index(inplace=True)
amazon_share_price_data.dtypes
amazon_share_price_data.isnull().any()



"""# Visual representation of Amazon's financial performance over time"""
# Amazon Opening Stock Price
fig = px.line(amazon_share_price_data, x='Date', y='Open', title='Amazon Opening Stock Price')
fig.update_traces(line=dict(color='red'))
average_open_price = amazon_share_price_data['Open'].mean()
fig.add_shape(
    type="line",
    x0=amazon_share_price_data['Date'].min(),
    x1=amazon_share_price_data['Date'].max(),
    y0=average_open_price,
    y1=average_open_price,
    line=dict(color="green", width=2, dash="dash")
)
fig.show()

# Amazon Closing Stock Price
fig = px.line(amazon_share_price_data, x='Date', y='Close', title='Amazon Closing Stock Price')
fig.update_traces(line=dict(color='green'))
average_open_price = amazon_share_price_data['Close'].mean()
fig.add_shape(
    type="line",
    x0=amazon_share_price_data['Date'].min(),
    x1=amazon_share_price_data['Date'].max(),
    y0=average_open_price,
    y1=average_open_price,
    line=dict(color="red", width=2, dash="dash")
)
fig.show()


#Profit and Loss for the Last 6 Months
six_months_ago = pd.to_datetime('today', utc=True) - pd.DateOffset(months=6)
last_6_months = amazon_share_price_data.loc[amazon_share_price_data['Date'] >= six_months_ago].copy()
last_6_months['Profit/Loss'] = last_6_months['Close'] - last_6_months['Open']
fig = go.Figure()

fig.add_trace(go.Bar(x=last_6_months['Date'],
                     y=last_6_months['Profit/Loss'],
                     marker_color=last_6_months['Profit/Loss'].apply(lambda x: 'rgba(0, 255, 0, 0.7)' if x > 0 else 'rgba(255, 0, 0, 0.7)')))

fig.update_layout(title='Profit and Loss for the Last 6 Months',
                  xaxis_title='Date',
                  yaxis_title='Profit/Loss',
                  xaxis_rangeslider_visible=False)

fig.show()



# Analyze the trend over time  - Long and Short time SMA for further understanding
# Calculate simple moving averages (SMA)
historical_data['SMA_50'] = historical_data['Close'].rolling(window=50).mean()
historical_data['SMA_200'] = historical_data['Close'].rolling(window=200).mean()
historical_data = amazon_data.history(period="5y")
historical_data['RSI'] = talib.RSI(historical_data['Close'], timeperiod=14)

# Calculate the 50-day and 200-day simple moving averages with a rolling window
historical_data['SMA_50'] = historical_data['Close'].rolling(window=50).mean()
historical_data['SMA_200'] = historical_data['Close'].rolling(window=200).mean()
historical_data.dropna(inplace=True)
fig = go.Figure()
fig.add_trace(go.Scatter(x=historical_data.index, y=historical_data['Close'], mode='lines', name='Stock Price', line=dict(color='green')))
fig.add_trace(go.Scatter(x=historical_data.index, y=historical_data['SMA_50'], mode='lines', name='50-Day SMA', line=dict(color='red')))
fig.update_layout(
    title=f"Stock Price and 50-Day SMA for {ticket_symbol}",
    xaxis_title="Date",
    yaxis_title="Price",
    showlegend=True
)

fig.show()

# Stock Price analysis 50-Day SMA & 200-Day SMA for AMZN
fig = go.Figure()
fig.add_trace(go.Scatter(x=historical_data.index, y=historical_data['Close'], mode='lines', name='Stock Price', line=dict(color='blue')))
fig.add_trace(go.Scatter(x=historical_data.index, y=historical_data['SMA_50'], mode='lines', name='50-Day SMA', line=dict(color='green')))
fig.add_trace(go.Scatter(x=historical_data.index, y=historical_data['SMA_200'], mode='lines', name='200-Day SMA', line=dict(color='red')))
fig.update_layout(
    title=f"Stock Price Analysis for {ticket_symbol}",
    xaxis_title="Date",
    yaxis_title="Price",
    showlegend=True
)
fig.show()


# SMA - 50 Regression analysis to understand  whether the stock prizes are in an increasing trend or decreasing trend.
X = historical_data[['SMA_50']]
X = sm.add_constant(X)
y = historical_data['Close']
model = sm.OLS(y, X).fit()
print(model.summary())
fig = px.scatter(historical_data, x='SMA_50', y='Close', trendline="ols", title="Scatter Plot with Regression Line")
fig.show()
