from pyecharts import options as opts
from pyecharts.charts import Scatter, Page
from pyecharts.globals import SymbolType
import pymysql
import webbrowser

conn = pymysql.connect(host='127.0.0.1', port=3306, user='sales',
                       password='123456', db='sales', charset='utf8')
cursor = conn.cursor()
sql_num = "SELECT trade_date,open,close FROM stocks where trade_date>='2020-01-01'order by trade_date asc"
cursor.execute(sql_num)
sh = cursor.fetchall()
v1 = []
v2 = []
v3 = []
for s in sh:
    v1.append(s[0])
    v2.append(float(s[1]))
    v3.append(float(s[2]))  # 这里一些python版本会出现以int型读取数据的情况，造成数据只显示第一位的异常，这里加个float保证正常读取


def scatter_splitline() -> Scatter:
    c = (
        Scatter()
        .add_xaxis(v1)
        .add_yaxis("开盘价", v2, label_opts=opts.LabelOpts(is_show=False))
        .add_yaxis("收盘价", v3, label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="企业股票趋势分析", subtitle="股票开盘价和收盘价"),
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            yaxis_opts=opts.AxisOpts(type_="value", min_=60, axistick_opts=opts.AxisTickOpts(is_show=True),
                                     splitline_opts=opts.SplitLineOpts(is_show=True)),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(is_show=True)
        )
    )
    return c


scatter_chart = scatter_splitline()
scatter_chart.render('股票趋势分析.html')

webbrowser.open('股票趋势分析.html')
