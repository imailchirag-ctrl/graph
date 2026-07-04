import matplotlib.pyplot as plt
import math
def is_graphical(sequence):
    seq = sorted(sequence, reverse=True)
    while True:
        seq = [x for x in seq if x > 0]
        if len(seq) == 0:
            return True
        seq.sort(reverse=True)
        d = seq.pop(0)
        if d > len(seq):
            return False
        for i in range(d):
            seq[i] -= 1
            if seq[i] < 0:
                return False
def construct_graph(sequence):
    if not is_graphical(sequence):
        print("Not a graphical sequence")
        return None, None
    n = len(sequence)
    nodes = list(range(n))
    degrees = sequence[:]
    edges = []
    while max(degrees) > 0:
        nodes_deg = sorted(zip(nodes, degrees), key=lambda x: x[1], reverse=True)
        u, d = nodes_deg[0]
        for i in range(1, d + 1):
            v = nodes_deg[i][0]
            edges.append((u, v))
            degrees[v] -= 1
        degrees[u] = 0
    return nodes, edges
def draw_graph(nodes, edges):
    n = len(nodes)
    angle = 2 * math.pi / n
    pos = {}
    for i in range(n):
        x = math.cos(i * angle)
        y = math.sin(i * angle)
        pos[i] = (x, y)
    for node, (x, y) in pos.items():
        plt.scatter(x, y)
        plt.text(x, y, str(node), fontsize=12, ha='center', va='center')
    for u, v in edges:
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        plt.plot([x1, x2], [y1, y2])
    plt.title("Graph Visualization")
    plt.axis('off')
    plt.show()
seq = [6,5,4,3,2,2,1,1]
nodes, edges = construct_graph(seq)
if nodes:
    print("Edges:", edges)
    draw_graph(nodes, edges)
