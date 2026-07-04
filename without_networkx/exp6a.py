import matplotlib.pyplot as plt

# =====================================================
# GRAPH DATA
# =====================================================

edges = [
    ('A', 'B', 14),
    ('A', 'C', 5),
    ('A', 'D', 2),
    ('B', 'C', 9),
    ('B', 'D', 8),
    ('B', 'F', 8),
    ('B', 'E', 15),
    ('C', 'D', 8),
    ('C', 'E', 13),
    ('D', 'E', 10),
    ('D', 'H', 11),
    ('E', 'F', 1),
    ('E', 'G', 7),
    ('E', 'H', 5),
    ('H', 'I', 6),
    ('G', 'H', 0),
    ('G', 'F', 10),
    ('G', 'I', 12),
    ('F', 'I', 11)
]

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

# =====================================================
# DFS (cycle detection WITHOUT find / nx)
# =====================================================

def dfs(u, target, visited, graph):
    if u == target:
        return True

    visited.add(u)

    i = 0
    while i < len(graph[u]):
        v = graph[u][i]

        if v not in visited:
            if dfs(v, target, visited, graph):
                return True

        i = i + 1

    return False


# =====================================================
# BUILD GRAPH STRUCTURE
# =====================================================

vertices = []
i = 0

while i < len(edges):
    if edges[i][0] not in vertices:
        vertices.append(edges[i][0])
    if edges[i][1] not in vertices:
        vertices.append(edges[i][1])
    i = i + 1


def get_weight(e):
    return e[2]


edges_sorted = list(edges)
edges_sorted.sort(key=get_weight)

graph = {}
i = 0

while i < len(vertices):
    graph[vertices[i]] = []
    i = i + 1

# =====================================================
# KRUSKAL MST (NO find, NO nx)
# =====================================================

mst = []
total_cost = 0

i = 0
while i < len(edges_sorted):

    u = edges_sorted[i][0]
    v = edges_sorted[i][1]
    w = edges_sorted[i][2]

    visited = set()
    has_cycle = dfs(u, v, visited, graph)

    if has_cycle == False:

        mst.append((u, v, w))
        total_cost = total_cost + w

        graph[u].append(v)
        graph[v].append(u)

    i = i + 1


# =====================================================
# DRAW FINAL MST (ONLY)
# =====================================================

def draw_node(x, y, label):
    plt.scatter(x, y, s=600, color='lightgray', edgecolors='black')
    plt.text(x, y, label, ha='center', va='center', fontweight='bold')


def draw_edge(u, v, color='black', width=2):
    x1, y1 = pos[u]
    x2, y2 = pos[v]
    plt.plot([x1, x2], [y1, y2], color=color, linewidth=width)


# draw all nodes
i = 0
while i < len(vertices):
    node = vertices[i]
    draw_node(pos[node][0], pos[node][1], node)
    i = i + 1

# draw all original edges (light background)
i = 0
while i < len(edges):
    draw_edge(edges[i][0], edges[i][1], color='gray', width=1)
    i = i + 1

# draw MST edges (highlight)
i = 0
while i < len(mst):
    draw_edge(mst[i][0], mst[i][1], color='red', width=3)
    i = i + 1

# edge labels
i = 0
while i < len(edges):
    u, v, w = edges[i]
    x1, y1 = pos[u]
    x2, y2 = pos[v]
    plt.text((x1+x2)/2, (y1+y2)/2, str(w), fontsize=8, ha='center')
    i = i + 1

plt.title("Final Minimum Spanning Tree (No NetworkX)", fontweight='bold')
plt.axis('off')
plt.show()

# =====================================================
# OUTPUT MST
# =====================================================

print("\nMST Edges:")
i = 0
while i < len(mst):
    print(mst[i][0], "-", mst[i][1], ":", mst[i][2])
    i = i + 1

print("\nTotal Cost =", total_cost)