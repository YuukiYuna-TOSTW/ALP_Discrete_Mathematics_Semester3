from pyvis.network import Network
import networkx as nx

def visualize_graph(G, filename="graph_visualisation.html"):
    net = Network(height="600px", width="100%", directed=G.is_directed())

    net.from_nx(G)

    net.barnes_hut()

    net.show(filename)

def shortest_path(G, source, target, file_name="shortest_path.html"):
    try:
        path = nx.shortest_path(G, source=source, target=target)
        return path
    except nx.NetworkXNoPath:
        return None