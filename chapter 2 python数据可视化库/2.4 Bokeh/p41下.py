import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, save
import webbrowser

df = pd.DataFrame(np.random.randn(200, 2), columns=['A', 'B'])

output_file("scatter_plot5.html")

# 课本上的plot_width和plot_height在较新版本的Bokeh中已经弃用，这里需要改成width和height
p = figure(width=600, height=400, x_axis_label='A', y_axis_label='B')
p.circle(df['A'], df['B'], size=10)

p.xaxis.axis_label_text_font_size = "30pt"
p.xaxis.major_label_text_font_size = "20pt"
p.yaxis.axis_label_text_font_size = "30pt"
p.yaxis.major_label_text_font_size = "20pt"

p.xaxis.axis_label = "X的数值"
p.xaxis.axis_label_text_color = "#aa6666"
p.xaxis.axis_label_standoff = 5
p.xaxis.axis_line_width = 3
p.xaxis.axis_line_color = "red"
p.xaxis.axis_line_dash = [6, 4]

p.yaxis.axis_label = "Y的数值"
p.yaxis.axis_label_text_font_style = "italic"
p.yaxis.major_label_text_color = "orange"
p.yaxis.major_label_orientation = "vertical"

p.axis.minor_tick_in = 10
p.axis.minor_tick_out = 3

p.xaxis.bounds = (-4, 4)

save(p)

webbrowser.open('scatter_plot5.html')
