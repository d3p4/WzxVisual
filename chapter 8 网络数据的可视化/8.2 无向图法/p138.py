import networkx as nx
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

plt.figure(figsize=(11, 8))
G = nx.DiGraph()
G.add_edges_from([
    ('林丹', '苏冬露'), ('俞毅', '常明媚'), ('邢伟', '常明媚'),
    ('常明媚', '林丹'), ('常明媚', '吕婵娟'), ('苏冬露', '常明媚'),
    ('林丹', '周康'), ('苏冬露', '俞毅'), ('吕婵娟', '邢伟'),
    ('林丹', '俞毅'), ('吕婵娟', '俞毅')
])

val_map = {'A': 0.3, 'D': 0.6714285714285714, 'H': 0.8}
values = [val_map.get(node, 0.25) for node in G.nodes()]

red_edges = [('林丹', '俞毅'), ('吕婵娟', '俞毅')]
edge_colors = ['red' if edge in red_edges else 'black' for edge in G.edges()]
# 将 not edge in 修改为 edge in，并将颜色列表生成逻辑反转，使用三元表达式使代码更简洁。
pos = nx.circular_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='GoldEnrod', node_size=1300)
nx.draw_networkx_labels(G, pos, font_size=13)
nx.draw_networkx_edges(G, pos, edgelist=red_edges, edge_color='r', arrows=False)
nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color=edge_colors, arrows=False)

plt.axis('off')
plt.show()
