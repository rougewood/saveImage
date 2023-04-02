import matplotlib
import matplotlib.pyplot as plt
import numpy
import pandas as pd
import pandas_datareader as web
import plotly.graph_objects as go

def savePng():
    plt.plot([0,1,2,3,4],[0,3,5,9,11])
    plt.xlabel('Months')
    plt.ylabel('Books Read')

    plt.show()
    plt.savefig('books_read.png', transparent=False, pad_inches=0.2, edgecolor='red')

def saveWHPng():
    w = 800
    h = 400

    im_np = numpy.random.rand(h, w)
    my_dpi = 96
    plt.figure(figsize=(800 / my_dpi, 800 / my_dpi), dpi=my_dpi)
    fig = plt.figure(frameon=False)
    fig.set_size_inches(w, h)
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    ax.imshow(im_np, aspect='equal')
    fig.savefig('figure.png', dpi=1)

def saveStockChart():
    stock = 'MSFT'

    df = web.DataReader(stock, data_source='yahoo', start='01-01-2019')

    df['Close'].plot()

    plt.figure(figsize=(10, 10))
    plt.plot(df.index, df['Close'])
    plt.xlabel("date")
    plt.ylabel("$ price")
    plt.title("DIS Stock Price 1/1/17 - 8/1/19")

    plt.show()
