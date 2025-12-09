import networkx as nx

G = nx.Graph()
nodes = input("Enter nodes separated by space: ").split()
G.add_nodes_from(nodes)
edges = []
entered_edges = False
while True:
    e = input("Enter edge (node1 node2 weight) or 'done': ")
    if e == 'done':
        break
    entered_edges = True
    try:
        n1, n2, w = e.split()
        if n1 not in nodes or n2 not in nodes:
            print("Error: One or both nodes not in graph.")
            continue
        edges.append((n1, n2, int(w)))
    except ValueError:
        print("Error: Please enter edge as 'node1 node2 weight'.")
if not entered_edges:
    nodes = list(G.nodes)
G.add_weighted_edges_from(edges)

print (edges)
print (nodes)