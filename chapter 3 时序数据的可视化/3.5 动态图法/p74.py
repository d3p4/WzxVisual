from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline
from pyecharts.faker import Faker
import webbrowser

attr = Faker.choose()
tl = Timeline()

for i in range(2014, 2021):
    pie = (
        Pie()
        .add(
            "销售额",
            [list(z) for z in zip(attr, Faker.values())],
            rosetype="radius",
            radius=["30%", "55%"],
        )
        .set_global_opts(title_opts=opts.TitleOpts("企业{}年商品销售额".format(i)))
    )
    tl.add(pie, "{}年".format(i))


tl.render('timeline_pie_chart.html')
webbrowser.open('timeline_pie_chart.html')