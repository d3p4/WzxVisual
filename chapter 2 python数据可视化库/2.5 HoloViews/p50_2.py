# import holoviews as hv
# from holoviews import dim, opts
# hv.extension('bokeh', 'matplotlib')
#
# #读取数据
# household = [19.27,18.62,18.97,21.08,21.73,20.57,21.64,17.58,19.42,21.39,19.53,18.63]
#
# #绘制图形
# curve = hv.Curve(household, ('x', 'x'), ('y', '家庭用品')).opts(fontsize={'title':20,'labels':16,'xticks':13,'yticks':13})
# (curve.relabel('普通刻度线').opts(xticks=5,width=300, height=400) +
#  curve.relabel('刻度线列表').opts(xticks=[0, 5, 9],width=300, height=400) +
#  curve.relabel("刻度线标签").opts(xticks=[(0, 'zero'), (5, '江苏'), (9, '重庆')],width=300, height=400))
import holoviews as hv
from holoviews import opts
import webbrowser

hv.extension('bokeh')

household = [19.27, 18.62, 18.97, 21.08, 21.73, 20.57, 21.64, 17.58, 19.42, 21.39, 19.53, 18.63]

curve = hv.Curve(household, ('x', 'x'), ('y', '家庭用品')).opts(
    fontsize={'title': 20, 'labels': 16, 'xticks': 13, 'yticks': 13}
)

combined = (
    curve.relabel('普通刻度线').opts(xticks=5, width=300, height=400) +
    curve.relabel('刻度线列表').opts(xticks=[0, 5, 9], width=300, height=400) +
    curve.relabel("刻度线标签").opts(xticks=[(0, 'zero'), (5, '江苏'), (9, '重庆')], width=300, height=400)
)

hv.save(combined, 'household_curve_ticks.html')
webbrowser.open('household_curve_ticks.html')
