from pyecharts import options as opts
from pyecharts.charts import ThemeRiver
from dbconn import conn
import webbrowser

sql_num = "SELECT date, count, category FROM problems"
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
            ["产品质量", "服务态度", "售后服务"],
            v1,
            singleaxis_opts=opts.SingleAxisOpts(type_="time", pos_bottom="10%"),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="2020年8月份客户投诉分析", title_textstyle_opts=opts.TextStyleOpts(font_size=20)),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=16)),
            yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=16)),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(is_show=True, item_width=40, item_height=20, textstyle_opts=opts.TextStyleOpts(font_size=16))
        )
        .set_series_opts(label_opts=True)
    )
    return c


output_path = 'themeriver.html'
themeriver().render(output_path)
webbrowser.open(output_path)
