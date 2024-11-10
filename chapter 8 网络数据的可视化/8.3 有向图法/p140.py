import networkx as nx
import matplotlib.pyplot as plt
import pylab

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(11, 7))

G = nx.DiGraph()
G.add_edges_from([('林丹', '苏冬露'), ('俞毅', '常明媚')], weight=21)
G.add_edges_from([('常明媚', '林丹'), ('常明媚', '吕婵娟'), ('苏冬露', '常明媚'), ('林丹', '周康')], weight=36)
G.add_edges_from([('苏冬露', '俞毅'), ('吕婵娟', '邢伟')], weight=39)
G.add_edges_from([('林丹', '俞毅'), ('吕婵娟', '俞毅')], weight=96)

val_map = {'A': 0.3, 'D': 0.6714285714285714, 'H': 0.8}
values = [val_map.get(node, 0.95) for node in G.nodes()]
edge_labels = dict([((u, v), d['weight']) for u, v, d in G.edges(data=True)])
red_edges = [('林丹', '俞毅'), ('吕婵娟', '俞毅')]
edge_colors = ['black' if edge in red_edges else 'red' for edge in G.edges()]
# 将 not edge in 修改为 edge in即可
black_edges = [edge for edge in G.edges() if edge not in red_edges]

pos = nx.circular_layout(G)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=True)
nx.draw_networkx_edges(G, pos, edgelist=black_edges, arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos)

nx.draw(G, pos, node_color='Gold', node_size=1500, edge_color=edge_colors, edge_cmap=plt.cm.Reds)
pylab.show()
