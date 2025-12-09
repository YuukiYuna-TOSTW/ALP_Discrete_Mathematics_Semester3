import networkx as nx
from pyvis.network import Network
import os
import sys

class GraphClass:
    def __init__(self, directed=False):
        try:
            self.graph = nx.DiGraph() if directed else nx.Graph()
            self.is_directed = directed
            print(f"✓ Graph berhasil dibuat ({'Directed' if directed else 'Undirected'})")
            print(f"  Node identifier support: String, Integer, Float, Kombinasi")
        except Exception as e:
            print(f"❌ Error saat inisialisasi graph: {str(e)}")
            self.graph = None
            self.is_directed = False

    def add_nodes(self, node_list):
        if self.graph is None:
            print("❌ Error: Graph belum diinisialisasi")
            return False
        
        if not node_list:
            print("❌ Error: Node list kosong")
            return False
        
        if not isinstance(node_list, (list, tuple, set)):
            print("❌ Error: node_list harus berupa list, tuple, atau set")
            return False
        
        try:
            # ✅ Validasi setiap node dengan berbagai tipe
            valid_nodes = []
            for node in node_list:
                # ✅ Support: int, float, str
                if isinstance(node, (int, float)):
                    valid_nodes.append(node)
                elif isinstance(node, str):
                    if node.strip() != "":
                        valid_nodes.append(node)
                else:
                    # ✅ Try convert ke string
                    node_str = str(node).strip()
                    if node_str != "" and node_str != "None":
                        valid_nodes.append(node)
            
            if not valid_nodes:
                print("❌ Error: Tidak ada node valid untuk ditambahkan")
                return False
            
            self.graph.add_nodes_from(valid_nodes)
            print(f"✓ Berhasil menambahkan {len(valid_nodes)} node(s)")
            
            # ✅ Print node types untuk info user
            int_nodes = [n for n in valid_nodes if isinstance(n, int)]
            float_nodes = [n for n in valid_nodes if isinstance(n, float)]
            str_nodes = [n for n in valid_nodes if isinstance(n, str)]
            
            if int_nodes:
                print(f"  • Integer nodes: {int_nodes}")
            if float_nodes:
                print(f"  • Float nodes: {float_nodes}")
            if str_nodes:
                print(f"  • String nodes: {str_nodes}")
            
            return True
            
        except Exception as e:
            print(f"❌ Error saat menambahkan nodes: {str(e)}")
            return False

    def add_edges_unweighted(self, edges):
        if self.graph is None:
            print("❌ Error: Graph belum diinisialisasi")
            return False
        
        if not edges:
            print("❌ Error: Edge list kosong")
            return False
        
        if not isinstance(edges, (list, tuple, set)):
            print("❌ Error: edges harus berupa list, tuple, atau set")
            return False
        
        try:
            added_count = 0
            skipped_count = 0
            
            for edge in edges:
                # ✅ Validasi format edge
                if not isinstance(edge, (tuple, list)) or len(edge) != 2:
                    print(f"⚠ Warning: Format edge tidak valid, harus (u, v): {edge}")
                    skipped_count += 1
                    continue
                
                u, v = edge
                
                # ✅ Validasi node exists dengan berbagai tipe
                if u not in self.graph.nodes():
                    print(f"⚠ Warning: Node '{u}' tidak ada dalam graph, menambahkan otomatis")
                    self.graph.add_node(u)
                
                if v not in self.graph.nodes():
                    print(f"⚠ Warning: Node '{v}' tidak ada dalam graph, menambahkan otomatis")
                    self.graph.add_node(v)
                
                # ✅ Validasi self-loop
                if u == v:
                    print(f"⚠ Warning: Self-loop tidak diperbolehkan: ({u}, {v})")
                    skipped_count += 1
                    continue
                
                # ✅ Cek duplikat edge
                if self.graph.has_edge(u, v):
                    print(f"⚠ Warning: Edge ({u}, {v}) sudah ada, melewati")
                    skipped_count += 1
                    continue
                
                # ✅ Tambahkan edge dengan weight=None
                self.graph.add_edge(u, v, weight=None)
                added_count += 1
            
            print(f"✓ Berhasil menambahkan {added_count} edge(s)")
            if skipped_count > 0:
                print(f"⚠ {skipped_count} edge(s) dilewati karena invalid atau duplikat")
            
            return added_count > 0
            
        except Exception as e:
            print(f"❌ Error saat menambahkan edges: {str(e)}")
            return False

    def add_edges_weighted(self, edges):
        if self.graph is None:
            print("❌ Error: Graph belum diinisialisasi")
            return False
        
        if not edges:
            print("❌ Error: Edge list kosong")
            return False
        
        if not isinstance(edges, (list, tuple, set)):
            print("❌ Error: edges harus berupa list, tuple, atau set")
            return False
        
        try:
            added_count = 0
            skipped_count = 0
            
            for edge in edges:
                # ✅ Validasi format edge
                if not isinstance(edge, (tuple, list)) or len(edge) != 3:
                    print(f"⚠ Warning: Format edge tidak valid, harus (u, v, weight): {edge}")
                    skipped_count += 1
                    continue
                
                u, v, w = edge
                
                # ✅ Validasi node exists dengan berbagai tipe
                if u not in self.graph.nodes():
                    print(f"⚠ Warning: Node '{u}' tidak ada dalam graph, menambahkan otomatis")
                    self.graph.add_node(u)
                
                if v not in self.graph.nodes():
                    print(f"⚠ Warning: Node '{v}' tidak ada dalam graph, menambahkan otomatis")
                    self.graph.add_node(v)
                
                # ✅ Validasi self-loop
                if u == v:
                    print(f"⚠ Warning: Self-loop tidak diperbolehkan: ({u}, {v})")
                    skipped_count += 1
                    continue
                
                # ✅ Validasi weight
                try:
                    weight = float(w)
                    if weight <= 0:
                        print(f"⚠ Warning: Weight harus positif untuk edge ({u}, {v}), menggunakan nilai absolut")
                        weight = abs(weight)
                except (ValueError, TypeError):
                    print(f"⚠ Warning: Weight tidak valid untuk edge ({u}, {v}): {w}, menggunakan 1")
                    weight = 1
                
                # ✅ Cek duplikat edge
                if self.graph.has_edge(u, v):
                    print(f"⚠ Warning: Edge ({u}, {v}) sudah ada, mengupdate weight ke {weight}")
                    self.graph[u][v]['weight'] = weight
                    continue
                
                # ✅ Tambahkan edge dengan weight
                self.graph.add_edge(u, v, weight=weight)
                added_count += 1
            
            print(f"✓ Berhasil menambahkan {added_count} edge(s)")
            if skipped_count > 0:
                print(f"⚠ {skipped_count} edge(s) dilewati karena invalid")
            
            return added_count > 0
            
        except Exception as e:
            print(f"❌ Error saat menambahkan weighted edges: {str(e)}")
            return False

    def get_graph(self):
        if self.graph is None:
            print("❌ Error: Graph belum diinisialisasi")
            return None
        
        try:
            return self.graph
        except Exception as e:
            print(f"❌ Error saat mengambil graph: {str(e)}")
            return None

    def validate_graph(self):
        if self.graph is None:
            print("❌ Error: Graph belum diinisialisasi")
            return False
        
        if self.graph.number_of_nodes() == 0:
            print("❌ Error: Graph tidak memiliki nodes")
            return False
        
        if self.graph.number_of_edges() == 0:
            print("⚠ Warning: Graph tidak memiliki edges")
            return True
        
        return True

    def visualize_graph(self, filename="graph_visu.html"):
        # ✅ Validasi graph
        if not self.validate_graph():
            return False
        
        # ✅ Validasi filename
        if not filename or not isinstance(filename, str):
            print("❌ Error: Filename tidak valid")
            return False
        
        if not filename.endswith('.html'):
            filename += '.html'
            print(f"⚠ Warning: Menambahkan extension .html ke filename: {filename}")
        
        try:
            G = self.graph
            
            # ✅ Buat network visualization
            try:
                net = Network(height="600px", width="100%", directed=G.is_directed())
            except Exception as e:
                print(f"❌ Error saat membuat Network object: {str(e)}")
                return False
            
            # ✅ Convert dari NetworkX (support berbagai tipe node)
            try:
                net.from_nx(G)
            except Exception as e:
                print(f"❌ Error saat convert dari NetworkX: {str(e)}")
                return False
            
            # ✅ Customize nodes (support berbagai tipe)
            try:
                for n in net.nodes:
                    n['size'] = 30
                    n['font'] = {'size': 100}
                    # ✅ Convert node label ke string untuk display
                    n['label'] = str(n['id'])
            except Exception as e:
                print(f"⚠ Warning: Error saat customize nodes: {str(e)}")
            
            # ✅ Set physics
            try:
                net.barnes_hut()
            except Exception as e:
                print(f"⚠ Warning: Error saat set physics: {str(e)}")
            
            # ✅ Save file
            try:
                net.show(filename, notebook=False)
                
                # ✅ Verify file exists
                if os.path.exists(filename):
                    file_size = os.path.getsize(filename)
                    print(f"✓ Visualisasi berhasil disimpan ke: {filename} ({file_size} bytes)")
                    return True
                else:
                    print(f"❌ Error: File {filename} tidak berhasil dibuat")
                    return False
                    
            except Exception as e:
                print(f"❌ Error saat menyimpan file: {str(e)}")
                return False
            
        except Exception as e:
            print(f"❌ Error tidak terduga saat visualisasi: {str(e)}")
            import traceback
            traceback.print_exc()
            return False