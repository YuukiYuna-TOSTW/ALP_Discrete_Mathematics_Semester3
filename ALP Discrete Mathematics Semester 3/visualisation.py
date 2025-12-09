from pyvis.network import Network
import networkx as nx

def visualize_graph(G, filename="graph_visu.html"):
    net = Network(height="600px", width="100%", directed=G.is_directed())

    net.from_nx(G)

    net.barnes_hut()

    net.show(filename)

def shortest_path_visualisation(G, source, target, filename="shortest_path.html"):
    try:
        path = nx.shortest_path(G, source, target, 'weight')
    except nx.NetworkXNoPath:
        print("No path found between", source, "and", target)
        return

    net = Network(height="600px", width="100%", directed=G.is_directed())
    net.from_nx(G)

    for i in range(len(path) - 1):
        n1 = path[i]
        n2 = path[i+1]
        weight = G[n1][n2].get('weight', None)

        net.add_edge(
            n1, n2,
            color="red",
            width=4,
            label=str(weight) if weight else None
        )

    # highlight nodes
    for n in path:
        net.get_node(n)['color'] = 'yellow'

    net.barnes_hut()
    net.show(filename)
