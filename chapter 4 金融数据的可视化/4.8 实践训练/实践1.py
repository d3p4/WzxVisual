import pandas as pd
import mplfinance as mpf


daily = pd.read_excel(r'D:\py_practice\python可视化\各章节数据源\ch04\中国平安.xls', index_col=0, parse_dates=True)
daily.index.name = 'date'


mpf.plot(daily, type='candle')   #有'ohlc', 'candle', 'line', 'renko', 'pnf'等类型