import networkx as nx
import matplotlib.pyplot as plt
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
path1 = ['A','B','D','E']
path_edges1 = list(zip(path1[:-1], path1[1:]))

closed1 = ['A','B','C','A']
closed_edges1 = list(zip(closed1[:-1], closed1[1:]))

trail1 = ['A','C','D','F','E','B']
trail_edges1 = list(zip(trail1[:-1], trail1[1:]))


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

    # Extra edge C-F
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

path2 = ['A','B','D','E','G']
path_edges2 = list(zip(path2[:-1], path2[1:]))

closed2 = ['E','G','F','E']
closed_edges2 = list(zip(closed2[:-1], closed2[1:]))

trail2 = ['A','B','E','G','F','C','D']
trail_edges2 = list(zip(trail2[:-1], trail2[1:]))


fig, axes = plt.subplots(2, 4, figsize=(24, 10))


nx.draw(
    G1,
    pos1,
    with_labels=True,
    node_color='black',
    node_size=700,
    font_color='white',
    width=2,
    ax=axes[0,0]
)

axes[0,0].set_title("Graph 1 : Original")


nx.draw(
    G1,
    pos1,
    with_labels=True,
    node_color='black',
    node_size=700,
    font_color='white',
    edge_color='gray',
    width=1.5,
    ax=axes[0,1]
)

nx.draw_networkx_edges(
    G1,
    pos1,
    edgelist=path_edges1,
    edge_color='red',
    width=4,
    ax=axes[0,1]
)

axes[0,1].set_title("Graph 1 : Path")


nx.draw(
    G1,
    pos1,
    with_labels=True,
    node_color='black',
    node_size=700,
    font_color='white',
    edge_color='gray',
    width=1.5,
    ax=axes[0,2]
)

nx.draw_networkx_edges(
    G1,
    pos1,
    edgelist=closed_edges1,
    edge_color='green',
    width=4,
    ax=axes[0,2]
)

axes[0,2].set_title("Graph 1 : Closed Walk")


nx.draw(
    G1,
    pos1,
    with_labels=True,
    node_color='black',
    node_size=700,
    font_color='white',
    edge_color='gray',
    width=1.5,
    ax=axes[0,3]
)

nx.draw_networkx_edges(
    G1,
    pos1,
    edgelist=trail_edges1,
    edge_color='blue',
    width=4,
    ax=axes[0,3]
)
axes[0,3].set_title("Graph 1 : Trail")
nx.draw(
    G2,
    pos2,
    with_labels=True,
    node_color='black',
    node_size=700,
    font_color='white',
    width=2,
    ax=axes[1,0]
)
axes[1,0].set_title("Graph 2 : Original")
nx.draw(
    G2,
    pos2,
    with_labels=True,
    node_color='black',
    node_size=700,
    font_color='white',
    edge_color='gray',
    width=1.5,
    ax=axes[1,1]
)

nx.draw_networkx_edges(
    G2,
    pos2,
    edgelist=path_edges2,
    edge_color='red',
    width=4,
    ax=axes[1,1]
)

axes[1,1].set_title("Graph 2 : Path")

nx.draw(
    G2,
    pos2,
    with_labels=True,
    node_color='black',
    node_size=700,
    font_color='white',
    edge_color='gray',
    width=1.5,
    ax=axes[1,2]
)

nx.draw_networkx_edges(
    G2,
    pos2,
    edgelist=closed_edges2,
    edge_color='green',
    width=4,
    ax=axes[1,2]
)

axes[1,2].set_title("Graph 2 : Closed Walk")
nx.draw(
    G2,
    pos2,
    with_labels=True,
    node_color='black',
    node_size=700,
    font_color='white',
    edge_color='gray',
    width=1.5,
    ax=axes[1,3]
)

nx.draw_networkx_edges(
    G2,
    pos2,
    edgelist=trail_edges2,
    edge_color='blue',
    width=4,
    ax=axes[1,3]
)

axes[1,3].set_title("Graph 2 : Trail")
plt.tight_layout()
plt.show()

