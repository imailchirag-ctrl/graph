import networkx as nx
import matplotlib.pyplot as plt

# Create figure with 2 rows and 2 columns
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# =====================================================
# GRAPH (c) ORIGINAL
# =====================================================

G1 = nx.Graph()

edges1 = [
    (1,2),
    (2,3),
    (3,4),
    (4,5),
    (4,1),
    (1,3),
    (5,2)
]

G1.add_edges_from(edges1)

pos1 = {
    1:(0,2),
    2:(2,1),
    3:(1,0),
    4:(-1,0),
    5:(-2,1)
}

nx.draw(
    G1,
    pos1,
    ax=axes[0,0],
    with_labels=True,
    node_color='lightblue',
    node_size=1000,
    font_size=12
)

axes[0,0].set_title("Graph (c) - Original")


# =====================================================
# GRAPH (c) HAMILTONIAN
# =====================================================

cycle1 = [(1,2), (2,5), (5,4), (4,3), (3,1)]

nx.draw(
    G1,
    pos1,
    ax=axes[0,1],
    with_labels=True,
    node_color='lightgreen',
    node_size=1000,
    font_size=12,
    edge_color='gray'
)

nx.draw_networkx_edges(
    G1,
    pos1,
    edgelist=cycle1,
    edge_color='red',
    width=3,
    ax=axes[0,1]
)

axes[0,1].set_title("Graph (c) - Hamiltonian Cycle")


# =====================================================
# GRAPH (d) ORIGINAL
# =====================================================

G2 = nx.Graph()

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

G2.add_edges_from(edges2)

pos2 = {
    7:(-2,2),
    1:(0,3),
    6:(-3,0),
    4:(0,-1),
    5:(-2,-2),
    2:(2,1),
    3:(3,-1)
}

nx.draw(
    G2,
    pos2,
    ax=axes[1,0],
    with_labels=True,
    node_color='orange',
    node_size=1000,
    font_size=12
)

axes[1,0].set_title("Graph (d) - Original")


# =====================================================
# GRAPH (d) HAMILTONIAN
# =====================================================

cycle2 = [(7,1), (1,6), (6,4), (4,5), (5,2), (2,3), (3,7)]

nx.draw(
    G2,
    pos2,
    ax=axes[1,1],
    with_labels=True,
    node_color='pink',
    node_size=1000,
    font_size=12,
    edge_color='gray'
)

nx.draw_networkx_edges(
    G2,
    pos2,
    edgelist=cycle2,
    edge_color='red',
    width=3,
    ax=axes[1,1]
)

axes[1,1].set_title("Graph (d) - Hamiltonian Cycle")


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