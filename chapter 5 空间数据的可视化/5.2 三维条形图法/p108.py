import pyecharts.options as opts
from pyecharts.charts import Bar3D
import webbrowser

hours = ["1时", "2时", "3时", "4时", "5时",  "6时",  "7时",  "8时", "9时", "10时",  "11时", "12时",
         "13时", "14时", "15时", "16时", "17时", "18时", "19时", "20时", "21时", "22时", "23时", "24时"]
days = ["周日", "周一", "周二", "周三", "周四", "周五", "周六"]

data = [
   [0, 9, 19], [0, 16, 14], [1, 9, 11], [1, 20, 15], [2, 6, 9],
   [2, 17, 5], [2, 20, 7], [3, 12, 9], [3, 11, 18], [3, 20, 16],
   [4, 21, 10], [4, 22, 13], [4, 23, 6], [5, 6, 8], [5, 8, 10],
   [5, 12, 4], [5, 18, 6], [6, 22, 3], [6, 10, 8], [6, 23, 16],
]
data = [[d[1], d[0], d[2]] for d in data]

(
    Bar3D(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name="",
        data=data,
        xaxis3d_opts=opts.Axis3DOpts(type_="category", data=hours),
        yaxis3d_opts=opts.Axis3DOpts(type_="category", data=days),
        zaxis3d_opts=opts.Axis3DOpts(type_="value"),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            max_=20,
            range_color=["#1E90FF", "#00BFFF", "#FFD700", "#FF8C00", "#FF0000",])
    )
    .render("三维条形图.html")
)

webbrowser.open("三维条形图.html")
