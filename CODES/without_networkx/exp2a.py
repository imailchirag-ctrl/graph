import matplotlib.pyplot as plt
import math

# =====================================================
# HELPER FUNCTIONS
# =====================================================

def draw_graph(ax, pos, edges, title):

    for u, v in edges:
        ax.plot(
            [pos[u][0], pos[v][0]],
            [pos[u][1], pos[v][1]],
            'k',
            linewidth=2
        )

    for node in pos:
        ax.scatter(
            pos[node][0],
            pos[node][1],
            s=250,
            color='black'
        )

        ax.text(
            pos[node][0],
            pos[node][1],
            str(node),
            color='white',
            ha='center',
            va='center',
            fontsize=8
        )

    ax.set_title(title)
    ax.axis('equal')
    ax.axis('off')


def degree_sequence(vertices, edges):

    deg = {v: 0 for v in vertices}

    for u, v in edges:
        deg[u] += 1
        deg[v] += 1

    return sorted(deg.values())


def isomorphic(vertices1, edges1, vertices2, edges2):

    if len(vertices1) != len(vertices2):
        return False

    if len(edges1) != len(edges2):
        return False

    return (
        degree_sequence(vertices1, edges1)
        ==
        degree_sequence(vertices2, edges2)
    )

# =====================================================
# PAIR 0
# =====================================================

vertices0 = list(range(9))

octagon_edges = [
    (0,1),(1,2),(2,3),(3,4),
    (4,5),(5,6),(6,7),(7,0)
]

center_edges = [
    (8,0),(8,1),(8,2),(8,3),
    (8,4),(8,5),(8,6),(8,7)
]

extra_edges = [
    (0,2),(0,6),
    (1,3),(1,7),
    (2,4),
    (3,5),
    (4,6),
    (5,7)
]

edges0A = octagon_edges + center_edges + extra_edges
edges0B = octagon_edges + center_edges + extra_edges

pos0A = {}

for i in range(8):
    angle = 2 * math.pi * i / 8 + math.pi/8
    pos0A[i] = (
        math.cos(angle),
        math.sin(angle)
    )

pos0A[8] = (0,0)

pos0B = {}

for i in range(8):
    angle = 2 * math.pi * i / 8
    pos0B[i] = (
        math.cos(angle),
        math.sin(angle)
    )

pos0B[8] = (0,0)

# =====================================================
# PAIR 1
# =====================================================

vertices1A = [1,2,3,4,5]
vertices1B = ['a','b','c','d','e']

edges1A = [
    (1,2),(2,3),(3,4),(4,5),(5,1)
]

edges1B = [
    ('a','c'),
    ('c','e'),
    ('e','b'),
    ('b','d'),
    ('d','a')
]

pos1A = {
    1:(0,1),
    2:(1,2),
    3:(2,1.5),
    4:(1.7,0),
    5:(0.3,0)
}

pos1B = {
    'a':(-1,1),
    'b':(0,1),
    'c':(1,0),
    'd':(0,-1),
    'e':(-1,-1)
}

# =====================================================
# PAIR 2
# =====================================================

vertices2 = [1,2,3,4,5,6,7,8]

edges2A = [
    (1,2),(2,3),(3,4),(4,1),
    (5,6),(6,7),(7,8),(8,5),
    (1,5),(4,7)
]

edges2B = [
    (1,2),(2,3),(3,4),(4,1),
    (5,6),(6,7),(7,8),(8,5),
    (1,5),(4,8)
]

pos2 = {
    1:(-2,2),
    2:(2,2),
    3:(2,-2),
    4:(-2,-2),
    5:(-1,1),
    6:(1,1),
    7:(1,-1),
    8:(-1,-1)
}

# =====================================================
# DRAW ALL 6 GRAPHS
# =====================================================

fig, ax = plt.subplots(3, 2, figsize=(14,12))

draw_graph(ax[0,0], pos0A, edges0A, "Pair 0 - Graph A")
draw_graph(ax[0,1], pos0B, edges0B, "Pair 0 - Graph B")

draw_graph(ax[1,0], pos1A, edges1A, "Pair 1 - Pentagon")
draw_graph(ax[1,1], pos1B, edges1B, "Pair 1 - Star")

draw_graph(ax[2,0], pos2, edges2A, "Pair 2 - Graph A")
draw_graph(ax[2,1], pos2, edges2B, "Pair 2 - Graph B")

plt.tight_layout()
plt.show()

# =====================================================
# RESULTS
# =====================================================

print("\n========== ISOMORPHISM RESULTS ==========\n")

print("Pair 0:")
if isomorphic(vertices0, edges0A, vertices0, edges0B):
    print("Graphs ARE ISOMORPHIC")
else:
    print("Graphs ARE NOT ISOMORPHIC")

print("\n-----------------------------\n")

print("Pair 1:")
if isomorphic(vertices1A, edges1A, vertices1B, edges1B):
    print("Graphs ARE ISOMORPHIC")
else:
    print("Graphs ARE NOT ISOMORPHIC")

print("\n-----------------------------\n")

print("Pair 2:")
if isomorphic(vertices2, edges2A, vertices2, edges2B):
    print("Graphs ARE ISOMORPHIC")
else:
    print("Graphs ARE NOT ISOMORPHIC")