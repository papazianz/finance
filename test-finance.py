

import pandas_datareader as pd_dr
import matplotlib.pyplot as pyplot
from matplotlib import style
import datetime as dt

if __name__ == "__main__":
    style.use('ggplot')

    start_dt = dt.datetime(2000, 1, 1)
    end_dt = dt.datetime(2010, 1, 1)

    dataFrame = pd_dr.get_data_yahoo('MSFT', start = start_dt, end = end_dt)
    dataFrame.reset_index(inplace=True)
    dataFrame.set_index("Date", inplace=True)
    dataFrame.to_csv('MSFT')
    dataFrame[['Adj Close', 'High', 'Low']].plot()
    #dataFrame.plot()
    pyplot.show()


    