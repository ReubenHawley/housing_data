import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import matplotlib.dates as mdates
import time

style.use('ggplot')

# dataframe used for plotting
df = pd.read_csv('C:\\Users\\fit4l\\PycharmProjects\\AutoBot\\Auto-Trade-Crypto-Bot-master\\OHLCV\\1d mex history.csv'
                 , parse_dates=True, index_col=0)


def ohlc_graph_plot(indicator, save_graph: bool = True, graph_show: bool = True):
    #df.reset_index(inplace=True)
    #df['Timestamp'] = df['Timestamp'].map(mdates.date2num)
    #time_now = time.time()

    # graph layout and frame
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5)
    ax2 = plt.subplot2grid((6, 1), (5, 0), sharex=ax1)


    # plotting fib lines on the graph
    ax2.plot(df['Timestamp'], indicator)

    if fiblines:
        ax2.axhline(y=23.6, color='g', linestyle='-')
        ax2.axhline(y=38.2, color='g', linestyle='-')
        ax2.axhline(y=50, color='b', linestyle='-')
        ax2.axhline(y=61.8, color='r', linestyle='-')
        ax2.axhline(y=78.6, color='r', linestyle='-')

    # display/save data frame/graph
    if save_graph:
        plt.savefig('3min mex history{}.png'.format(time_now), dpi=320)
    if graph_show:
        plt.ylabel("Price")
        plt.xlabel("Time")
        plt.show()

ohlc_graph_plot(df)