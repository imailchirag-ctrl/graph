import matplotlib.pyplot as plt
import networkx as nx
G = nx.Graph()
nodes = [1,2,3,4,5,6]
edges = [(1,2),(1,3),(2,3),(2,4),(3,5),(4,5),(5,6)]
for n in nodes:
    G.add_node(n)
for e in edges:
    G.add_edge(e[0], e[1])

plt.figure(figsize=(12,10))

# 1. Original Graph
plt.subplot(2,2,1)
nx.draw(G, with_labels=True, node_color='lightblue', node_size=800)
plt.title("Original Graph")
subset = [1,2,3,4]
G_induced = nx.Graph()
for n in subset:
    G_induced.add_node(n)
for (u,v) in edges:
    if u in subset and v in subset:
        G_induced.add_edge(u,v)
plt.subplot(2,2,2)
nx.draw(G_induced, with_labels=True, node_color='lightgreen', node_size=800)
plt.title("Induced Subgraph")
G_spanning = nx.Graph()
for n in nodes:
    G_spanning.add_node(n)
spanning_edges = [(1,2),(2,4),(4,5),(5,6)]

for (u,v) in spanning_edges:
    G_spanning.add_edge(u,v)
plt.subplot(2,2,3)
nx.draw(G_spanning, with_labels=True, node_color='orange', node_size=800)
plt.title("Spanning Subgraph")
G_edge_deleted = nx.Graph()
for n in nodes:
    G_edge_deleted.add_node(n)
for (u,v) in edges:
    if not ((u == 2 and v == 3) or (u == 3 and v == 2)):
        G_edge_deleted.add_edge(u,v)
plt.subplot(2,2,4)
nx.draw(G_edge_deleted, with_labels=True, node_color='pink', node_size=800)
plt.title("Edge Deleted Subgraph")
plt.tight_layout()
plt.show()