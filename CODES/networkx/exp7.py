import matplotlib.pyplot as plt
import networkx as nx

# Create graph
G = nx.Graph()

# Edges from the given image
edges = [
    (1, 3, 5),
    (1, 2, 14),
    (1, 4, 2),

    (3, 2, 9),
    (2, 4, 8),

    (3, 6, 8),
    (3, 5, 13),
    (2, 5, 15),
    (4, 5, 10),

    (5, 6, 1),
    (5, 7, 7),
    (5, 8, 5),

    (6, 7, 10),
    (7, 8, 0),

    (6, 9, 11),
    (7, 9, 12),
    (8, 9, 6),

    (4, 8, 11)
]

# Add weighted edges
G.add_weighted_edges_from(edges)

# Node positions to match image layout
pos = {
    1: (-4, 0),

    3: (-2, 2),
    2: (-2, 0),
    4: (-2, -2),

    5: (0, 0),

    6: (2, 2),
    7: (2, 0),
    8: (2, -2),

    9: (4, 0)
}

# Source and target
source = 1
target = 9

# Dijkstra shortest path
path = nx.dijkstra_path(G, source, target)
length = nx.dijkstra_path_length(G, source, target)

print("Shortest Path:", path)
print("Total Cost:", length)

# Draw graph
plt.figure(figsize=(10, 7))

nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    node_color='lightblue',
    font_size=12,
    font_weight='bold'
)

# Draw edge weights
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Highlight shortest path
path_edges = list(zip(path, path[1:]))
nx.draw_networkx_edges(
    G,
    pos,
    edgelist=path_edges,
    edge_color='red',
    width=3
)

plt.title("Shortest Path using Dijkstra Algorithm")
plt.axis('off')
plt.show()