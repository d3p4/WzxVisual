# import holoviews as hv
# from holoviews import dim, opts
# hv.extension('bokeh', 'matplotlib')
#
# xs = range(-10,11)
# ys = [100-x**2 for x in xs]
# low_ys = [25-(0.5*el)**2 for el in xs]
# shallow = hv.Curve((xs, low_ys),'距离','高度',label='平缓的抛物线').opts(fontsize={'title':20,'labels':16,'xticks':13,'yticks':13})
# medium = hv.Curve((xs, ys),'距离','高度',label='陡峭的抛物线').opts(fontsize={'title':20,'labels':16,'xticks':13,'yticks':13})
# shallow + medium
import holoviews as hv
from holoviews import opts
import webbrowser

hv.extension('bokeh')

xs = range(-10, 11)
ys = [100 - x**2 for x in xs]
low_ys = [25 - (0.5 * el)**2 for el in xs]
shallow = hv.Curve((xs, low_ys), '距离', '高度', label='平缓的抛物线').opts(width=600, height=400, fontsize={'title': 20, 'labels': 16, 'xticks': 13, 'yticks': 13})
medium = hv.Curve((xs, ys), '距离', '高度', label='陡峭的抛物线').opts(fontsize={'title': 20, 'labels': 16, 'xticks': 13, 'yticks': 13})
combined = shallow + medium

hv.save(combined, 'trajectory_curves.html')
webbrowser.open('trajectory_curves.html')
