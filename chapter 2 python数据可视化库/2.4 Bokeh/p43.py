import pandas as pd
import numpy as np
from bokeh.plotting import figure, output_file, save
import webbrowser

df = pd.DataFrame(np.random.randn(200, 2), columns=['A', 'B'])

output_file("scatter_plot7.html")

p = figure(width=600, height=400, x_axis_label='A', y_axis_label='B')
p.circle(df.index, df['A'], color='green', size=10, alpha=0.5)
p.circle(df.index, df['B'], color='#FF0000', size=10, alpha=0.5)

p.xaxis.axis_label_text_font_size = "30pt"
p.xaxis.major_label_text_font_size = "20pt"
p.yaxis.axis_label_text_font_size = "30pt"
p.yaxis.major_label_text_font_size = "20pt"

p.xgrid.grid_line_color = 'red'
p.ygrid.grid_line_alpha = 0.1
p.ygrid.grid_line_dash = [11, 4]
p.xgrid.minor_grid_line_color = 'navy'
p.xgrid.minor_grid_line_alpha = 0.1
p.ygrid.band_fill_alpha = 0.1
p.ygrid.band_fill_color = "navy"
p.grid.bounds = (-3, 200)

save(p)

webbrowser.open('scatter_plot7.html')
