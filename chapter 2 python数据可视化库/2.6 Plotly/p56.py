# import plotly.express as px
# import pandas as pd
# df = pd.read_csv('D:/Python数据可视化分析与案例实战/ch02/stocks.csv')
#
# fig = px.line(df, x='Date', y='Close', range_x=['2015/1/1', '2019/12/31'])
#
# fig.update_layout(
#     xaxis_title="日期",
#     yaxis_title="收盘价",
#     width=700, height=400,
#     title=dict(
#        text="近5年企业股票收盘价走势",
#        x=0.5,
#        xanchor = 'center',
#        xref = 'paper'
#     ),
#     font=dict(
#         family="Courier New, monospace",
#         size=18,
#         color="RebeccaPurple"
#     ),
#     xaxis_title_font_family='Times New Roman',
#     yaxis_title_font_color='red'
# )
#
# py.plot(fig, filename='时间序列图.html')

import plotly.express as px
import pandas as pd
import plotly.offline as pyo
import webbrowser

df = pd.read_csv('D:/py_practice/python可视化/各章节数据源/ch02/stocks.csv')

fig = px.line(df, x='Date', y='Close', range_x=['2015/1/1', '2019/12/31'])

fig.update_layout(
    xaxis_title="日期",
    yaxis_title="收盘价",
    width=700, height=400,
    title=dict(
        text="近5年企业股票收盘价走势",
        x=0.5,
        xanchor='center',
        xref='paper'
    ),
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    ),
    xaxis_title_font_family='Times New Roman',
    yaxis_title_font_color='red'
)

pyo.plot(fig, filename='时间序列图.html')
webbrowser.open('时间序列图.html')
