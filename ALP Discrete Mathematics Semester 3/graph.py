import networkx as nx

class graph:
    def __init__(self):
        self.G = nx.Graph()

    def add_node(self, n):
        self.G.add_node(n)

    def add_edge(self, u, v):
        self.G.add_edge(u, v)
