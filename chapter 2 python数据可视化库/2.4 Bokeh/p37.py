from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.io import output_file, show

output_file("折线图.html")

p = figure(width=900, height=600)
# 课本上的plot_width和 plot_height在较新版本的Bokeh中已经弃用，这里需要改成width和height
p.line([1,  2,  3,  4,  5,  6,  7,  8,  9,  10,  11,  12],
       [270,  287,  293,  276, 315, 339, 297, 357, 376, 316, 325, 308],
       legend_label="销售额",  line_width=3)

p.xaxis.axis_label = "月份"
p.xaxis.axis_label_text_font_size = "30pt"
p.xaxis.major_label_text_font_size = "20pt"

p.xaxis.ticker = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

p.yaxis.axis_label = "销售额"
p.yaxis.axis_label_text_font_size = "30pt"
p.yaxis.major_label_text_font_size = "20pt"

p.legend.label_text_font_size = "30pt"

show(p)
