import plotly.offline as py
import plotly.graph_objs as go
import webbrowser

trace1 = go.Bar(x=['4月份', '5月份', '6月份'], y=[25, 13, 19], name='企业')
trace2 = go.Bar(x=['4月份', '5月份', '6月份'], y=[21, 13, 16], name='公司')
trace3 = go.Bar(x=['4月份', '5月份', '6月份'], y=[12, 24, 16], name='消费者')
data = [trace1, trace2, trace3]
layout = go.Layout(barmode='group')
fig = go.Figure(data=data, layout=layout)

fig.update_layout(
    xaxis_title="月份",
    yaxis_title="销售额",
    legend_title="客户类型",
    width=700, height=500,
    title=dict(
       text="2020年第二季度企业销售业绩分析",
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

py.plot(fig, filename='条形图.html')
webbrowser.open('条形图.html')
