import networkx as nx
import visualisation as visu

def Node_Degree(G, node):
    return G.degree(node)

def Graph_Cycles(G):
    return list(nx.simple_cycles(G))

def Graf_Connected(G):
    return nx.is_connected(G)

def Breadth_First_Search(G, start):
    return list(nx.bfs_edges(G, start))

def Depth_First_Search(G, start):
    return list(nx.dfs_edges(G, start))

def Dijkstra_Shortest_Path(G, source, target):
    visu.shortest_path_visualisation(G, source, target)