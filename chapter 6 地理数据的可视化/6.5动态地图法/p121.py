from pyecharts import options as opts
from pyecharts.charts import Geo
from pyecharts.globals import ChartType, SymbolType
import webbrowser

c = (
    Geo()
    .add_schema(maptype="湖北")
    .add(
        "",
        [("随州市", 66), ("孝感市", 77), ("武汉市", 88), ("咸宁市", 100),
         ("黄冈市", 30), ("宜昌市", 120), ("鄂州市", 77), ("黄石市", 88),
         ("襄阳市", 100), ("荆门市", 30), ("十堰市", 120), ("荆州市", 66)],
        type_=ChartType.EFFECT_SCATTER,
        color="green",
    )
    .add(
        "物流货运量",
        [("孝感市", "武汉市"), ("咸宁市", "武汉市"), ("孝感市", "咸宁市"),
         ("武汉市", "黄冈市"), ("武汉市", "宜昌市"), ("武汉市", "鄂州市"),
         ("武汉市", "黄石市"), ("武汉市", "咸宁市"), ("荆门市", "黄石市"),
         ("武汉市", "荆州市"), ("武汉市", "十堰市"), ("武汉市", "襄阳市"),
         ("武汉市", "随州市"), ("襄阳市", "宜昌市"), ("十堰市", "宜昌市")],
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(
            symbol=SymbolType.ARROW, symbol_size=6, color="blue"
        ),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(title_opts=opts.TitleOpts(title="湖北省主要城市物流路线及货运量"))
)

c.render("121动态地图.html")
webbrowser.open("121动态地图.html")
