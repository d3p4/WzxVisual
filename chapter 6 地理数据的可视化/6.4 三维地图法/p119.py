from pyecharts import options as opts
from pyecharts.charts import Map3D
import webbrowser

satisfaction = [
    ["武汉市", 95], ["荆门市", 94], ["黄石市", 92], ["孝感市", 88],
    ["十堰市", 91], ["荆州市", 90], ["宜昌市", 99], ["黄冈市", 99],
    ["襄阳市", 92], ["咸宁市", 72], ["鄂州市", 76], ["随州市", 95]
]

c = (
    Map3D(init_opts=opts.InitOpts(width="850px", height="500px"))
    .add_schema(
        maptype="湖北",
        itemstyle_opts=opts.ItemStyleOpts(
            opacity=1,
            border_width=0.8,
        ),
        map3d_label=opts.Map3DLabelOpts(
            is_show=False,
        ),
        emphasis_label_opts=opts.LabelOpts(
            is_show=False,
            font_size=5,
        ),
        light_opts=opts.Map3DLightOpts(
            main_intensity=1.2,
            main_shadow_quality="high",
            is_main_shadow=False,
            main_beta=10,
            ambient_intensity=0.3,
        ),
    )
    .add(
        series_name="",
        maptype="湖北",
        data_pair=satisfaction,
        is_map_symbol_show=False,
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="湖北省主要城市客户满意度的三维地图"),
        visualmap_opts=opts.VisualMapOpts(
            min_=60,
            max_=100,
            range_text=["100分", "60分"],
            is_calculable=False,
            range_color=['#22DDB8', "blue", "yellow", "red"],
            pos_top=40
        )
    )
    .render("119三维地图.html")
)

webbrowser.open("119三维地图.html")