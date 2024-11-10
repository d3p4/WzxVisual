from pyecharts import options as opts
from pyecharts.charts import Sunburst
import webbrowser


def sunburst() -> Sunburst:
    data = [
        opts.SunburstItem(
            name="古寨",
            children=[
                opts.SunburstItem(
                    name="山水",
                    value=15,
                    children=[
                        opts.SunburstItem(name="山寨喧嚣", value=2),
                        opts.SunburstItem(
                            name="日落",
                            value=5,
                            children=[
                                opts.SunburstItem(name="万家灯火", value=2),
                                opts.SunburstItem(name="水如明镜", value=4),
                            ],
                        ),
                    ],
                ),
                opts.SunburstItem(name="建筑", value=10, children=[
                    opts.SunburstItem(name="博物馆", value=5, children=[
                        opts.SunburstItem(name="宗教文化", value=1),
                        opts.SunburstItem(name="节日文化", value=2),
                    ]),
                ]),
            ],
        ),
        opts.SunburstItem(
            name="苗族",
            children=[
                opts.SunburstItem(
                    name="苗族人",
                    children=[
                        opts.SunburstItem(name="热情好客", value=1),
                        opts.SunburstItem(name="民风民俗", value=2),
                    ],
                ),
            ],
        ),
    ]

    c = (
        Sunburst()
        .add(series_name="", data_pair=data, radius=["0", "90%"])
        .set_global_opts(title_opts=opts.TitleOpts(title="贵州苗族古寨"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
    )
    return c


output_path = 'sunburst.html'
sunburst().render(output_path)
webbrowser.open(output_path)
