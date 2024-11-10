# import plotly.graph_objects as go
#
# y = ['第一季度', '第一季度', '第一季度', '第一季度', '第一季度', '第一季度',
#      '第二季度', '第二季度', '第二季度', '第二季度', '第二季度', '第二季度']
# fig = go.Figure()
# fig.add_trace(go.Box(
#     x=[23, 22, 26, 10, 15, 14, 22, 27, 19, 11, 15, 23],
#     y=y,
#     name='公司',
#     marker_color='#3D9970'
# ))
# fig.add_trace(go.Box(
#     x=[26, 27, 23, 16, 10, 15, 17, 19, 25, 18, 17, 22],
#     y=y,
#     name='消费者',
#     marker_color='#FF4136'
# ))
# fig.add_trace(go.Box(
#     x=[11, 23, 21, 19, 16, 26, 19, 20, 11, 16, 18, 25],
#     y=y,
#     name='小型企业',
#     marker_color='#FF851B'
# ))
#
# fig.update_traces(orientation='h')
#
# fig.update_layout(
#     boxmode='group',
#     legend_title="客户类型",
#     width=700, height=500,
#     title=dict(
#        text="2020年上半年不同客户的订单量分析",
#        x=0.5,
#        xanchor='center',
#        xref='paper'),
#     font=dict(
#         family="Courier New, monospace",
#         size=18,
#         color="RebeccaPurple"
#     ),
#     xaxis_title_font_family='Times New Roman',
#     yaxis_title_font_color='red'
# )
#
# py.plot(fig, filename='箱形图.html')
import plotly.graph_objects as go
import plotly.offline as pyo
import webbrowser

y = ['第一季度', '第一季度', '第一季度', '第一季度', '第一季度', '第一季度',
     '第二季度', '第二季度', '第二季度', '第二季度', '第二季度', '第二季度']

fig = go.Figure()
fig.add_trace(go.Box(
    x=[23, 22, 26, 10, 15, 14, 22, 27, 19, 11, 15, 23],
    y=y,
    name='公司',
    marker_color='#3D9970'
))
fig.add_trace(go.Box(
    x=[26, 27, 23, 16, 10, 15, 17, 19, 25, 18, 17, 22],
    y=y,
    name='消费者',
    marker_color='#FF4136'
))
fig.add_trace(go.Box(
    x=[11, 23, 21, 19, 16, 26, 19, 20, 11, 16, 18, 25],
    y=y,
    name='小型企业',
    marker_color='#FF851B'
))

fig.update_traces(orientation='h')

fig.update_layout(
    boxmode='group',
    legend_title="客户类型",
    width=700, height=500,
    title=dict(
        text="2020年上半年不同客户的订单量分析",
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

pyo.plot(fig, filename='箱形图.html', auto_open=False)
webbrowser.open('箱形图.html')
