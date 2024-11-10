from pyecharts import options as opts
from pyecharts.charts import ThemeRiver
from dbconn import conn
import webbrowser

sql_num = "SELECT order_date, ROUND(SUM(sales), 2), pay_method FROM orders WHERE order_date >= '2020-06-01' and order_date <= '2020-06-30' GROUP BY pay_method, order_date"
cursor = conn.cursor()
cursor.execute(sql_num)
sh = cursor.fetchall()
v1 = []
for s in sh:
    v1.append([s[0], s[1], s[2]])


def themeriver() -> ThemeRiver:
    c = (
        ThemeRiver()
        .add(
            ["支付宝", "微信", "信用卡", "其它"],
            v1,
            singleaxis_opts=opts.SingleAxisOpts(type_="time", pos_bottom="10%"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2020年6月份不同支付方式下的商品销售额", subtitle="2020年6月份企业运营分析"),
            toolbox_opts=opts.ToolboxOpts(is_show=True),
            legend_opts=opts.LegendOpts(is_show=True, pos_right='230')
        )
        .set_series_opts(label_opts=True)
    )
    return c


output_file = "themeriver_chart.html"
themeriver().load_javascript()
themeriver().render(output_file)

webbrowser.open(output_file)
