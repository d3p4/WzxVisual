import plotly.figure_factory as ff
import plotly.offline as py
import webbrowser

df = [
    dict(Task="需求调研", Start='2020-01-01', Finish='2020-03-10'),
    dict(Task="制定方案", Start='2020-03-11', Finish='2020-05-16'),
    dict(Task="项目实施", Start='2020-05-17', Finish='2020-09-26'),
    dict(Task="项目验收", Start='2020-09-27', Finish='2020-11-10'),
    dict(Task="项目竣工", Start='2020-11-11', Finish='2020-12-31')
]

colors = ['#CDC9A5', '#7D26CD', '#7CFC00', '#A0522D', '#458B74', '#CD0000', '#00008B']

fig = ff.create_gantt(df, show_colorbar=True, colors=colors,
                      index_col='Task', group_tasks=True)
fig.update_layout(
    font=dict(
        family="MicroSoft YaHei",
        size=15,
        color="black"
    ),
    title="2020年企业数据中台项目计划",
    xaxis_title="时间",
    yaxis_title="项目阶段",
    legend=dict(x=0.86, y=0.98, font=dict(size=13, color="black"))
)

py.plot(fig, filename='甘特图.html')
webbrowser.open('甘特图.html')
