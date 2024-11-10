from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType
import webbrowser

c = (
    Geo()
    .add_schema(maptype="湖北")
    .add(
        "",
        [("武汉市", 184), ("荆门市", 192), ("黄石市", 131), ("孝感市", 79),
         ("十堰市", 71), ("荆州市", 83), ("宜昌市", 56), ("黄冈市", 99),
         ("襄阳市", 65), ("咸宁市", 49), ("鄂州市", 52), ("随州市", 79)],
        type_=ChartType.HEATMAP,
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=True))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(),
        title_opts=opts.TitleOpts(title="湖北省主要城市销售额的热力地图")
    )
    .render("116热力地图.html")
)

webbrowser.open("116热力地图.html")