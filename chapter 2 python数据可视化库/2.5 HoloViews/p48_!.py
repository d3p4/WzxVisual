# import holoviews as hv
# from holoviews import dim, opts
# hv.extension('bokeh', 'matplotlib')
#
# #读取数据
# household = [19.27,18.62,18.97,21.08,21.73,20.57,21.64,17.58,19.42,21.39,19.53,18.63]
# office =    [29.46,21.16,11.46,19.47,22.79,17.01,11.61,24.59,13.91,13.18,21.16,20.33]
#
# #绘制图形
# (hv.Curve(household, label='家庭用品')*hv.Curve(office, label='办公用品')).opts(fontscale=1.2, width=400, height=400, title='字体缩放',fontsize={'title':20,'labels':16,'xticks':13,'yticks':13})
import holoviews as hv
from holoviews import opts
import webbrowser

hv.extension('bokeh')

household = [19.27, 18.62, 18.97, 21.08, 21.73, 20.57, 21.64, 17.58, 19.42, 21.39, 19.53, 18.63]
office = [29.46, 21.16, 11.46, 19.47, 22.79, 17.01, 11.61, 24.59, 13.91, 13.18, 21.16, 20.33]

curve = (hv.Curve(household, label='家庭用品') * hv.Curve(office, label='办公用品')).opts(
    fontscale=1.2, width=400, height=400, title='字体缩放',
    fontsize={'title': 20, 'labels': 16, 'xticks': 13, 'yticks': 13}
)

hv.save(curve, 'household_office_curves.html')
webbrowser.open('household_office_curves.html')
