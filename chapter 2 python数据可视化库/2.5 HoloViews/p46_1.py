# import holoviews as hv
# from holoviews import dim, opts
# hv.extension('bokeh', 'matplotlib')
#
# xs = range(-10,11)
# ys = [100-x**2 for x in xs]
# curve = hv.Curve((xs, ys)).opts(fontsize={'title': 20, 'labels': 16, 'xticks': 13, 'yticks': 13})
#
# curve
import holoviews as hv
from holoviews import opts
import webbrowser

hv.extension('bokeh')

xs = range(-10, 11)
ys = [100 - x**2 for x in xs]
curve = hv.Curve((xs, ys)).opts(width=600, height=400,
                                fontsize={'title': 20, 'labels': 16, 'xticks': 13, 'yticks': 13})

hv.save(curve, 'curve.html')
webbrowser.open('curve.html')
