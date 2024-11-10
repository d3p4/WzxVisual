from pyecharts.charts import Bar
from pyecharts import options as opts
import webbrowser

bar=(
    Bar()
    .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    .set_global_opts(title_opts=opts.TitleOpts(
        title="商家A和商家B 9月销售数量统计", title_textstyle_opts=opts.TextStyleOpts(font_size=20)),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=16)),
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=16)),
        toolbox_opts=opts.ToolboxOpts(),
        legend_opts=opts.LegendOpts(is_show=True, item_width=40,
                                    item_height=20, textstyle_opts=opts.TextStyleOpts(font_size=16)))
    .set_series_opts(label_opts=opts.LabelOpts(font_size=16))
)
bar.render('sales.html')
webbrowser.open('sales.html')

