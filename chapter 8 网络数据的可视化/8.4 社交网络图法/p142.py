import pandas as pd
import holoviews as hv
from bokeh.io import output_file, show
from bokeh.resources import INLINE
import webbrowser

hv.extension('bokeh')

edges_df = pd.read_csv('D:/py_practice/python可视化/各章节数据源/ch08/edges.csv')
nodes_df = pd.read_csv('D:/py_practice/python可视化/各章节数据源/ch08/nodes.csv')

if len(nodes_df.columns) < 3:
    nodes_df['dummy'] = 0

fb_nodes = hv.Nodes(nodes_df)
fb_graph = hv.Graph((edges_df, fb_nodes), label='商品分享朋友圈')

colors = ['#000000']+hv.Cycle('Category20').values
fb_graph = fb_graph.redim.range(x=(-0.05, 1.05), y=(-0.05, 1.05))
fb_graph.opts(color_index='circle', width=600, height=600, show_frame=True,
              xaxis=None, yaxis=None, node_size=25, edge_line_width=2, cmap=colors)

output_file("network_graph.html")
hv.save(fb_graph, 'network_graph.html')
webbrowser.open('network_graph.html', new=2)
