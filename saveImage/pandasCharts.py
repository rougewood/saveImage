import pandas as pd

import mplfinance as fplt

apple_df = pd.read_csv('AAPL_data.csv', index_col=0, parse_dates=True)


# Plot candlestick.
# Add volume.
# Add moving averages: 3,6,9.
# Save graph to *.png.
# ['blueskies',
#  'brasil',
#  'charles',
#  'checkers',
#  'classic',
#  'default',
#  'mike',
#  'nightclouds',
#  'sas',
#  'starsandstripes',
#  'yahoo']
mc = fplt.make_marketcolors(up='g',down='r')
s  = fplt.make_mpf_style(marketcolors=mc)
my_dpi = 96
fplt.figure(figsize=(1800 / my_dpi, 400 / my_dpi), dpi=my_dpi)

fplt.plot(apple_df, type='candle', style=s,
        title='',
        ylabel='',
        ylabel_lower='',
        volume=True,
        mav=(3,6,9),
        savefig='test-mplfiance.png')