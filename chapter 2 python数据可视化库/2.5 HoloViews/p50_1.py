# import holoviews as hv
# from holoviews import dim, opts
# hv.extension('bokeh', 'matplotlib')
#
# #绘制图形
# bars = hv.Bars([('消费者', 181.56), ('小型企业', 146.81), ('公司', 103.96)], '客户类型').opts(fontsize={'title':20,'labels':16,'xticks':13,'yticks':13})
#
# (bars.relabel('反转X、Y轴').opts(invert_axes=True, width=300, height=400) +
#  bars.relabel('反转X轴').opts(invert_xaxis=True, width=300, height=400) +
#  bars.relabel('反转Y轴').opts(invert_yaxis=True, width=300, height=400)).opts(shared_axes=False)
import holoviews as hv
from holoviews import opts
import webbrowser

hv.extension('bokeh')

bars = hv.Bars([('消费者', 181.56), ('小型企业', 146.81), ('公司', 103.96)], '客户类型').opts(
    fontsize={'title': 20, 'labels': 16, 'xticks': 13, 'yticks': 13}
)

combined = (
    bars.relabel('反转X、Y轴').opts(invert_axes=True, width=300, height=400) +
    bars.relabel('反转X轴').opts(invert_xaxis=True, width=300, height=400) +
    bars.relabel('反转Y轴').opts(invert_yaxis=True, width=300, height=400)
).opts(shared_axes=False)

hv.save(combined, 'bars_inverted_axes.html')
webbrowser.open('bars_inverted_axes.html')
