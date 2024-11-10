# import holoviews as hv
# from holoviews import dim, opts
# hv.extension('bokeh', 'matplotlib')
#
# xs = range(-10,11)
# ys = [100-x**2 for x in xs]
# trajectory = hv.Curve((xs, ys),'距离','高度').opts(fontsize={'title':20,'labels':16,'xticks':13,'yticks':13})
# trajectory
import holoviews as hv
from holoviews import opts
import webbrowser

hv.extension('bokeh')

xs = range(-10, 11)
ys = [100 - x**2 for x in xs]
trajectory = hv.Curve((xs, ys), '距离', '高度').opts(width=600, height=400,
                                                 fontsize={'title': 20, 'labels': 16, 'xticks': 13, 'yticks': 13})

hv.save(trajectory, 'trajectory.html')
webbrowser.open('trajectory.html')
