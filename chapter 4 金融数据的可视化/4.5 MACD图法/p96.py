from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


def import_csv(stock_code):
    df = pd.read_csv(stock_code + '.csv')
    df.rename(columns={
        'trade_date': 'Date',
        'open': 'Open',
        'high': 'High',
        'low': 'Low',
        'close': 'Close',
        'volume': 'Volume'},
        inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])  # 将日期列转换为datetime类型
    df.set_index(['Date'], inplace=True)
    return df


stock_code = 'D:/py_practice/python可视化/各章节数据源/ch04/stocks'
scale = 100
df = import_csv(stock_code)[-scale:]


num_periods_fast = 10
K_fast = 2 / (num_periods_fast + 1)
ema_fast = 0
num_periods_slow = 40
K_slow = 2 / (num_periods_slow + 1)
ema_slow = 0
num_periods_macd = 20
K_macd = 2 / (num_periods_macd + 1)
ema_macd = 0

ema_fast_values = []
ema_slow_values = []
macd_values = []
macd_signal_values = []
MACD_hist_values = []
for close_price in df['Close']:
    if ema_fast == 0:
        ema_fast = close_price
        ema_slow = close_price
    else:
        ema_fast = (close_price - ema_fast) * K_fast + ema_fast
        ema_slow = (close_price - ema_slow) * K_slow + ema_slow

    ema_fast_values.append(ema_fast)
    ema_slow_values.append(ema_slow)

    macd = ema_fast - ema_slow  
    if ema_macd == 0:
        ema_macd = macd
    else:
        ema_macd = (macd - ema_macd) * K_macd + ema_macd  
    macd_values.append(macd)
    macd_signal_values.append(ema_macd)
    MACD_hist_values.append(macd - ema_macd)

df = df.assign(ClosePrice=pd.Series(df['Close'], index=df.index))
df = df.assign(FastEMA10d=pd.Series(ema_fast_values, index=df.index))
df = df.assign(SlowEMA40d=pd.Series(ema_slow_values, index=df.index))
df = df.assign(MACD=pd.Series(macd_values, index=df.index))
df = df.assign(EMA_MACD20d=pd.Series(macd_signal_values, index=df.index))
df = df.assign(MACD_hist=pd.Series(MACD_hist_values, index=df.index))

close_price = df['ClosePrice']
ema_f = df['FastEMA10d']
ema_s = df['SlowEMA40d']
macd = df['MACD']
ema_macd = df['EMA_MACD20d']
macd_hist = df['MACD_hist']


fig, ax = plt.subplots(3, 1, figsize=(12, 10))  # 加了个figsize


plt.rcParams['font.sans-serif'] = ['SimHei']  
plt.rcParams['axes.unicode_minus'] = False
plt.subplots_adjust(hspace=.3)  #三个图间距从1改成3，防止重叠


ax[0].set_ylabel('Close')
ax[0].set_title('股票价格MACD图')
ax[0].plot(df.index, close_price, color='g', lw=1., label='Close')
ax[0].plot(df.index, ema_f, color='b', lw=1., label='FastEMA10d')
ax[0].plot(df.index, ema_s, color='r', lw=1., label='SlowEMA40d')
ax[0].legend()
ax[1].plot(df.index, macd, color='k', lw=1., label='MACD')
ax[1].plot(df.index, ema_macd, color='g', lw=1., label='EMA_MACD20d')
ax[1].legend()
ax[2].bar(df.index, macd_hist, color='r', label='MACD_hist')
ax[2].legend()
ax[2].set_xlabel('日期', size=16)


for a in ax:
    a.tick_params(axis='both', which='major', labelsize=10)

interval = scale // 25  # 比手动设置4个间隔更便捷
for a in ax:
    a.set_xticks(df.index[::interval])
    a.set_xticklabels([d.strftime('%Y-%m-%d') for d in df.index[::interval]], rotation=45)

plt.tight_layout()
#  添加了自动布局调整，确保所有元素（包括标签）都能在图表中正确显示
plt.show()
# pylab是一个比较旧的接口，现在只在jupyter支持，所以移除了 pylab 的导入，直接使用 matplotlib.pyplot。
# 在 import_csv 函数中，将日期列转换为 datetime 类型。
# 改变了 x 轴刻度的设置方式。意义：新的方法更加通用和简洁
# 直接使用 DataFrame 的索引来设置刻度，避免了复杂的日期范围计算
# 旧方法需要单独处理x轴，新方法在一个循环中处理所有子图的x轴，更加通用
# 旧方法就像是我们自己创建了一个日历，然后试图将日记内容对应到这个日历上。
# 新方法则是直接使用日记本身的日期，每隔几页翻一下，在那里做个标记。
# 原代码如下，以作对比
# from datetime import datetime
# import pylab as pl
# import pandas as pd
# import matplotlib.pyplot as plt
# import matplotlib as mpl
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
#         'volume': 'Volume'},
#         inplace=True)
#     df.set_index(['Date'], inplace=True)
#     return df
#
# stock_code = 'D:\Python数据可视化分析与案例实战\ch04\stocks'
# #数据的规模
# scale = 100
# df = import_csv(stock_code)[-scale:]
#
# #指数移动平均线
# num_periods_fast = 10  # 快速EMA的时间周期
# #K:平滑常数，取2/(n+1)
# K_fast = 2 / (num_periods_fast + 1)  #快速EMA平滑常数
# ema_fast = 0
# num_periods_slow = 40    #慢速EMA的时间周期
# K_slow = 2 / (num_periods_slow + 1)  #慢速EMA平滑常数
# ema_slow = 0
# num_periods_macd = 20   #MACD EMA的时间周期
# K_macd = 2 / (num_periods_macd + 1)  #MACD EMA平滑常数
# ema_macd = 0
#
# ema_fast_values = []
# ema_slow_values = []
# macd_values = []
# macd_signal_values = []
# MACD_hist_values = []
# for close_price in df['Close']:
#     if ema_fast == 0:
#         ema_fast = close_price
#         ema_slow = close_price
#     else:
#         ema_fast = (close_price - ema_fast) * K_fast + ema_fast
#         ema_slow = (close_price - ema_slow) * K_slow + ema_slow
#
#     ema_fast_values.append(ema_fast)
#     ema_slow_values.append(ema_slow)
#
#     macd = ema_fast - ema_slow
#     if ema_macd == 0:
#         ema_macd = macd
#     else:
#         ema_macd = (macd - ema_macd) * K_macd + ema_macd
#     macd_values.append(macd)
#     macd_signal_values.append(ema_macd)
#     MACD_hist_values.append(macd - ema_macd)
#
# df = df.assign(ClosePrice=pd.Series(df['Close'], index=df.index))
# df = df.assign(FastEMA10d=pd.Series(ema_fast_values, index=df.index))
# df = df.assign(SlowEMA40d=pd.Series(ema_slow_values, index=df.index))
# df = df.assign(MACD=pd.Series(macd_values, index=df.index))
# df = df.assign(EMA_MACD20d=pd.Series(macd_signal_values, index=df.index))
# df = df.assign(MACD_hist=pd.Series(MACD_hist_values, index=df.index))
#
# close_price = df['ClosePrice']
# ema_f = df['FastEMA10d']
# ema_s = df['SlowEMA40d']
# macd = df['MACD']
# ema_macd = df['EMA_MACD20d']
# macd_hist = df['MACD_hist']
#
# #设置画布，纵向排列的三个子图
# fig, ax = plt.subplots(3, 1)
#
# # 设置标签显示中文
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# #调整子图的间距，hspace表示高(height)方向的间距
# plt.subplots_adjust(hspace=.1)
#
# #设置第一子图的y轴信息及标题
# ax[0].set_ylabel('Close')
# ax[0].set_title('股票价格MACD图')
# close_price.plot(ax=ax[0], color='g', lw=1., legend=True, use_index=False)
# ema_f.plot(ax=ax[0], color='b', lw=1., legend=True, use_index=False)
# ema_s.plot(ax=ax[0], color='r', lw=1., legend=True, use_index=False)
#
# #应用同步缩放
# ax[1] = plt.subplot(312, sharex=ax[0])
# macd.plot(ax=ax[1], color='k', lw=1., legend=True, sharex=ax[0], use_index=False)
# ema_macd.plot(ax=ax[1], color='g', lw=1., legend=True, use_index=False)
#
# #应用同步缩放
# ax[2] = plt.subplot(313, sharex=ax[0])
# df['MACD_hist'].plot(ax=ax[2], color='r', kind='bar', legend=True, sharex=ax[0])
#
# #给x轴加上标签
# plt.xlabel('日期',size=16)
# #设置刻度值的字体大小
# plt.tick_params(labelsize=13)
#
# #设置坐标间隔
# interval = scale // 25
# pl.xticks([i for i in range(1,scale,4)],
#           [datetime.strftime(i, format='%Y-%m-%d') for i in \
#            pd.date_range(df.index[0], df.index[-1],freq='%dd' % (interval))],rotation=45)
#
# plt.show()