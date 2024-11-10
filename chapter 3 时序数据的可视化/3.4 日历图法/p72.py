from pyecharts.globals import CurrentConfig, NotebookType
CurrentConfig.NOTEBOOK_TYPE = NotebookType.JUPYTER_LAB
from pyecharts import options as opts
from pyecharts.charts import Calendar, Page
import webbrowser
from dbconn import conn


cursor = conn.cursor()
sql_num = "SELECT trade_date,close FROM stocks WHERE year(trade_date)=2020"
cursor.execute(sql_num)
sh = cursor.fetchall()
v1 = []
for s in sh:
    v1.append([s[0], s[1]])
data = v1


def calendar_base() -> Calendar:
    c = (
        Calendar()
            .add("", data, calendar_opts=opts.CalendarOpts(range_="2020"))
            .set_global_opts(
            title_opts=opts.TitleOpts(title="2020年上半年股票收盘价日历图"),
            visualmap_opts=opts.VisualMapOpts(
                max_=95,
                min_=65,
                orient="horizontal",  # vertical垂直的，horizontal水平的
                is_piecewise=True,
                pos_top="200px",
                pos_left="10px"
            ),
            toolbox_opts=opts.ToolboxOpts(is_show=False),
            legend_opts=opts.LegendOpts(is_show=True)
        )
    )
    return c


calendar = calendar_base()
calendar.render('calendar_chart.html')
webbrowser.open('calendar_chart.html')
