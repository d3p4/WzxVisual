# import plotly.graph_objects as go
#
# store = ['定远店','东海店','海恒店','金寨店','燎原店','临泉店','庐江店','明耀店','众兴店']
# consumer = [30,22,20,28,16,30,24,18,12]
#
# fig = go.Figure(data=[go.Pie(labels=store, values=consumer, textinfo='label+percent',insidetextorientation='radial')])

# fig.update_layout(
#     legend_title="客户类型",
#     width=700,height=500,
#     title = dict(
#        text = "2020年第二季度各门店销售业绩分析",
#        x = 0.5,
#        xanchor = 'center',
#        xref = 'paper'
#     ),
#     font=dict(
#         family="Courier New, monospace",
#         size=18,
#         color="RebeccaPurple"
#     )
# )

# py.plot(fig, filename='饼图.html')
import plotly.graph_objects as go
import plotly.offline as pyo
import webbrowser

store = ['定远店', '东海店', '海恒店', '金寨店', '燎原店', '临泉店', '庐江店', '明耀店', '众兴店']
consumer = [30, 22, 20, 28, 16, 30, 24, 18, 12]

fig = go.Figure(data=[go.Pie(labels=store, values=consumer, textinfo='label+percent', insidetextorientation='radial')])

fig.update_layout(
    legend_title="客户类型",
    width=700, height=500,
    title=dict(
        text="2020年第二季度各门店销售业绩分析",
        x=0.5,
        xanchor='center',
        xref='paper'
    ),
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    )
)

pyo.plot(fig, filename='饼图.html')
webbrowser.open('饼图.html')
