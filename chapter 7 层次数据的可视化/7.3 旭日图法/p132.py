from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB

from pyecharts import options as opts
from pyecharts.charts import Sunburst
import webbrowser

def sunburst() -> Sunburst:
    data = [
        opts.SunburstItem(
            name="爷爷奶奶",
            children=[
                opts.SunburstItem(
                    name="张叔叔李阿姨",
                    value=15,
                    children=[
                        opts.SunburstItem(name="表妹张诗诗", value=2),
                        opts.SunburstItem(
                            name="表哥张政",
                            value=5,
                            children=[opts.SunburstItem(name="表侄张佳", value=2)],
                        ),
                        opts.SunburstItem(name="表姐张意涵", value=4,
                             children=[opts.SunburstItem(name="表侄张文海", value=2)],
                        ),
                    ],
                ),
                opts.SunburstItem(
                    name="爸爸妈妈",
                    value=10,
                    children=[
                        opts.SunburstItem(name="我", value=5),
                        opts.SunburstItem(name="哥哥张伟", value=3),
                    ],
                ),
            ],
        ),
    ]

    c = (
        Sunburst()
        .add(series_name="我的家庭成员旭日图", data_pair=data, radius=[0, "85%"])
        .set_global_opts(title_opts=opts.TitleOpts(title="我的家庭成员旭日图"),
                         toolbox_opts=opts.ToolboxOpts())
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}"))
    )
    return c

if __name__ == "__main__":
    chart = sunburst()
    chart.render('sunburst_family.html')
    webbrowser.open('sunburst_family.html')
