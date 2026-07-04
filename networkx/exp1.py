import matplotlib.pyplot as plt 
import networkx as nx 
 
fig, axes = plt.subplots(2, 2, figsize=(10, 8)) 
 
K_5 = nx.Graph() 
K_5.add_nodes_from(range(5)) 
K_5.add_edges_from([ 
    (0,1),(0,2),(0,3),(0,4),(1,2),(1,3),(1,4),(2,3),(2,4),(3,4)]) 
nx.draw(K_5, ax=axes[0, 0], with_labels=True) 
axes[0, 0].set_title("K5 / Complete Graph") 
 
C_5 = nx.Graph() 
C_5.add_nodes_from(range(5)) 
C_5.add_edges_from([ 
    (0,1),(1,2),(2,3),(3,4),(4,0) 
]) 
nx.draw(C_5, ax=axes[0, 1], with_labels=True) 
axes[0, 1].set_title("C5 / Cycle Graph") 
 
P_5 = nx.Graph() 
P_5.add_nodes_from(range(5)) 
P_5.add_edges_from([ 
    (0,1),(1,2),(2,3),(3,4)]) 
nx.draw(P_5, ax=axes[1, 0],node_color='red', with_labels=True) 
 
axes[1, 0].set_title("P5 / Path Graph") 
 
K3 = nx.Graph() 
K3.add_nodes_from(range(5)) 
K3.add_edges_from([(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)]) 
pos={ } 
pos[0]=(0,1) 
pos[1]=(1,1) 
pos[2]=(0,0) 
pos[3]=(1,0) 
pos[4]=(2,0) 
nx.draw(K3,pos, ax=axes[1,1],with_labels=True) 
axes[1,1].set_title("K2,3/bipartite graph") 
plt.show()