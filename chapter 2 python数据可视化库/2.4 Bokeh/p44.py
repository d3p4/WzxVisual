import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, save
import webbrowser

output_file("line_plot.html")

p = figure(width=600, height=400)

x = np.linspace(0, 4 * np.pi, 200)
y = np.cos(x)

p.circle(x, y, legend_label="cos(x)")
p.line(x, y, legend_label="cos(x)")

p.line(x, 2 * y, legend_label="2*cos(x)", line_dash=[4, 4], line_color="orange", line_width=2)

p.square(x, 3 * y, legend_label="3*cos(x)", fill_color=None, line_color="green")
p.line(x, 3 * y, legend_label="3*cos(x)", line_color="green")

p.xaxis.axis_label_text_font_size = "30pt"
p.xaxis.major_label_text_font_size = "20pt"
p.yaxis.axis_label_text_font_size = "30pt"
p.yaxis.major_label_text_font_size = "20pt"

p.legend.location = "bottom_left"
p.legend.orientation = "vertical"

p.legend.label_text_font = "times"
p.legend.label_text_font_style = "italic"
p.legend.label_text_color = "navy"
p.legend.label_text_font_size = '10pt'

p.legend.border_line_width = 3
p.legend.border_line_color = "navy"
p.legend.border_line_alpha = 0.5

p.legend.background_fill_color = "gray"
p.legend.background_fill_alpha = 0.2
p.legend.label_text_font_size = "15pt"

save(p)

webbrowser.open('line_plot.html')
