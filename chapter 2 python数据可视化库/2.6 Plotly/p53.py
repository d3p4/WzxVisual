# import numpy as np
# import plotly.offline as py
# import plotly.graph_objs as go
#
# store = ['定远店', '东海店', '海恒店', '金寨店', '燎原店', '临泉店', '庐江店', '明耀店', '众兴店']
# sales = [12, 13, 14, 16, 18, 19, 21, 24, 25]
# profit = [2.6, 2.1, 3.1, 2.2, 2.4, 2.5, 2.1, 2.9, 3.5]
#
# colors = np.random.rand(len(store))
# fig = go.Figure()
# fig.add_scatter(x=sales, y=profit, mode='markers',
#                 marker={'size': sales, 'color': colors, 'opacity': 0.9,
#                         'colorscale': 'Viridis', 'showscale': True})
#
# fig.update_layout(
#     xaxis_title="销售额",
#     yaxis_title="利润额",
#     width=700, height=500,
#     title=dict(
#        text="2020年第二季度各门店销售额与利润额分析",
#        x=0.5,
#        xanchor='center',
#        xref='paper'
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
# py.plot(fig, filename='散点图.html')
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go
import webbrowser

store = ['定远店', '东海店', '海恒店', '金寨店', '燎原店', '临泉店', '庐江店', '明耀店', '众兴店']
sales = [12, 13, 14, 16, 18, 19, 21, 24, 25]
profit = [2.6, 2.1, 3.1, 2.2, 2.4, 2.5, 2.1, 2.9, 3.5]

colors = np.random.rand(len(store))
fig = go.Figure()
fig.add_scatter(x=sales, y=profit, mode='markers',
                marker={'size': sales, 'color': colors, 'opacity': 0.9,
                        'colorscale': 'Viridis', 'showscale': True})

fig.update_layout(
    xaxis_title="销售额",
    yaxis_title="利润额",
    width=700, height=500,
    title=dict(
        text="2020年第二季度各门店销售额与利润额分析",
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

pyo.plot(fig, filename='散点图.html')
webbrowser.open('散点图.html')
