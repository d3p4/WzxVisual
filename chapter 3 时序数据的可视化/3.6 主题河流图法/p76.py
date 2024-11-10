from pyecharts import options as opts
from pyecharts.charts import ThemeRiver
import pymysql
import webbrowser

# 数据库连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='sales',
                       password='123456', db='sales', charset='utf8')

sql_num = "SELECT order_date, ROUND(SUM(profit), 2), category FROM orders WHERE order_date >= '2020-06-01' AND order_date <= '2020-06-30' GROUP BY category, order_date"
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
                ["办公用品", "家具", "技术"],
                v1,
                singleaxis_opts=opts.SingleAxisOpts(type_="time", pos_bottom="10%"),
            )
            .set_global_opts(
                title_opts=opts.TitleOpts(title="不同类型商品的销售额分析", subtitle="2020年6月份企业运营分析"),
                toolbox_opts=opts.ToolboxOpts(),
                legend_opts=opts.LegendOpts(is_show=True)
            )
            .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    )
    return c


theme_river_chart = themeriver()
theme_river_chart.render('themeriver_chart.html')
webbrowser.open('themeriver_chart.html')
