import pandas as pd
import mplfinance as mpf


daily = pd.read_excel('D:/py_practice/python可视化/各章节数据源/ch04/stocks.xls',
                      index_col=0, parse_dates=True)
daily.index.name = 'date'

mpf.plot(daily, type='renko')

