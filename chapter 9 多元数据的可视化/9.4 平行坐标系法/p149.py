import pyecharts.options as opts
from pyecharts.charts import Parallel
import webbrowser

parallel_axis = [
    {"dim": 0, "name": "商品类型", "type": "category"},
    {"dim": 1, "name": "东北"},
    {"dim": 2, "name": "华北"},
    {"dim": 3, "name": "华东"},
    {"dim": 4, "name": "西南"},
    {"dim": 5, "name": "中南"},
    {"dim": 6, "name": "西北"},
    {"dim": 7, "name": "业绩评估", "type": "category", "data": ["较差", "一般", "较好", "优秀"]}
]

data = [
    ["用具", 1.68, 1.66, 0.3, 2.62, 2.63, 2.22, "较差"],
    ["纸张", 4.68, 5.26, 8.3, 6.82, 9.03, 4.62, "一般"],
    ["书架", 6.18, 7.26, 6.3, 4.82, 8.03, 3.32, "一般"],
    ["器具", 9.18, 9.26, 13.3, 13.82, 14.63, 11.62, "较好"],
    ["配件", 8.18, 8.26, 10.3, 11.82, 13.03, 14.52, "较好"],
    ["设备", 12.98, 18.66, 15.83, 19.62, 15.93, 18.82, "优秀"]
]


def Parallel_splitline() -> Parallel:
    c = (
        Parallel()
        .add_schema(schema=parallel_axis)
        .add(series_name="", data=data, linestyle_opts=opts.LineStyleOpts(width=4, opacity=0.5))
    )
    return c


Parallel_splitline().render('平行坐标系.html')
webbrowser.open('平行坐标系.html')
