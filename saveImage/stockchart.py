import matplotlib.pyplot as plt
from mplfinance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates
import pandas_datareader as web

plt.style.use('ggplot')

# Extracting Data for plotting
data = pd.read_csv('data.csv')
# data = web.DataReader('MSFT', data_source='yahoo', start='01-01-2019')
ohlc = data.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
ohlc['Date'] = pd.to_datetime(ohlc['Date'])
ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
ohlc = ohlc.astype(float)

# Creating Subplots
fig, ax = plt.subplots()
type(ax)
candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)

# Setting labels & titles
ax.set_xlabel('Date')
ax.set_ylabel('Price')
fig.suptitle('Daily Candlestick Chart of NIFTY50')

# Formatting Date
date_format = mpl_dates.DateFormatter('%d-%m-%Y')
ax.xaxis.set_major_formatter(date_format)
fig.autofmt_xdate()

fig.tight_layout()

plt.savefig("mygraph.png")