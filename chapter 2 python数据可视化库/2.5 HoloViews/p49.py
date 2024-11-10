# import holoviews as hv
# from holoviews import dim, opts
# hv.extension('bokeh', 'matplotlib')
#
# #读取数据
# household = [19.27,18.62,18.97,21.08,21.73,20.57,21.64,17.58,19.42,21.39,19.53,18.63]
#
# #绘制图形
# curve = hv.Curve(household, ('x', 'x'), ('y', '家庭用品')).opts(fontsize={'title':20,'labels':16,'xticks':13,'yticks':13})
# (curve.relabel('没有坐标轴').opts(width=300, height=400,xaxis=None, yaxis=None) +
#  curve.relabel('没有X坐标轴').opts(width=300, height=400,xaxis='bare') +
#  curve.relabel('移动Y坐标轴').opts(width=300, height=400,xaxis='bottom', yaxis='right'))
import holoviews as hv
from holoviews import opts
import webbrowser

hv.extension('bokeh')

household = [19.27, 18.62, 18.97, 21.08, 21.73, 20.57, 21.64, 17.58, 19.42, 21.39, 19.53, 18.63]

curve = hv.Curve(household, ('x', 'x'), ('y', '家庭用品')).opts(fontsize={'title': 20, 'labels': 16, 'xticks': 13, 'yticks': 13})

combined = (
    curve.relabel('没有坐标轴').opts(width=300, height=400, xaxis=None, yaxis=None) +
    curve.relabel('没有X坐标轴').opts(width=300, height=400, xaxis='bare') +
    curve.relabel('移动Y坐标轴').opts(width=300, height=400, xaxis='bottom', yaxis='right')
)

hv.save(combined, 'household_curves_axes.html')
webbrowser.open('household_curves_axes.html')
