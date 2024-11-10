from pyecharts import options as opts
from pyecharts.charts import Kline
import pymysql
import webbrowser

v1 = []
v2 = []
conn = pymysql.connect(host='127.0.0.1', port=3306, user='sales',
                       password='123456', db='sales', charset='utf8')
cursor = conn.cursor()

sql_num = "SELECT trade_date, open, high, low, close FROM stocks WHERE YEAR(trade_date)=2020 AND MONTH(trade_date)=6 ORDER BY trade_date ASC"
cursor.execute(sql_num)
sh = cursor.fetchall()
for s in sh:
    v1.append([s[0]])
for s in sh:
    v2.append([s[1], s[2], s[3], s[4]])
data = v2


def kline_markline() -> Kline:
    c = (
        Kline()
        .add_xaxis(v1)
        .add_yaxis(
            "企业股票收盘价",
            data,
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="max", value_dim="close")]
            ),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(is_scale=True, axislabel_opts=opts.LabelOpts(font_size=16)),
            yaxis_opts=opts.AxisOpts(
                is_scale=True,
                axislabel_opts=opts.LabelOpts(font_size=16),
                splitarea_opts=opts.SplitAreaOpts(
                    is_show=True, areastyle_opts=opts.AreaStyleOpts(opacity=1)
                ),
            ),
            datazoom_opts=[opts.DataZoomOpts(pos_bottom="-2%")],
            title_opts=opts.TitleOpts(title="2020年6月份企业股票价格走势",
                                      title_textstyle_opts=opts.TextStyleOpts(font_size=20)),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(is_show=True, item_width=40, item_height=20,
                                        textstyle_opts=opts.TextStyleOpts(font_size=16))
        )
        .set_series_opts(label_opts=opts.LabelOpts(font_size=16))
    )
    return c


kline_chart = kline_markline()
kline_chart.render('kline_chart.html')
webbrowser.open('kline_chart.html')

cursor.close()
conn.close()
