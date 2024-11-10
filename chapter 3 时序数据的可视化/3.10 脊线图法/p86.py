import altair as alt
import pandas as pd
import webbrowser

source = pd.read_csv('D:/py_practice/python可视化/各章节数据源/ch03/return_days.csv')

step = 25
overlap = 1

chart = (
    alt.Chart(source, height=step)
    .transform_timeunit(Month='month(date)')
    .transform_joinaggregate(mean_temp='mean(return)', groupby=['Month'])
    .transform_bin(['bin_max', 'bin_min'], 'return')
    .transform_aggregate(value='count()', groupby=['Month', 'mean_temp', 'bin_min', 'bin_max'])
    .transform_impute(impute='value', groupby=['Month', 'mean_temp'], key='bin_min', value=0)
    .mark_area(interpolate='monotone', fillOpacity=0.8, stroke='lightgray', strokeWidth=0.3)
    .encode(
        alt.X('bin_min:Q', bin='binned', title='退单量'),
        alt.Y('value:Q', scale=alt.Scale(range=[step, -step * overlap]), axis=None),
        alt.Fill('mean_temp:Q', legend=None, scale=alt.Scale(domain=[30, 5], scheme='redyellowblue'))
    )
    .facet(
        row=alt.Row('Month:T', title=None, header=alt.Header(labelAngle=0, labelAlign='right', format='%B'))
    )
    .properties(title='退单量分析', bounds='flush')
    .configure_facet(spacing=0)
    .configure_view(stroke=None)
    .configure_title(anchor='end')
)

chart.save('退单量分析.html')
webbrowser.open('退单量分析.html')
