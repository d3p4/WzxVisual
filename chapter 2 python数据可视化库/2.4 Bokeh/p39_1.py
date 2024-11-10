import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, save
import webbrowser

df = pd.DataFrame(np.random.randn(100, 2), columns=['A', 'B'])
output_file("scatter_plot1.html")
# 课本上的plot_width和 plot_height在较新版本的Bokeh中已经弃用，这里需要改成width和height
p = figure(width=600, height=400,
           tools='pan,box_zoom,save,reset,help',
           toolbar_location='above',
           x_axis_label='A', y_axis_label='B',
           x_range=[-3, 3], y_range=[-3, 3]
           )

p.xaxis.axis_label_text_font_size = "30pt"
p.xaxis.major_label_text_font_size = "20pt"
p.yaxis.axis_label_text_font_size = "30pt"
p.yaxis.major_label_text_font_size = "20pt"

p.circle(df['A'], df['B'], size=20, alpha=0.5)

save(p)
webbrowser.open("scatter_plot1.html")
