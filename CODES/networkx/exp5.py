import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

n = int(input("Enter number of vertices: "))
print("Enter adjacency matrix:")
adj_matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    if len(row) != n:
        raise ValueError(f"Each row must contain {n} entries.")
    adj_matrix.append(row)

G = nx.from_numpy_array(np.array(adj_matrix))
L = nx.line_graph(G)

print("Original Graph Edges:")
print(list(G.edges()))
print("\nLine Graph Vertices (edges of original graph):")
print(list(L.nodes()))
print("\nLine Graph Edges:")
print(list(L.edges()))

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Original Graph")
nx.draw(G, with_labels=True, node_color='lightblue', node_size=800)

plt.subplot(1, 2, 2)
plt.title("Line Graph")
nx.draw(L, with_labels=True, node_color='lightgreen', node_size=800)
plt.show()
