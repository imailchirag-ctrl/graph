import networkx as nx
import matplotlib.pyplot as plt

# ----- GRAPH -----
edges = [
    ('A','B',14),
    ('A','C',5),
    ('A','D',2),
    ('B','C',9),
    ('B','D',8),
    ('B','F',8),
    ('B','E',15),
    ('C','D',8),
    ('C','E',13),
    ('D','E',10),
    ('D','H',11),
    ('E','F',1),
    ('E','G',7),
    ('E','H',5),
    ('H','I',6),
    ('G','H',0),
    ('G','F',10),
    ('G','I',12),
    ('F','I',11)
]

G = nx.Graph()
G.add_weighted_edges_from(edges)

pos = {
    'A': (-3, 0),
    'B': (-2, 1),
    'C': (-2, 0),
    'D': (-2, -1),
    'E': (0, 0),
    'F': (2, 1),
    'G': (2, 0),
    'H': (2, -1),
    'I': (3, 0)
}

edges_sorted = sorted(edges, key=lambda x: x[2])

mst = nx.Graph()
steps = []
costs = []
total = 0

for u, v, w in edges_sorted:
    mst.add_edge(u, v, weight=w)

    if nx.is_forest(mst):
        total += w
        steps.append(list(mst.edges(data=True)))
        costs.append(total)
    else:
        mst.remove_edge(u, v)

plt.figure(figsize=(16, 12))

plt.subplot(3, 4, 1)
nx.draw(G, pos, with_labels=True,
        node_color='lightgray',
        edge_color='black', width=2)

labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

plt.title("Original Graph")

# MST STEPS
for i, step in enumerate(steps):
    plt.subplot(3, 4, i+2)

    # Draw original graph edges and nodes
    nx.draw(G, pos, with_labels=True,
            node_color='lightgray',
            edge_color='black', width=2)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    # Overlay MST edges in red
    H = nx.Graph()
    H.add_edges_from([(u, v) for u, v, _ in step])

    nx.draw(H, pos,
            node_color='lightblue',
            edge_color='red', width=3)

    step_labels = {(u, v): w['weight'] for u, v, w in step}
    nx.draw_networkx_edge_labels(H, pos, edge_labels=step_labels, font_color='red')

    plt.title(f"Step {i+1}\nCost = {costs[i]}")

plt.suptitle("Kruskal MST with Original Graph Background", fontsize=16)
plt.tight_layout()
plt.show()

print("MST edges:")
for u, v, w in mst.edges(data=True):
    print(f"{u}-{v} : {w['weight']}")

print("Total Cost:", total)