import plotly.offline as pyo
import plotly.graph_objects as go
import webbrowser

month = ['第一季度', '第二季度', '第三季度', '第四季度']
sales = [630, 880, 930, 1179]

fig = go.Figure(data=[go.Pie(labels=month, values=sales, textinfo='label+percent',
                             insidetextorientation='radial')])

fig.update_layout(
    title=dict(
        text="2019年季度销售业绩分析",
        x=0.47,
        y=0.95
    ),
    font=dict(
        family="Microsoft Yahei UI",
        size=20,
        color='black'
    ),
    xaxis_title="月份",
    xaxis_title_font_family='MS Sans Serif',
    xaxis_title_font_size=16,
    xaxis_title_font_color='red',
    yaxis_title="业绩数据",
    yaxis_title_font_family='MS Sans Serif',
    yaxis_title_font_size=16,
    yaxis_title_font_color='red'
)

pyo.plot(fig, filename='pie.html', auto_open=False)
webbrowser.open('pie.html')
#
# import plotly.offline as py
# import plotly.graph_objects as go
#
# month = ['第一季度', '第二季度', '第三季度', '第四季度']
# sales = [630, 880, 930, 1179]
#
# fig = go.Figure(data=[go.Pie(labels=month, values=sales, textinfo='label+percent',
#                              insidetextorientation='radial')])
#
# fig.update_layout(
#     title=dict(
#         text="2019年季度销售业绩分析",
#         x=0.47,
#         y=0.95
#     ),
#     font=dict(
#         family="Microsoft Yahei UI",
#         size=20,
#         color='black'
#     ),
#     xaxis_title="月份",
#     xaxis_title_font_family='MS Sans Serif',
#     xaxis_title_font_size=16,
#     xaxis_title_font_color='red',
#     yaxis_title="业绩数据",
#     yaxis_title_font_family='MS Sans Serif',
#     yaxis_title_font_size=16,
#     yaxis_title_font_color='red'
# )
#
# py.plot(fig, filename='pie.html')
