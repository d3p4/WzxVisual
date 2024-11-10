import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, save
import webbrowser

df = pd.DataFrame(np.random.randn(100, 2), columns=['A', 'B'])

output_file("scatter_plot2.html")

# 课本上的plot_width和 plot_height在较新版本的Bokeh中已经弃用，这里需要改成width和height
p = figure(width=600, height=400, x_axis_label='A', y_axis_label='B')
p.circle(df.index, df['A'], color='green', size=10, alpha=0.5)
p.circle(df.index, df['B'], color='#FF0000', size=10, alpha=0.5)

p.xaxis.axis_label_text_font_size = "30pt"
p.xaxis.major_label_text_font_size = "20pt"
p.yaxis.axis_label_text_font_size = "30pt"
p.yaxis.major_label_text_font_size = "20pt"

save(p)
webbrowser.open("scatter_plot2.html")
