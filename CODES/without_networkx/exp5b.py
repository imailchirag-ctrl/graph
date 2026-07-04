import matplotlib.pyplot as plt
import math

# Input number of vertices
n = int(input("Enter number of vertices: "))

# Input adjacency matrix
print("Enter adjacency matrix:")
adj_matrix = []

for i in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

# Vertex labels A, B, C...
labels = []
for i in range(n):
    labels.append(chr(65 + i))

# Find edges of original graph
edges = []

for i in range(n):
    for j in range(i + 1, n):
        if adj_matrix[i][j] == 1:
            edges.append((labels[i], labels[j]))

print("\nEdges of Original Graph:")
print(edges)

# Vertices of line graph = edges of original graph
line_vertices = edges.copy()
m = len(line_vertices)

# Create adjacency matrix for line graph
line_adj_matrix = [[0] * m for _ in range(m)]

for i in range(m):
    for j in range(i + 1, m):

        e1 = line_vertices[i]
        e2 = line_vertices[j]

        # Adjacent if they share a common vertex
        if (e1[0] in e2) or (e1[1] in e2):
            line_adj_matrix[i][j] = 1
            line_adj_matrix[j][i] = 1

print("\nVertices of Line Graph:")
print(line_vertices)

print("\nAdjacency Matrix of Line Graph:")
for row in line_adj_matrix:
    print(row)

# =====================================================
# Draw Original Graph
# =====================================================

pos_original = {}

for i in range(n):
    angle = 2 * math.pi * i / n
    pos_original[labels[i]] = (
        math.cos(angle),
        math.sin(angle)
    )

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.title("Original Graph")

# Draw edges
for (u, v) in edges:
    x = [pos_original[u][0], pos_original[v][0]]
    y = [pos_original[u][1], pos_original[v][1]]
    plt.plot(x, y, 'k-')

# Draw vertices
for node, (x, y) in pos_original.items():
    plt.scatter(x, y, s=300)
    plt.text(x, y, node,
             fontsize=12,
             ha='center',
             va='center',
             color='white')

plt.axis('off')

# =====================================================
# Draw Line Graph
# =====================================================

plt.subplot(1, 2, 2)
plt.title("Line Graph")

pos_line = {}

for i in range(m):
    angle = 2 * math.pi * i / m
    pos_line[i] = (
        math.cos(angle),
        math.sin(angle)
    )

# Draw edges of line graph
for i in range(m):
    for j in range(i + 1, m):

        if line_adj_matrix[i][j] == 1:
            x = [pos_line[i][0], pos_line[j][0]]
            y = [pos_line[i][1], pos_line[j][1]]
            plt.plot(x, y, 'k-')

# Draw vertices of line graph
for i, (x, y) in pos_line.items():
    plt.scatter(x, y, s=300)

    plt.text(
        x,
        y,
        str(line_vertices[i]),
        fontsize=8,
        ha='center',
        va='center'
    )

plt.axis('off')

plt.tight_layout()
plt.show()