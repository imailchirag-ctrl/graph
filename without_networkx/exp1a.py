import matplotlib.pyplot as plt
def draw_graph(ax, nodes, edges, positions, color, title):
    for (u, v) in edges:
        x = [positions[u][0], positions[v][0]]
        y = [positions[u][1], positions[v][1]]
        ax.plot(x, y)
    for node in nodes:
        x, y = positions[node]
        ax.scatter(x, y, s=800, c=color)
        ax.text(x, y, str(node), ha='center', va='center', color='black')
    ax.set_title(title)
    ax.axis('off')
plt.figure(figsize=(12, 8))
nodes1 = [1, 2, 3, 4, 5]
edges1 = [(1,2), (2,3), (3,4), (4,5)]
pos1 = {1:(0,0), 2:(1,0), 3:(2,0), 4:(3,0), 5:(4,0)}
ax1 = plt.subplot(2,2,1)
draw_graph(ax1, nodes1, edges1, pos1, 'grey', "P5 - Path Graph")
nodes2 = [1,2,3,4,5]
edges2 = [(1,2),(2,3),(3,4),(4,5),(5,1)]
pos2 = {
    1:(0,1), 2:(1,2), 3:(2,1.5),
    4:(1.5,0.5), 5:(0.5,0.5)
}
ax2 = plt.subplot(2,2,2)
draw_graph(ax2, nodes2, edges2, pos2, 'red', "C5 - Cycle Graph")
nodes3 = [1,2,3,4,5]
edges3 = [(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)]
pos3 = {
    1:(0,1), 2:(0,-1),
    3:(2,2), 4:(2,0), 5:(2,-2)
}
ax3 = plt.subplot(2,2,3)
draw_graph(ax3, nodes3, edges3, pos3, 'blue', "K2,3 - Complete Bipartite Graph")
nodes4 = [1,2,3,4,5]
edges4 = [(1,2),(1,3),(1,4),(1,5),
          (2,3),(2,4),(2,5),
          (3,4),(3,5),
          (4,5)]
pos4 = {
    1:(0,1), 2:(1,2), 3:(2,1),
    4:(1.5,0), 5:(0.5,0)
}
ax4 = plt.subplot(2,2,4)
draw_graph(ax4, nodes4, edges4, pos4, 'yellow', "K5 - Complete Graph")
plt.tight_layout()
plt.show()