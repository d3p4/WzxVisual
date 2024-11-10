import math
from typing import Union
import pyecharts.options as opts
from pyecharts.charts import Surface3D
import webbrowser


def float_range(start: int, end: int, step: Union[int, float], round_number: int = 2):
    temp = []
    while True:
        if start < end:
            temp.append(round(start, round_number))
            start += step
        else:
            break
    return temp


def surface3d_data():
    for t0 in float_range(-5, 5, 0.05):
        y = t0
        for t1 in float_range(-5, 5, 0.25):
            x = t1
            z = math.sin(x + y) * x * y / 2
            yield [x, y, z]

(
    Surface3D(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name="",
        shading="color",
        data=list(surface3d_data()),
        xaxis3d_opts=opts.Axis3DOpts(type_="value"),
        yaxis3d_opts=opts.Axis3DOpts(type_="value"),
        grid3d_opts=opts.Grid3DOpts(width=80, height=40, depth=80),
    )
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(
            dimension=2,
            max_=1,
            min_=-1,
            range_color=["#1E90FF", "#00BFFF", "#FFD700", "#FF8C00", "#FF0000"]
        )
    )
    .render("三维曲面.html")
)

webbrowser.open("三维曲面.html")
