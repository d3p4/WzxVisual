import pyecharts.options as opts
from pyecharts.charts import Parallel
import webbrowser

# 定义平行坐标系的轴
parallel_axis = [
    {"dim": 0, "name": "销售大区", "type": "category"},
    {"dim": 1, "name": "2014年"},
    {"dim": 2, "name": "2015年"},
    {"dim": 3, "name": "2016年"},
    {"dim": 4, "name": "2017年"},
    {"dim": 5, "name": "2018年"},
    {"dim": 6, "name": "2019年"},
    {"dim": 7, "name": "2020年"},
    {"dim": 8, "name": "业绩评估", "type": "category", "data": ["Bad", "OK", "Good", "Excellent"]}
]

# 定义数据
data = [
    ["西北", 1.18, 1.26, 0.3, 2.82, 2.03, 2.62, 2.02, "Bad"],
    ["华中", 7.18, 9.26, 12.3, 6.82, 9.03, 4.62, 2.82, "OK"],
    ["西南", 6.18, 7.26, 10.3, 4.82, 8.03, 3.32, 6.12, "OK"],
    ["华南", 9.18, 9.26, 13.3, 13.82, 14.63, 11.62, 15.12, "Good"],
    ["东北", 8.18, 8.26, 10.3, 11.82, 13.03, 14.52, 10.12, "Good"],
    ["华东", 10.98, 18.66, 20.83, 15.62, 17.93, 16.82, 19.62, "Excellent"]
]


def parallel_splitline() -> Parallel:
    c = (
        Parallel()
        .add_schema(schema=parallel_axis)
        .add(
            series_name="",
            data=data,
            linestyle_opts=opts.LineStyleOpts(width=4, opacity=0.5),
        )
    )
    return c


parallel_chart = parallel_splitline()
parallel_chart.render('parallel_chart.html')
webbrowser.open('parallel_chart.html')
