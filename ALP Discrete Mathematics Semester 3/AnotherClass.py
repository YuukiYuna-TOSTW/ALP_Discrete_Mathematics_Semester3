import networkx as nx
from collections import deque

class AnotherClass:
    def __init__(self, graph_input):
        # ✅ Cek apakah input adalah GraphClass object
        if hasattr(graph_input, 'get_graph'):
            # Input adalah GraphClass object
            self.G = graph_input.get_graph()
            if self.G is None:
                raise ValueError("❌ Error: Graph dari GraphClass tidak valid")
            print("✓ AnotherClass berhasil diinisialisasi dengan GraphClass")
        elif isinstance(graph_input, (nx.Graph, nx.DiGraph)):
            # Input adalah NetworkX Graph langsung
            self.G = graph_input
            print("✓ AnotherClass berhasil diinisialisasi dengan NetworkX Graph")
        else:
            raise TypeError("❌ Error: Input harus berupa NetworkX Graph atau GraphClass object")
        
        # ✅ Validasi graph
        if self.G.number_of_nodes() == 0:
            raise ValueError("❌ Error: Graph tidak memiliki nodes")

    def degrees(self):
        try:
            if self.G.is_directed():
                result = {
                    node: {
                        "in_degree": self.G.in_degree(node),
                        "out_degree": self.G.out_degree(node),
                        "total_degree": self.G.degree(node)
                    }
                    for node in self.G.nodes()
                }
            else:
                result = {node: self.G.degree(node) for node in self.G.nodes()}
            
            print("✓ Berhasil menghitung degree semua nodes")
            return result
            
        except Exception as e:
            print(f"❌ Error saat menghitung degrees: {str(e)}")
            return None

    def has_cycle(self):
        try:
            if self.G.is_directed():
                cycles = list(nx.simple_cycles(self.G))
            else:
                cycles = list(nx.cycle_basis(self.G))
            
            has_cycle = len(cycles) > 0
            
            if has_cycle:
                print(f"✓ Graf memiliki {len(cycles)} cycle(s)")
            else:
                print("✓ Graf tidak memiliki cycle")
            
            return has_cycle, cycles
            
        except Exception as e:
            print(f"❌ Error saat cek cycle: {str(e)}")
            return False, []

    def is_connected(self):
        try:
            if self.G.is_directed():
                result = nx.is_weakly_connected(self.G)
                print(f"✓ Graf adalah {'weakly connected' if result else 'not connected'}")
            else:
                result = nx.is_connected(self.G)
                print(f"✓ Graf adalah {'connected' if result else 'not connected'}")
            
            return result
            
        except Exception as e:
            print(f"❌ Error saat cek konektivitas: {str(e)}")
            return False

    def bfs(self, start):
        # ✅ Validasi start node
        if start not in self.G.nodes():
            print(f"❌ Error: Node '{start}' tidak ada dalam graph")
            return None
        
        try:
            visited = set()
            queue = deque([start])
            hasil = []

            while queue:
                node = queue.popleft()
                if node not in visited:
                    visited.add(node)
                    hasil.append(node)
                    for neigh in self.G.neighbors(node):
                        if neigh not in visited:
                            queue.append(neigh)

            print(f"✓ BFS dari '{start}': {' → '.join(str(n) for n in hasil)}")
            return hasil
            
        except Exception as e:
            print(f"❌ Error saat BFS: {str(e)}")
            return None

    def dfs(self, start):
        # ✅ Validasi start node
        if start not in self.G.nodes():
            print(f"❌ Error: Node '{start}' tidak ada dalam graph")
            return None
        
        try:
            visited = set()
            hasil = []

            def dfs_visit(node):
                visited.add(node)
                hasil.append(node)
                for neigh in self.G.neighbors(node):
                    if neigh not in visited:
                        dfs_visit(neigh)

            dfs_visit(start)
            print(f"✓ DFS dari '{start}': {' → '.join(str(n) for n in hasil)}")
            return hasil
            
        except Exception as e:
            print(f"❌ Error saat DFS: {str(e)}")
            return None
        
    def dijkstra_all(self, start):
        # ✅ Validasi start node
        if start not in self.G.nodes():
            print(f"❌ Error: Node '{start}' tidak ada dalam graph")
            return None
        
        try:
            # ✅ Cek apakah graph memiliki weight
            has_weight = any('weight' in self.G[u][v] and self.G[u][v]['weight'] is not None 
                           for u, v in self.G.edges())
            
            if not has_weight:
                print("⚠ Warning: Graph tidak memiliki weight, menggunakan weight=1")
                result = nx.single_source_shortest_path_length(self.G, start)
            else:
                result = nx.single_source_dijkstra_path_length(self.G, start, weight='weight')
            
            print(f"✓ Dijkstra dari '{start}' berhasil dihitung untuk {len(result)} node(s)")
            return result
            
        except Exception as e:
            print(f"❌ Error saat menjalankan Dijkstra: {str(e)}")
            return None

    def dijkstra_to(self, start, target):
        # ✅ Validasi nodes
        if start not in self.G.nodes():
            print(f"❌ Error: Node start '{start}' tidak ada dalam graph")
            return None, []
        
        if target not in self.G.nodes():
            print(f"❌ Error: Node target '{target}' tidak ada dalam graph")
            return None, []
        
        if start == target:
            print(f"⚠ Warning: Start dan target sama")
            return 0, [start]
        
        try:
            # ✅ Cek apakah graph memiliki weight
            has_weight = any('weight' in self.G[u][v] and self.G[u][v]['weight'] is not None 
                           for u, v in self.G.edges())
            
            if not has_weight:
                print("⚠ Warning: Graph tidak memiliki weight, menggunakan weight=1")
                path = nx.shortest_path(self.G, start, target)
                distance = len(path) - 1
            else:
                distance, path = nx.single_source_dijkstra(self.G, start, target, weight='weight')
            
            print(f"✓ Shortest path dari '{start}' ke '{target}':")
            print(f"  • Jalur: {' → '.join(str(n) for n in path)}")
            print(f"  • Jarak: {distance}")
            
            return distance, path
            
        except nx.NetworkXNoPath:
            print(f"❌ Error: Tidak ada jalur dari '{start}' ke '{target}'")
            return None, []
        except Exception as e:
            print(f"❌ Error saat menjalankan Dijkstra: {str(e)}")
            return None, []