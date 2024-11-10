import networkx as nx
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

nodes = ['A', 'B', 'C', 'D', 'E', 'F']
edges = [('A', 'C'), ('A', 'B'), ('A', 'E'), ('B', 'E'), ('B', 'F'), ('C', 'F'), ('C', 'E'), ('D', 'F')]

plt.figure(figsize=(11, 7))
G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.shell_layout(G)

plt.title('客户商品分享的网络关系图', size=20)
nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), node_color='GoldEnrod', node_size=900)
nx.draw_networkx_labels(G, pos, font_size=16)
nx.draw_networkx_edges(G, pos, arrows=True)
plt.axis('off')
plt.show()
