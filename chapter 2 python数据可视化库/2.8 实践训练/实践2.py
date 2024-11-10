# from pyecharts.globals import CurrentConfig, NotebookType
# CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
# 
# from pyecharts.charts import Bar
# from pyecharts import options as opts
# 
# bar = (
#     Bar()
#     .add_xaxis(['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'])
#     .add_yaxis("订单量", [200, 197, 233, 216, 345, 319, 197, 357, 376, 416, 355, 408])
#     .set_global_opts(title_opts=opts.TitleOpts(title="2019年12个月商品的订单量",
#                                                title_textstyle_opts=opts.TextStyleOpts(font_size=20)),
#                      xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=16)),
#                      yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=16)),
#                      toolbox_opts=opts.ToolboxOpts(),
#                      legend_opts=opts.LegendOpts(is_show=True, item_width=40, item_height=20,
#                                                  textstyle_opts=opts.TextStyleOpts(font_size=16)))
#     .set_series_opts(label_opts=opts.LabelOpts(font_size=16))
# )
# 
# bar.load_javascript()
# bar.render_notebook()

from pyecharts.globals import CurrentConfig
from pyecharts.charts import Bar
from pyecharts import options as opts
import webbrowser

bar = (
    Bar()
    .add_xaxis(['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'])
    .add_yaxis("订单量", [200, 197, 233, 216, 345, 319, 197, 357, 376, 416, 355, 408])
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2019年12个月商品的订单量",
                                  title_textstyle_opts=opts.TextStyleOpts(font_size=20)),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=16)),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=16)),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=True, item_width=40, item_height=20,
                                    textstyle_opts=opts.TextStyleOpts(font_size=16))
    )
    .set_series_opts(label_opts=opts.LabelOpts(font_size=16))
)

bar.render('订单量柱状图.html')
webbrowser.open('订单量柱状图.html')
