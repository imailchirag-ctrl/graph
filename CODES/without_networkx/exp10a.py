import matplotlib.pyplot as plt

# =====================================================
# FUNCTION TO DRAW GRAPH
# =====================================================

def draw_graph(ax, pos, edges,
               node_color='lightblue',
               highlight_edges=None,
               title=""):

    # Draw all edges
    for u, v in edges:
        x = [pos[u][0], pos[v][0]]
        y = [pos[u][1], pos[v][1]]

        ax.plot(
            x, y,
            color='gray',
            linewidth=2,
            zorder=1
        )

    # Draw highlighted Hamiltonian cycle
    if highlight_edges:
        for u, v in highlight_edges:

            x = [pos[u][0], pos[v][0]]
            y = [pos[u][1], pos[v][1]]

            ax.plot(
                x, y,
                color='red',
                linewidth=4,
                zorder=2
            )

    # Draw nodes
    for node, (x, y) in pos.items():

        ax.scatter(
            x,
            y,
            s=1000,
            color=node_color,
            edgecolors='black',
            zorder=3
        )

        ax.text(
            x,
            y,
            str(node),
            fontsize=12,
            fontweight='bold',
            ha='center',
            va='center',
            zorder=4
        )

    ax.set_title(title)
    ax.axis('off')


# =====================================================
# CREATE FIGURE
# =====================================================

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# =====================================================
# GRAPH (c)
# =====================================================

edges1 = [
    (1,2),
    (2,3),
    (3,4),
    (4,5),
    (4,1),
    (1,3),
    (5,2)
]

pos1 = {
    1:(0,2),
    2:(2,1),
    3:(1,0),
    4:(-1,0),
    5:(-2,1)
}

# Original Graph
draw_graph(
    axes[0,0],
    pos1,
    edges1,
    node_color='lightblue',
    title="Graph (c) - Original"
)

# Hamiltonian Cycle
cycle1 = [
    (1,2),
    (2,5),
    (5,4),
    (4,3),
    (3,1)
]

draw_graph(
    axes[0,1],
    pos1,
    edges1,
    node_color='lightgreen',
    highlight_edges=cycle1,
    title="Graph (c) - Hamiltonian Cycle"
)

# =====================================================
# GRAPH (d)
# =====================================================

edges2 = [
    (7,1),
    (1,6),
    (6,4),
    (4,5),
    (5,2),
    (2,3),
    (3,4),
    (3,7)
]

pos2 = {
    7:(-2,2),
    1:(0,3),
    6:(-3,0),
    4:(0,-1),
    5:(-2,-2),
    2:(2,1),
    3:(3,-1)
}

# Original Graph
draw_graph(
    axes[1,0],
    pos2,
    edges2,
    node_color='orange',
    title="Graph (d) - Original"
)

# Hamiltonian Cycle
cycle2 = [
    (7,1),
    (1,6),
    (6,4),
    (4,5),
    (5,2),
    (2,3),
    (3,7)
]

draw_graph(
    axes[1,1],
    pos2,
    edges2,
    node_color='pink',
    highlight_edges=cycle2,
    title="Graph (d) - Hamiltonian Cycle"
)

# =====================================================

plt.tight_layout()
plt.show()

# =====================================================
# STEP-BY-STEP OUTPUT
# =====================================================

print("GRAPH (c)")

cycle_c = [1,2,5,4,3,1]

for i in range(len(cycle_c)-1):
    print(f"Step {i+1}: {cycle_c[i]} -> {cycle_c[i+1]}")

print("\nGRAPH (d)")

cycle_d = [7,1,6,4,5,2,3,7]

for i in range(len(cycle_d)-1):
    print(f"Step {i+1}: {cycle_d[i]} -> {cycle_d[i+1]}")