import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def import_csv(stock_code):
    df = pd.read_csv(stock_code + '.csv')
    df.rename(columns={
        'trade_date': 'Date',
        'open': 'Open',
        'high': 'High',
        'low': 'Low',
        'close': 'Close',
        'volume': 'Volume'
    }, inplace=True)
    df.set_index(['Date'], inplace=True)
    return df


stock_code = 'D:/py_practice/python可视化/各章节数据源/ch04/stocks'
scale = 300
df = import_csv(stock_code)[-scale:]

time_period = 20
stdev_factor = 2
history = []
sma_values = []
upper_band = []
lower_band = []

for close_price in df['Close']:
    history.append(close_price)
    if len(history) > time_period:
        del (history[0])

    sma = np.mean(history)
    sma_values.append(sma)
    stdev = np.sqrt(np.sum((history - sma) ** 2) / len(history))
    upper_band.append(sma + stdev_factor * stdev)
    lower_band.append(sma - stdev_factor * stdev)

df = df.assign(收盘价=pd.Series(df['Close'], index=df.index))
df = df.assign(中界线=pd.Series(sma_values, index=df.index))
df = df.assign(阻力线=pd.Series(upper_band, index=df.index))
df = df.assign(支撑线=pd.Series(lower_band, index=df.index))

plt.figure(figsize=(10, 6))
plt.ylabel(f'{stock_code} price in ￥')

df['收盘价'].plot(color='k', lw=1., legend=True)
df['中界线'].plot(color='b', lw=1., legend=True)
df['阻力线'].plot(color='r', lw=1., legend=True)
df['支撑线'].plot(color='g', lw=1., legend=True)

plt.xlabel('日期', size=16)
plt.tick_params(labelsize=16)
plt.legend(loc='upper right', fontsize=16)

plt.title('股票价格BOLL图', fontsize=20)
plt.show()
# 原有代码如下
# import pandas as pd
# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# #设置图像标签显示中文
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# #导入数据
# def import_csv(stock_code):
#     df = pd.read_csv(stock_code + '.csv')
#     df.rename(columns={
#         'trade_date': 'Date',
#         'open': 'Open',
#         'high': 'High',
#         'low': 'Low',
#         'close': 'Close',
#         'volume': 'Volume'
#     },
#               inplace=True)
#     df.set_index(['Date'], inplace=True)
#     return df
#
# stock_code = 'D:/desktop/数据可视化/各章节数据源\ch04\stocks'
# #数据的规模
# scale = 300
# df = import_csv(stock_code)[-scale:]
#
# #SMA:简单移动平均
# time_period = 20  #SMA的计算周期，默认为20
# stdev_factor = 2  #上下频带的标准偏差比例因子
# history = []      #每个计算周期所需的价格数据
# sma_values = []   #初始化SMA值
# upper_band = []   #初始化阻力线价格
# lower_band = []   #初始化支撑线价格
#
# #构造列表形式的绘图数据
# for close_price in df['Close']:
#     history.append(close_price)
#     #计算移动平均时先确保时间周期不大于20
#     if len(history) > time_period:
#         del (history[0])
#
#     #将计算的SMA值存入列表
#     sma = np.mean(history)
#     sma_values.append(sma)
#     #计算标准差
#     stdev = np.sqrt(np.sum((history - sma) ** 2) / len(history))
#     upper_band.append(sma + stdev_factor * stdev)
#     lower_band.append(sma - stdev_factor * stdev)
#
# #将计算结果合并到DataFrame
# df = df.assign(收盘价=pd.Series(df['Close'], index=df.index))
# df = df.assign(中界线=pd.Series(sma_values, index=df.index))
# df = df.assign(阻力线=pd.Series(upper_band, index=df.index))
# df = df.assign(支撑线=pd.Series(lower_band, index=df.index))
#
# #绘制图形
# ax = plt.figure(figsize=(10,6))
# #设置y轴标签
# ax.ylabel = '%s price in ￥' % (stock_code)
#
# df['收盘价'].plot(color='k', lw=1., legend=True)
# df['中界线'].plot(color='b', lw=1., legend=True)
# df['阻力线'].plot(color='r', lw=1., legend=True)
# df['支撑线'].plot(color='g', lw=1., legend=True)
#
# #设置x轴标签
# plt.xlabel('日期',size=16)
# #设置刻度值的字体大小
# plt.tick_params(labelsize=16)
# #设置图例
# plt.legend(loc='upper right',fontsize=16)
#
# plt.title('股票价格BOLL图',fontsize=20)
# plt.show()
#
