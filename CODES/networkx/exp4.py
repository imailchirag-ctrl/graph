import networkx as nx
import matplotlib.pyplot as plt

sequence = [6,5,4,3,2,2,1,1]

def havel_hakimi_steps(seq):
    """Return list of sequences at each Havel-Hakimi step."""
    steps = []
    seq_nodes = list(range(len(seq)))
    seq = sorted(zip(seq, seq_nodes), reverse=True)
    
    while any(deg for deg, node in seq):
        steps.append([deg for deg, node in seq])
        seq = sorted(seq, reverse=True)
        deg, node = seq.pop(0)
        for i in range(deg):
            target_deg, target_node = seq[i]
            seq[i] = (target_deg-1, target_node)
    steps.append([deg for deg, node in seq])  # final zero step
    return steps

if nx.is_graphical(sequence):
    print("Graphical sequence")
    
    # Prepare figure
    steps_list = havel_hakimi_steps(sequence)
    num_steps = len(steps_list)
    
    plt.figure(figsize=(4*num_steps, 5))
    
    nodes = list(range(len(sequence)))
    G = nx.Graph()
    G.add_nodes_from(nodes)
    pos = nx.spring_layout(G, seed=42)  # consistent layout
    
    # Apply Havel-Hakimi and draw step by step
    seq = sorted(zip(sequence, nodes), reverse=True)
    step = 0
    for current_seq in steps_list:
        plt.subplot(1, num_steps, step+1)
        nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=500)
        plt.title(f"Step {step+1}\n{current_seq}")
        
        if step < num_steps-1:  # apply HH only if not last step
            seq = sorted(seq, reverse=True)
            deg, node = seq.pop(0)
            for i in range(deg):
                target_deg, target_node = seq[i]
                G.add_edge(node, target_node)
                seq[i] = (target_deg-1, target_node)
        step += 1
    
    plt.suptitle(f"Havel-Hakimi Process for {sequence}", fontsize=16)
    plt.tight_layout()
    plt.show()
    
    print("Edges:", list(G.edges()))
else:
    print("Not a graphical sequence")