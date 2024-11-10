from pyecharts import options as opts
from pyecharts.charts import Scatter
import webbrowser
from dbconn import conn

cur = conn.cursor()
sql_num = "SELECT trade_date, amount FROM stocks WHERE trade_date >= '2020-01-01' ORDER BY trade_date ASC"
cur.execute(sql_num)
sh = cur.fetchall()
v1 = []
v2 = []
for s in sh:
    v1.append(s[0])
    v2.append(s[1])


def scatter_splitline() -> Scatter:
    c = (
        Scatter()
        .add_xaxis(v1)
        .add_yaxis("成交金额", v2, label_opts=opts.LabelOpts(is_show=False))
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2020年企业股票成交金额分析", subtitle="成交金额（万元）"),
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True)),
            yaxis_opts=opts.AxisOpts(type_="value", max_=60000, axistick_opts=opts.AxisTickOpts(is_show=True), splitline_opts=opts.SplitLineOpts(is_show=True)),
            toolbox_opts=opts.ToolboxOpts(),
        )
    )
    return c


output_file = "scatter_chart.html"
scatter_splitline().load_javascript()
scatter_splitline().render(output_file)

webbrowser.open(output_file)
