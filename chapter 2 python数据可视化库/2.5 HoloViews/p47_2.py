# import holoviews as hv
# from holoviews import dim, opts
# hv.extension('bokeh', 'matplotlib')
#
# #读取数据
# household = [19.27,18.62,18.97,21.08,21.73,20.57,21.64,17.58,19.42,21.39,19.53,18.63]
#
# #绘制图形
# hv.Curve(household).opts(width=400, height=400,bgcolor='lightgray',title="图形背景").opts(fontsize={'title':20,'labels':16,'xticks':13,'yticks':13})
import holoviews as hv
from holoviews import opts
import webbrowser

hv.extension('bokeh')

household = [19.27, 18.62, 18.97, 21.08, 21.73, 20.57, 21.64, 17.58, 19.42, 21.39, 19.53, 18.63]

curve = hv.Curve(household).opts(width=400, height=400, bgcolor='lightgray', title="图形背景",
                                 fontsize={'title': 20, 'labels': 16, 'xticks': 13, 'yticks': 13})

hv.save(curve, 'household_curve_background.html')
webbrowser.open('household_curve_background.html')
