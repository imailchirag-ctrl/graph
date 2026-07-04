
import matplotlib.pyplot as plt

class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):

        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    def degree(self, node):
        return len(self.graph[node])

def dfs(graph, node, visited):

    visited.add(node)

    for neighbour in graph.graph[node]:

        if neighbour not in visited:
            dfs(graph, neighbour, visited)

def is_connected(graph):

    visited = set()

    start = list(graph.graph.keys())[0]

    dfs(graph, start, visited)

    return len(visited) == len(graph.graph)

def is_eulerian(graph):

    if not is_connected(graph):
        return False

    for node in graph.graph:

        if graph.degree(node) % 2 != 0:
            return False

    return True

def remove_edge(graph, u, v):

    graph.graph[u].remove(v)
    graph.graph[v].remove(u)

def add_edge(graph, u, v):

    graph.graph[u].append(v)
    graph.graph[v].append(u)

def dfs_count(graph, node, visited):

    visited.add(node)

    count = 1

    for neighbour in graph.graph[node]:

        if neighbour not in visited:
            count += dfs_count(graph, neighbour, visited)

    return count

def is_valid_next_edge(graph, u, v):

    if len(graph.graph[u]) == 1:
        return True

    visited1 = set()
    count1 = dfs_count(graph, u, visited1)

    remove_edge(graph, u, v)

    visited2 = set()
    count2 = dfs_count(graph, u, visited2)

    add_edge(graph, u, v)

    return count1 == count2

def fleury(graph):

    start = list(graph.graph.keys())[0]

    path = [start]

    current = start

    while True:

        if len(graph.graph[current]) == 0:
            break

        for neighbour in graph.graph[current]:

            if is_valid_next_edge(graph, current, neighbour):

                path.append(neighbour)

                remove_edge(graph, current, neighbour)

                current = neighbour

                break

    return path

def draw_graph(graph, pos, title):

    plt.figure(figsize=(6,5))

    for u in graph.graph:

        for v in graph.graph[u]:

            x1, y1 = pos[u]
            x2, y2 = pos[v]

            plt.plot([x1, x2], [y1, y2], 'gray')

    for node in pos:

        x, y = pos[node]

        plt.scatter(x, y, s=1000, color='black')

        plt.text(x, y, node,
                 color='white',
                 fontsize=12,
                 ha='center',
                 va='center')

    plt.title(title)

    plt.axis('off')

    plt.show()

def draw_steps(graph_original, pos, path, title):

    edges = list(zip(path[:-1], path[1:]))

    n = len(edges)

    cols = 4
    rows = (n // cols) + (n % cols > 0)

    fig, axes = plt.subplots(rows, cols, figsize=(14, 3*rows))

    axes = axes.flatten()

    for i in range(n):

        ax = axes[i]

        for u in graph_original.graph:

            for v in graph_original.graph[u]:

                x1, y1 = pos[u]
                x2, y2 = pos[v]

                ax.plot([x1, x2], [y1, y2], color='lightgray')

        for j in range(i+1):

            u, v = edges[j]

            x1, y1 = pos[u]
            x2, y2 = pos[v]

            ax.plot([x1, x2], [y1, y2],
                    color='red',
                    linewidth=3)

        for node in pos:

            x, y = pos[node]

            ax.scatter(x, y, s=700, color='black')

            ax.text(x, y, node,
                    color='white',
                    fontsize=10,
                    ha='center',
                    va='center')

        ax.set_title(f"Step {i+1}")

        ax.axis('off')

    for j in range(n, len(axes)):
        axes[j].axis('off')

    fig.suptitle(title)

    plt.tight_layout()

    plt.show()

G1 = Graph()

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

for u, v in edges1:
    G1.add_edge(u, v)

pos1 = {
    'A': (0,1),
    'B': (1,2),
    'C': (1,0),
    'D': (2,1),
    'E': (3,2),
    'F': (3,0)
}

G2 = Graph()

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

for u, v in edges2:
    G2.add_edge(u, v)

pos2 = {
    'A': (0,1),
    'B': (1,2),
    'C': (1,0),
    'D': (2,1),
    'E': (3,2),
    'F': (3,0),
    'G': (4,1)
}

draw_graph(G1, pos1, "Graph 1")

if is_eulerian(G1):

    print("Graph 1 Eulerian")

    path1 = fleury(G1)

    print(path1)

    G1_draw = Graph()

    for u, v in edges1:
        G1_draw.add_edge(u, v)

    draw_steps(G1_draw, pos1, path1, "Graph 1 Fleury Steps")

else:
    print("Graph 1 Not Eulerian")

draw_graph(G2, pos2, "Graph 2")

if is_eulerian(G2):

    print("Graph 2 Eulerian")

    path2 = fleury(G2)

    print(path2)

    G2_draw = Graph()

    for u, v in edges2:
        G2_draw.add_edge(u, v)

    draw_steps(G2_draw, pos2, path2, "Graph 2 Fleury Steps")

else:
    print("Graph 2 Not Eulerian")
