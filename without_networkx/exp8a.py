import matplotlib.pyplot as plt

# =====================================================
# DRAW FUNCTION
# =====================================================

def draw_graph(ax, pos, edges,
               highlight_edges=None,
               highlight_color='red',
               title=""):

    # Draw all edges
    for u, v in edges:
        x = [pos[u][0], pos[v][0]]
        y = [pos[u][1], pos[v][1]]

        ax.plot(
            x, y,
            color='gray',
            linewidth=1.5,
            zorder=1
        )

    # Highlighted edges
    if highlight_edges:
        for u, v in highlight_edges:

            x = [pos[u][0], pos[v][0]]
            y = [pos[u][1], pos[v][1]]

            ax.plot(
                x, y,
                color=highlight_color,
                linewidth=4,
                zorder=2
            )

    # Draw nodes
    for node, (x, y) in pos.items():

        ax.scatter(
            x, y,
            s=700,
            color='black',
            zorder=3
        )

        ax.text(
            x, y,
            str(node),
            color='white',
            fontsize=12,
            fontweight='bold',
            ha='center',
            va='center',
            zorder=4
        )

    ax.set_title(title)
    ax.axis('off')


# =====================================================
# GRAPH 1
# =====================================================

edges1 = [
    ('A','B'),
    ('A','C'),
    ('B','C'),
    ('B','D'),
    ('C','D'),
    ('B','E'),
    ('D','E'),
    ('D','F'),
    ('E','F'),
    ('C','F')
]

pos1 = {
    'A': (0,1),
    'B': (1,2),
    'C': (1,0),
    'D': (2,1),
    'E': (3,2),
    'F': (3,0)
}

path1 = ['A','B','D','E']
path_edges1 = list(zip(path1[:-1], path1[1:]))

closed1 = ['A','B','C','A']
closed_edges1 = list(zip(closed1[:-1], closed1[1:]))

trail1 = ['A','C','D','F','E','B']
trail_edges1 = list(zip(trail1[:-1], trail1[1:]))

# =====================================================
# GRAPH 2
# =====================================================

edges2 = [
    ('A','B'),
    ('A','C'),
    ('B','C'),
    ('B','D'),
    ('C','D'),
    ('B','E'),
    ('D','E'),
    ('D','F'),
    ('E','F'),
    ('E','G'),
    ('F','G'),
    ('C','F')
]

pos2 = {
    'A': (0,1),
    'B': (1,2),
    'C': (1,0),
    'D': (2,1),
    'E': (3,2),
    'F': (3,0),
    'G': (4,1)
}

path2 = ['A','B','D','E','G']
path_edges2 = list(zip(path2[:-1], path2[1:]))

closed2 = ['E','G','F','E']
closed_edges2 = list(zip(closed2[:-1], closed2[1:]))

trail2 = ['A','B','E','G','F','C','D']
trail_edges2 = list(zip(trail2[:-1], trail2[1:]))

# =====================================================
# DISPLAY
# =====================================================

fig, axes = plt.subplots(2, 4, figsize=(24, 10))

# ---------------- Graph 1 ----------------

draw_graph(
    axes[0,0],
    pos1,
    edges1,
    title="Graph 1 : Original"
)

draw_graph(
    axes[0,1],
    pos1,
    edges1,
    path_edges1,
    'red',
    "Graph 1 : Path"
)

draw_graph(
    axes[0,2],
    pos1,
    edges1,
    closed_edges1,
    'green',
    "Graph 1 : Closed Walk"
)

draw_graph(
    axes[0,3],
    pos1,
    edges1,
    trail_edges1,
    'blue',
    "Graph 1 : Trail"
)

# ---------------- Graph 2 ----------------

draw_graph(
    axes[1,0],
    pos2,
    edges2,
    title="Graph 2 : Original"
)

draw_graph(
    axes[1,1],
    pos2,
    edges2,
    path_edges2,
    'red',
    "Graph 2 : Path"
)

draw_graph(
    axes[1,2],
    pos2,
    edges2,
    closed_edges2,
    'green',
    "Graph 2 : Closed Walk"
)

draw_graph(
    axes[1,3],
    pos2,
    edges2,
    trail_edges2,
    'blue',
    "Graph 2 : Trail"
)

plt.tight_layout()
plt.show()