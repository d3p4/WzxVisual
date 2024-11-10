import json
from pyecharts import options as opts
from pyecharts.charts import Graph
import webbrowser

with open("D:/py_practice/python可视化/各章节数据源//ch07/miserables.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes = j["nodes"]
    links = j["links"]

c = (
    Graph(init_opts=opts.InitOpts(width="550px", height="550px"))
    .add(
        "",
        nodes=nodes,
        links=links,
        layout="circular",
        is_rotate_label=True,
        linestyle_opts=opts.LineStyleOpts(color="source", curve=0.4),
        label_opts=opts.LabelOpts(position="right"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="2020年9月客户分享和弦图", title_textstyle_opts=opts.TextStyleOpts(font_size=20)),
        legend_opts=opts.LegendOpts(orient="vertical", pos_left="20%", pos_top="20%"),
    )
)

c.render("和弦图.html")
webbrowser.open("和弦图.html")
