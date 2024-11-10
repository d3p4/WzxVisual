from pyecharts import options as opts
from pyecharts.charts import Map
import webbrowser

c = (
    Map()
    .add(
        "",
        [("武汉市", 18.4), ("荆门市", 19.2), ("黄石市", 13.1), ("孝感市", 14.9),
         ("十堰市", 7.1), ("荆州市", 8.3), ("宜昌市", 15.6), ("黄冈市", 9.9),
         ("襄阳市", 6.5), ("咸宁市", 4.9), ("鄂州市", 5.2), ("随州市", 11.9)],
        "湖北"
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="湖北省主要城市利润额的着色地图"),
        visualmap_opts=opts.VisualMapOpts(max_=20, is_piecewise=True)
    )
    .render("118着色地图.html")
)

webbrowser.open("118着色地图.html")
