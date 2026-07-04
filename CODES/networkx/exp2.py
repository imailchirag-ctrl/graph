import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import math

plt.figure(figsize=(15, 12))

# =====================================================
# PAIR 0 (ISOMORPHIC)
# =====================================================

G0A = nx.Graph()
G0B = nx.Graph()

# Outer octagon
octagon_edges = [
    (0,1),(1,2),(2,3),(3,4),
    (4,5),(5,6),(6,7),(7,0)
]

# Center connections
center_edges = [
    (8,0),(8,1),(8,2),(8,3),
    (8,4),(8,5),(8,6),(8,7)
]

# Extra edges
extra_edges = [
    (0,2),(0,6),
    (1,3),(1,7),
    (2,4),
    (3,5),
    (4,6),
    (5,7)
]

for G in [G0A, G0B]:
    G.add_nodes_from(range(9))
    G.add_edges_from(octagon_edges)
    G.add_edges_from(center_edges)
    G.add_edges_from(extra_edges)

# -----------------------------
# Graph A Layout
# -----------------------------

pos_left = {}

for i in range(8):
    angle = 2 * math.pi * i / 8 + math.pi / 8
    pos_left[i] = (math.cos(angle), math.sin(angle))

pos_left[8] = (0, 0)

# -----------------------------
# Graph B Layout
# -----------------------------

pos_right = {}

for i in range(8):
    angle = 2 * np.pi * i / 8
    pos_right[i] = (np.cos(angle), np.sin(angle))

pos_right[8] = (0, 0)

plt.subplot(3, 2, 1)
nx.draw(
    G0A,
    pos_left,
    with_labels=False,
    node_size=400,
    width=2,
    node_color="black"
)
plt.title("Pair 0 - Graph A")

plt.subplot(3, 2, 2)
nx.draw(
    G0B,
    pos_right,
    with_labels=False,
    node_size=400,
    width=2,
    node_color="black"
)
plt.title("Pair 0 - Graph B")

# =====================================================
# PAIR 1 (PENTAGON vs STAR)
# =====================================================

G1 = nx.Graph()
G2 = nx.Graph()

G1.add_edges_from([
    (1,2),(2,3),(3,4),(4,5),(5,1)
])

G2.add_edges_from([
    ('a','c'),
    ('c','e'),
    ('e','b'),
    ('b','d'),
    ('d','a')
])

pos_star = {
    'a': (-1,1),
    'b': (0,1),
    'c': (1,0),
    'd': (0,-1),
    'e': (-1,-1)
}

plt.subplot(3, 2, 3)
nx.draw(
    G1,
    with_labels=True,
    node_size=800
)
plt.title("Pair 1 - Pentagon")

plt.subplot(3, 2, 4)
nx.draw(
    G2,
    pos_star,
    with_labels=True,
    node_size=800
)
plt.title("Pair 1 - Star")

# =====================================================
# PAIR 2 (NON-ISOMORPHIC)
# =====================================================

G3 = nx.Graph()
G4 = nx.Graph()

G3.add_edges_from([
    (1,2),(2,3),(3,4),(4,1),
    (5,6),(6,7),(7,8),(8,5),
    (1,5),(4,7)
])

G4.add_edges_from([
    (1,2),(2,3),(3,4),(4,1),
    (5,6),(6,7),(7,8),(8,5),
    (1,5),(4,8)
])

pos_common = {
    1: (-2,2),
    2: (2,2),
    3: (2,-2),
    4: (-2,-2),
    5: (-1,1),
    6: (1,1),
    7: (1,-1),
    8: (-1,-1)
}

plt.subplot(3, 2, 5)
nx.draw(
    G3,
    pos_common,
    with_labels=True,
    node_size=800
)
plt.title("Pair 2 - Graph A")

plt.subplot(3, 2, 6)
nx.draw(
    G4,
    pos_common,
    with_labels=True,
    node_size=800
)
plt.title("Pair 2 - Graph B")

plt.tight_layout()
plt.show()

# =====================================================
# ISOMORPHISM CHECKS
# =====================================================

print("\n========== ISOMORPHISM RESULTS ==========\n")

GM0 = nx.isomorphism.GraphMatcher(G0A, G0B)

print("Pair 0:")
if GM0.is_isomorphic():
    print("Graphs ARE ISOMORPHIC")
    print("Mapping =", GM0.mapping)
else:
    print("Graphs ARE NOT ISOMORPHIC")

print("\n-----------------------------\n")

GM1 = nx.isomorphism.GraphMatcher(G1, G2)

print("Pair 1:")
if GM1.is_isomorphic():
    print("Graphs ARE ISOMORPHIC")
    print("Mapping =", GM1.mapping)
else:
    print("Graphs ARE NOT ISOMORPHIC")

print("\n-----------------------------\n")

GM2 = nx.isomorphism.GraphMatcher(G3, G4)

print("Pair 2:")
if GM2.is_isomorphic():
    print("Graphs ARE ISOMORPHIC")
    print("Mapping =", GM2.mapping)
else:
    print("Graphs ARE NOT ISOMORPHIC")