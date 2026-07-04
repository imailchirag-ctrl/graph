import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# Add vertices
vertices = ['a', 'b', 'c', 'd', 'e', 'f']
G.add_nodes_from(vertices)

# Add edges
edges = [
    ('a', 'f'),
    ('a', 'e'),
    ('a', 'c'),
    ('a', 'b'),

    ('f', 'b'),
    ('f', 'e'),
    ('f', 'd'),
    ('f', 'c'),

    ('b', 'c'),
    ('b', 'd'),

    ('c', 'e'),
    ('c', 'd'),

    ('d', 'e')
]

G.add_edges_from(edges)

# Greedy Coloring
coloring = nx.coloring.greedy_color(G, strategy='largest_first')

# Color name mapping
color_names = {
    0: "Red",
    1: "Blue",
    2: "Green",
    3: "Yellow",
    4: "Orange"
}

print("Vertex Colors:")
for node, color in coloring.items():
    print(node, "->", color_names[color])

# Chromatic Number
chromatic_number = max(coloring.values()) + 1
print("\nChromatic Number =", chromatic_number)

# Positioning
pos = {
    'a': (-2, 0),
    'f': (-1, 1),
    'b': (-1, -1),
    'e': (1, 1),
    'c': (1, -1),
    'd': (2, 0)
}

# Create two subplots
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Original Graph
nx.draw(
    G,
    pos,
    ax=axes[0],
    with_labels=True,
    node_color='lightgray',
    node_size=2000,
    font_size=15,
    font_color='black',
    edge_color='black'
)
axes[0].set_title("Original Graph")

# Colored Graph
colors = ['red', 'blue', 'green', 'yellow', 'orange']
node_colors = [colors[coloring[node]] for node in G.nodes()]

nx.draw(
    G,
    pos,
    ax=axes[1],
    with_labels=True,
    node_color=node_colors,
    node_size=2000,
    font_size=15,
    font_color='white',
    edge_color='black'
)

axes[1].set_title(f"Greedy Graph Coloring\nChromatic Number = {chromatic_number}")

plt.tight_layout()
plt.show()