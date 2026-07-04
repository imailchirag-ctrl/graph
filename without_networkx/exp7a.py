import matplotlib.pyplot as plt

# Same graph as in the image
graph = {
    1: [(3,5), (2,14), (4,2)],

    2: [(1,14), (3,9), (4,8), (5,15)],

    3: [(1,5), (2,9), (5,13), (6,8)],

    4: [(1,2), (2,8), (5,10), (8,11)],

    5: [(2,15), (3,13), (4,10),
        (6,1), (7,7), (8,5)],

    6: [(3,8), (5,1), (7,10), (9,11)],

    7: [(5,7), (6,10), (8,0), (9,12)],

    8: [(4,11), (5,5), (7,0), (9,6)],

    9: [(6,11), (7,12), (8,6)]
}

# Node positions to match image
pos = {
    1: (-6, 0),

    3: (-3, 3),
    2: (-3, 0),
    4: (-3, -3),

    5: (0, 0),

    6: (3, 3),
    7: (3, 0),
    8: (3, -3),

    9: (6, 0)
}

# Dijkstra Algorithm with steps
def dijkstra_steps(graph, start):

    dist = {node: float('inf') for node in graph}
    visited = {node: False for node in graph}
    parent = {node: None for node in graph}

    dist[start] = 0

    steps = []

    for _ in range(len(graph)):

        min_node = None
        min_val = float('inf')

        for node in graph:
            if not visited[node] and dist[node] < min_val:
                min_val = dist[node]
                min_node = node

        visited[min_node] = True

        for neigh, w in graph[min_node]:

            if (not visited[neigh] and
                dist[min_node] + w < dist[neigh]):

                dist[neigh] = dist[min_node] + w
                parent[neigh] = min_node

        steps.append((min_node, dict(dist), dict(parent)))

    return steps

# Start node
steps = dijkstra_steps(graph, 1)

# Plotting
plt.figure(figsize=(18, 10))

for i, (current, dist, parent) in enumerate(steps):

    plt.subplot(3, 3, i + 1)

    # Draw all edges
    drawn = set()

    for node in graph:

        for neigh, w in graph[node]:

            if (neigh, node) not in drawn:

                x1, y1 = pos[node]
                x2, y2 = pos[neigh]

                plt.plot(
                    [x1, x2],
                    [y1, y2],
                    linestyle='dashed',
                    color='gray'
                )

                plt.text(
                    (x1 + x2) / 2,
                    (y1 + y2) / 2,
                    str(w),
                    fontsize=9
                )

                drawn.add((node, neigh))

    # Highlight shortest path tree
    for node in parent:

        if parent[node] is not None:

            x1, y1 = pos[node]
            x2, y2 = pos[parent[node]]

            plt.plot(
                [x1, x2],
                [y1, y2],
                color='blue',
                linewidth=3
            )

    # Draw nodes
    for node, (x, y) in pos.items():

        plt.scatter(x, y, s=700, color='red')

        d = dist[node]

        label = "∞" if d == float('inf') else str(d)

        plt.text(
            x,
            y,
            f"{node}\n{label}",
            ha='center',
            va='center',
            color='white',
            fontsize=10,
            fontweight='bold'
        )

    plt.title(f"Step {i+1}\nVisit Node {current}")

    plt.axis('off')

plt.tight_layout()

plt.show()