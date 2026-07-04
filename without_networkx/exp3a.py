import matplotlib.pyplot as plt
pos = {
    1: (-2, 2),
    2: (0, 2),
    3: (-1, 0),
    4: (1, 0),
    5: (0, -2),
    6: (2, -2)
}
nodes = [1,2,3,4,5,6]
edges = [(1,2),(1,3),(2,3),(2,4),(3,5),(4,5),(5,6)]
def draw_graph(ax, nodes, edges, node_color='lightblue', title=''):
    # Draw nodes
    for n in nodes:
        x, y = pos[n]
        ax.plot(x, y, 'o', color=node_color, markersize=20, zorder=2)
        ax.text(x, y, str(n), fontsize=14, fontweight='bold', ha='center', va='center', zorder=3)
    
    # Draw edges
    for u, v in edges:
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        ax.plot([x1, x2], [y1, y2], color='black', linewidth=2, zorder=1)
    
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(title, fontsize=16)
fig, axes = plt.subplots(2,2, figsize=(14,12))
axes = axes.flatten()
draw_graph(axes[0], nodes, edges, node_color='lightblue', title="Original Graph")
subset_nodes = [1,2,3,4]
subset_edges = [e for e in edges if e[0] in subset_nodes and e[1] in subset_nodes]
draw_graph(axes[1], subset_nodes, subset_edges, node_color='lightgreen', title="Induced Subgraph")
spanning_edges = [(1,2),(2,4),(4,5),(5,6)]
draw_graph(axes[2], nodes, spanning_edges, node_color='orange', title="Spanning Subgraph")
edge_deleted = [e for e in edges if e != (2,3) and e != (3,2)]
draw_graph(axes[3], nodes, edge_deleted, node_color='pink', title="Edge Deleted Subgraph")

plt.tight_layout()
plt.show()