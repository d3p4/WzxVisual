import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def import_csv(stock_code):
    df = pd.read_csv(stock_code + '.csv', infer_datetime_format=True)
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
gain_history = []
loss_history = []
avg_gain_values = []
avg_loss_values = []
rsi_values = []
last_price = 0

for close in df['Close']:
    if last_price == 0:
        last_price = close

    gain_history.append(max(0, close - last_price))
    loss_history.append(max(0, last_price - close))
    last_price = close

    if len(gain_history) > time_period:
        del (gain_history[0])
        del (loss_history[0])

    avg_gain = np.mean(gain_history)
    avg_loss = np.mean(loss_history)

    avg_gain_values.append(avg_gain)
    avg_loss_values.append(avg_loss)

    rs = 0
    if avg_loss > 0:
        rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))
    rsi_values.append(rsi)

df = df.assign(RSAvgGainOver20D=pd.Series(avg_gain_values, index=df.index))
df = df.assign(RSAvgLossOver20D=pd.Series(avg_loss_values, index=df.index))
df = df.assign(RSIOver20D=pd.Series(rsi_values, index=df.index))

fig = plt.figure(figsize=(10,7))
ax1 = fig.add_subplot(311, ylabel='close')
df['Close'].plot(ax=ax1, color='black', lw=1.5, legend=True)

plt.tick_params(labelsize=16)
plt.legend(loc='upper right', fontsize=16)
plt.ylabel('Close', size=16, rotation=90, verticalalignment='center')

ax2 = fig.add_subplot(312, ylabel='RS', sharex=ax1)
df['RSAvgGainOver20D'].plot(ax=ax2, color='g', lw=1.5, legend=True)
df['RSAvgLossOver20D'].plot(ax=ax2, color='r', lw=1.5, legend=True)
plt.tick_params(labelsize=16)
plt.legend(loc='upper left', fontsize=16)
plt.ylabel('RS', size=16, rotation=90, verticalalignment='center')

ax3 = fig.add_subplot(313, ylabel='RSI', sharex=ax1)
df['RSIOver20D'].plot(ax=ax3, color='b', lw=1.5, legend=True)
plt.xlabel('日期', size=16)
plt.ylabel('RSI', size=16, rotation=90, verticalalignment='center')
plt.tick_params(labelsize=16)
plt.legend(loc='upper right', fontsize=16)

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
#     df = pd.read_csv(stock_code + '.csv',infer_datetime_format=True)
#     df.rename(columns={
#         'trade_date': 'Date',
#         'open': 'Open',
#         'high': 'High',
#         'low': 'Low',
#         'close': 'Close',
#         'volume': 'Volume'
#     },inplace=True)
#     df.set_index(['Date'], inplace=True)
#     return df
#
# stock_code = 'D:/py_practice/python可视化/各章节数据源/ch04/stocks'
# #数据的规模
# scale = 300
# df = import_csv(stock_code)[-scale:]
#
# time_period = 20     #损益的回溯周期
# gain_history = []    #回溯期内的收益历史（无收益为0，有收益则为收益的幅度）
# loss_history = []    #回溯期内的损失历史（无损失为0，有损失则为损失的幅度）
# avg_gain_values = [] #存储平均收益值以便图形绘制
# avg_loss_values = [] #存储平均损失值以便图形绘制
# rsi_values = []      #存储算得的RSI值
# last_price = 0
# #当前价-过去价 > 0 表示收益(gain)
# #当前价-过去价 < 0 表示损失(loss)
#
# #遍历收盘价以计算RSI指标
# for close in df['Close']:
#     if last_price == 0:
#         last_price = close
#
#     gain_history.append(max(0, close - last_price))
#     loss_history.append(max(0, last_price - close))
#     last_price = close
#
#     if len(gain_history) > time_period:  #最大观测值等于回溯周期
#         del (gain_history[0])
#         del (loss_history[0])
#
#     avg_gain = np.mean(gain_history)  #回溯期的平均收益
#     avg_loss = np.mean(loss_history)  #回溯期的平均损失
#
#     avg_gain_values.append(avg_gain)
#     avg_loss_values.append(avg_loss)
#
#     #初始化rs值
#     rs = 0
#     if avg_loss > 0:     #避免除数出现0
#         rs = avg_gain / avg_loss
#
#     rsi = 100 - (100 / (1 + rs))
#     rsi_values.append(rsi)
#
# #将计算所得值并入DataFrame
# df = df.assign(RSAvgGainOver20D=pd.Series(avg_gain_values, index=df.index))
# df = df.assign(RSAvgLossOver20D=pd.Series(avg_loss_values, index=df.index))
# df = df.assign(RSIOver20D=pd.Series(rsi_values, index=df.index))
#
# #定义画布并添加子图
# fig = plt.figure(figsize=(10,7))
# ax1 = fig.add_subplot(311, ylabel='close')
# df['Close'].plot(ax=ax1, color='black', lw=1.5, legend=True)
#
# #设置刻度值的字体大小
# plt.tick_params(labelsize=16)
# plt.legend(loc='upper right',fontsize=16)
#
# #给y轴加上标签
# plt.ylabel('Close',size=16,rotation=90,verticalalignment='center')
#
# #设置同步缩放横轴，便于缩放查看
# ax2 = fig.add_subplot(312, ylabel='RS', sharex=ax1)
# df['RSAvgGainOver20D'].plot(ax=ax2, color='g', lw=1.5, legend=True)
# df['RSAvgLossOver20D'].plot(ax=ax2, color='r', lw=1.5, legend=True)
# plt.tick_params(labelsize=16)
# plt.legend(loc='upper left',fontsize=16)
# plt.ylabel('RS',size=16,rotation=90,verticalalignment='center')
#
# ax3 = fig.add_subplot(313, ylabel='RSI', sharex=ax1)
# df['RSIOver20D'].plot(ax=ax3, color='b', lw=1.5, legend=True)
# #给x轴加上标签
# plt.xlabel('日期',size=16)
# #给y轴加上标签
# plt.ylabel('RSI', size=16, rotation=90, verticalalignment='center')
# #设置刻度值的字体大小
# plt.tick_params(labelsize=16)
# #设置图例
# plt.legend(loc='upper right',fontsize=16)
#
# plt.show()

