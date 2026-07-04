import matplotlib.pyplot as plt
import networkx as nx

# =========================================================
# CHECK EULERIAN
# =========================================================

def is_eulerian(G):
    return nx.is_connected(G) and all(deg % 2 == 0 for node, deg in G.degree())


def draw_initial(G1, pos1, G2, pos2):

    fig, axes = plt.subplots(1, 2, figsize=(12,5))

    nx.draw(
        G1,
        pos1,
        ax=axes[0],
        with_labels=True,
        node_color="lightblue",
        node_size=700,
        width=2
    )

    axes[0].set_title("Graph 1")

    nx.draw(
        G2,
        pos2,
        ax=axes[1],
        with_labels=True,
        node_color="lightgreen",
        node_size=700,
        width=2
    )

    axes[1].set_title("Graph 2")

    plt.tight_layout()
    plt.show()

# =========================================================
# DRAW STEP BY STEP EULER PATH
# =========================================================

def draw_steps_small(G, pos, path, title):

    edges = list(zip(path, path[1:]))
    n = len(edges)

    cols = 4
    rows = (n // cols) + (n % cols > 0)

    fig, axes = plt.subplots(rows, cols, figsize=(14, 3*rows))

    axes = axes.flatten()

    for i in range(n):

        ax = axes[i]

        # Draw full graph
        nx.draw(
            G,
            pos,
            ax=ax,
            with_labels=True,
            node_color="lightgray",
            node_size=600,
            edge_color="gray",
            width=1.5
        )

        # Highlight traversed edges
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=edges[:i+1],
            edge_color='red',
            width=4,
            ax=ax
        )

        ax.set_title(f"Step {i+1}", fontsize=10)

        ax.axis('off')

    # Hide extra empty boxes
    for j in range(n, len(axes)):
        axes[j].axis('off')

    fig.suptitle(title, fontsize=14)

    plt.tight_layout()
    plt.show()

# =========================================================
# GRAPH 1  (FROM YOUR FIRST CODE)
# =========================================================

G1 = nx.Graph()

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

G1.add_edges_from(edges1)

pos1 = {
    'A': (0,1),
    'B': (1,2),
    'C': (1,0),
    'D': (2,1),
    'E': (3,2),
    'F': (3,0)
}

# =========================================================
# GRAPH 2  (FROM YOUR FIRST CODE)
# =========================================================

G2 = nx.Graph()

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

G2.add_edges_from(edges2)

pos2 = {
    'A': (0,1),
    'B': (1,2),
    'C': (1,0),
    'D': (2,1),
    'E': (3,2),
    'F': (3,0),
    'G': (4,1)
}

# =========================================================
# SHOW ORIGINAL GRAPHS
# =========================================================

draw_initial(G1, pos1, G2, pos2)

# =========================================================
# GRAPH 1 EULER CHECK
# =========================================================

print("GRAPH 1")

if is_eulerian(G1):

    print("Eulerian Circuit EXISTS")

    circuit1 = list(nx.eulerian_circuit(G1))

    print("Euler Circuit:")
    print(circuit1)

    path1 = [circuit1[0][0]]

    for u, v in circuit1:
        path1.append(v)

    print("Traversal Path:")
    print(path1)

    draw_steps_small(G1, pos1, path1, "Graph 1 Euler Circuit Steps")

else:
    print("NOT Eulerian")

# =========================================================
# GRAPH 2 EULER CHECK
# =========================================================

print("\nGRAPH 2")

if is_eulerian(G2):

    print("Eulerian Circuit EXISTS")

    circuit2 = list(nx.eulerian_circuit(G2))

    print("Euler Circuit:")
    print(circuit2)

    path2 = [circuit2[0][0]]

    for u, v in circuit2:
        path2.append(v)

    print("Traversal Path:")
    print(path2)

    draw_steps_small(G2, pos2, path2, "Graph 2 Euler Circuit Steps")

else:
    print("NOT Eulerian")