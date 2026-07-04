import matplotlib.pyplot as plt

# =====================================================
# VERTICES
# =====================================================

vertices = ['a', 'b', 'c', 'd', 'e', 'f']

# =====================================================
# EDGES
# =====================================================

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

# =====================================================
# ADJACENCY LIST
# =====================================================

adj = {v: set() for v in vertices}

for u, v in edges:
    adj[u].add(v)
    adj[v].add(u)

# =====================================================
# GREEDY COLORING (Largest Degree First)
# =====================================================

sorted_vertices = sorted(
    vertices,
    key=lambda x: len(adj[x]),
    reverse=True
)

coloring = {}

for vertex in sorted_vertices:

    used_colors = set()

    for neighbor in adj[vertex]:
        if neighbor in coloring:
            used_colors.add(coloring[neighbor])

    color = 0
    while color in used_colors:
        color += 1

    coloring[vertex] = color

# =====================================================
# OUTPUT
# =====================================================

print("Vertex Colors:\n")

for node in sorted(vertices):
    print(node, "-> Color", coloring[node])

chromatic_number = max(coloring.values()) + 1

print("\nChromatic Number =", chromatic_number)

# =====================================================
# POSITIONS
# =====================================================

pos = {
    'a': (-2, 0),
    'f': (-1, 1),
    'b': (-1, -1),
    'e': (1, 1),
    'c': (1, -1),
    'd': (2, 0)
}

# =====================================================
# COLOR MAP
# =====================================================

color_map = {
    0: "red",
    1: "blue",
    2: "green",
    3: "yellow"
}

# =====================================================
# DRAW FUNCTION
# =====================================================

def draw_graph(ax, node_colors, title):

    # Draw edges
    for u, v in edges:

        x = [pos[u][0], pos[v][0]]
        y = [pos[u][1], pos[v][1]]

        ax.plot(
            x,
            y,
            color='black',
            linewidth=2
        )

    # Draw vertices
    for node in vertices:

        x, y = pos[node]

        ax.scatter(
            x,
            y,
            s=2200,
            color=node_colors[node],
            edgecolors='black',
            zorder=5
        )

        text_color = "white"

        if node_colors[node] == "yellow":
            text_color = "black"

        ax.text(
            x,
            y,
            node,
            fontsize=15,
            fontweight='bold',
            ha='center',
            va='center',
            color=text_color,
            zorder=10
        )

    ax.set_title(title, fontsize=14)
    ax.axis('off')

# =====================================================
# ORIGINAL GRAPH COLORS
# =====================================================

original_colors = {
    node: "lightgray"
    for node in vertices
}

# =====================================================
# COLORED GRAPH
# =====================================================

colored_nodes = {}

for node in vertices:
    colored_nodes[node] = color_map[coloring[node]]

# =====================================================
# DISPLAY SIDE BY SIDE
# =====================================================

fig, axes = plt.subplots(1, 2, figsize=(12, 6))

draw_graph(
    axes[0],
    original_colors,
    "Original Graph"
)

draw_graph(
    axes[1],
    colored_nodes,
    f"Greedy Coloring\nChromatic Number = {chromatic_number}"
)

plt.tight_layout()
plt.show()