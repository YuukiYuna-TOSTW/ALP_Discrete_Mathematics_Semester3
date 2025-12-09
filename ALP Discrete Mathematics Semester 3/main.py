import os
import sys
import time
import webbrowser
from GraphClass import GraphClass
from AnotherClass import AnotherClass
import Soal1 as StudyCase1
import Soal2 as StudyCase2

class MainProgram:
    def __init__(self):
        self.graph = None
        self.analyzer = None
        self.graph_type = None
        
    def clear_screen(self):
        """Clear terminal screen"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, title):
        """Print header dengan border"""
        print("\n" + "="*70)
        print(f"{title:^70}")
        print("="*70)
    
    def print_subheader(self, title):
        """Print subheader"""
        print("\n" + "-"*70)
        print(title)
        print("-"*70)
    
    def wait_enter(self):
        """Wait for user to press enter"""
        input("\nTekan ENTER untuk melanjutkan...")
    
    def welcome_screen(self):
        """Tampilan selamat datang"""
        self.clear_screen()
        self.print_header("SELAMAT DATANG")
        print("\n🎓 Program Analisis Graf - Matematika Diskrit")
        print("   Semester 3 - Algoritma dan Pemrograman")
        print("\n📚 Program ini menyediakan:")
        print("   • Visualisasi Graf")
        print("   • Analisis Graf (Degree, Cycle, Connected)")
        print("   • Graph Traversal (BFS & DFS)")
        print("   • Shortest Path (Dijkstra)")
        print("\n📝 Node Identifier dapat berupa:")
        print("   • Huruf (A, B, C, ...)")
        print("   • Angka (1, 2, 3, ...)")
        print("   • Kombinasi (A1, N2, Vertex1, ...)")
        print("\n✨ Dibuat dengan ❤️ menggunakan Python")
        print("="*70)
        self.wait_enter()
    
    def show_study_cases(self):
        """Tampilkan study cases (Soal 1 dan Soal 2)"""
        while True:
            self.clear_screen()
            self.print_header("STUDY CASES")
            
            print("\n📖 Pilih Study Case:")
            print("   1. Study Case 1 - Graf Tak Berarah")
            print("   2. Study Case 2 - Graf Berbobot")
            print("   3. Lanjut ke Menu Utama")
            print("   0. Keluar dari Program")
            
            choice = input("\nPilihan Anda (0-3): ").strip()
            
            if choice == '1':
                self.clear_screen()
                StudyCase1.soal1_solution()
                self.wait_enter()
            elif choice == '2':
                self.clear_screen()
                StudyCase2.soal2_solution()
                self.wait_enter()
            elif choice == '3':
                break
            elif choice == '0':
                self.goodbye_screen()
                sys.exit(0)
            else:
                print("❌ Pilihan tidak valid!")
                time.sleep(1)
    
    def create_custom_graph(self):
        """Menu untuk membuat graf custom"""
        self.clear_screen()
        self.print_header("BUAT GRAF CUSTOM")
        
        print("\n📊 Pilih Tipe Graf:")
        print("   1. Graf Tidak Berbobot (Unweighted)")
        print("   2. Graf Berbobot (Weighted)")
        print("   0. Kembali")
        
        choice = input("\nPilihan Anda (0-2): ").strip()
        
        if choice == '1':
            self.create_unweighted_graph()
        elif choice == '2':
            self.create_weighted_graph()
        elif choice == '0':
            return
        else:
            print("❌ Pilihan tidak valid!")
            time.sleep(1)
    
    def _normalize_node(self, node_str):
        node_str = node_str.strip()
        
        if not node_str:
            return None
        
        # ✅ Cek apakah pure integer
        if node_str.isdigit():
            return int(node_str)
        
        # ✅ Cek apakah float
        try:
            if '.' in node_str:
                return float(node_str)
        except:
            pass
        
        # ✅ Return sebagai string untuk kombinasi dan huruf
        return node_str
    
    def _parse_nodes_input(self, input_str):
        # ✅ Support comma atau space separator
        if ',' in input_str:
            nodes_raw = input_str.split(',')
        else:
            nodes_raw = input_str.split()
        
        nodes = []
        for node_str in nodes_raw:
            normalized = self._normalize_node(node_str)
            if normalized is not None:
                nodes.append(normalized)
        
        return nodes
    
    def create_unweighted_graph(self):
        """Buat graf tidak berbobot"""
        self.clear_screen()
        self.print_subheader("BUAT GRAF TIDAK BERBOBOT")
        
        try:
            # Input nodes dengan berbagai format
            print("\n📝 Format Input Nodes:")
            print("   • Gunakan spasi atau koma sebagai separator")
            print("   • Contoh 1: A B C D")
            print("   • Contoh 2: 1 2 3 4")
            print("   • Contoh 3: A1 B2 C3")
            print("   • Contoh 4: vertex1, vertex2, vertex3")
            
            nodes_input = input("\nMasukkan nodes: ").strip()
            if not nodes_input:
                print("❌ Input nodes kosong!")
                time.sleep(2)
                return
            
            # ✅ Parse nodes dengan berbagai format
            nodes = self._parse_nodes_input(nodes_input)
            
            if not nodes:
                print("❌ Tidak ada node valid!")
                time.sleep(2)
                return
            
            print(f"\n✓ Node yang diterima: {nodes}")
            
            # Buat graph
            self.graph = GraphClass(directed=False)
            self.graph.add_nodes(nodes)
            
            # Input edges
            edges = []
            print("\n📝 Format Input Edges:")
            print("   • Format: node1 node2")
            print("   • Ketik 'done' untuk selesai")
            print("   • Contoh: A B atau 1 2 atau vertex1 vertex2\n")
            
            edge_num = 1
            while True:
                edge_input = input(f"Edge #{edge_num}: ").strip()
                if edge_input.lower() == 'done':
                    break
                
                # ✅ Parse edge input dengan berbagai format
                parts = edge_input.split()
                
                if len(parts) < 2:
                    print("⚠ Format salah! Gunakan: node1 node2")
                    continue
                
                node1_str = parts[0]
                node2_str = parts[1]
                
                # ✅ Normalize nodes
                node1 = self._normalize_node(node1_str)
                node2 = self._normalize_node(node2_str)
                
                if node1 is None or node2 is None:
                    print("⚠ Node tidak valid!")
                    continue
                
                edges.append((node1, node2))
                print(f"  ✓ Edge ({node1}, {node2}) ditambahkan")
                edge_num += 1
            
            if not edges:
                print("❌ Minimal harus ada 1 edge!")
                time.sleep(2)
                return
            
            # Tambah edges ke graph
            self.graph.add_edges_unweighted(edges)
            self.graph_type = "unweighted"
            
            # Visualisasi
            filename = "custom_unweighted_graph.html"
            if self.graph.visualize_graph(filename):
                print(f"\n✓ Graf berhasil divisualisasikan: {filename}")
            
            # Buat analyzer
            self.analyzer = AnotherClass(self.graph)
            
            print("\n✓ Graf berhasil dibuat!")
            self.wait_enter()
            
            # Langsung ke menu analisis
            self.analysis_menu()
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            self.wait_enter()
    
    def create_weighted_graph(self):
        """Buat graf berbobot"""
        self.clear_screen()
        self.print_subheader("BUAT GRAF BERBOBOT")
        
        try:
            # Input nodes dengan berbagai format
            print("\n📝 Format Input Nodes:")
            print("   • Gunakan spasi atau koma sebagai separator")
            print("   • Contoh 1: A B C D")
            print("   • Contoh 2: 1 2 3 4")
            print("   • Contoh 3: A1 B2 C3")
            print("   • Contoh 4: vertex1, vertex2, vertex3")
            
            nodes_input = input("\nMasukkan nodes: ").strip()
            if not nodes_input:
                print("❌ Input nodes kosong!")
                time.sleep(2)
                return
            
            # ✅ Parse nodes dengan berbagai format
            nodes = self._parse_nodes_input(nodes_input)
            
            if not nodes:
                print("❌ Tidak ada node valid!")
                time.sleep(2)
                return
            
            print(f"\n✓ Node yang diterima: {nodes}")
            
            # Buat graph
            self.graph = GraphClass(directed=False)
            self.graph.add_nodes(nodes)
            
            # Input edges
            edges = []
            print("\n📝 Format Input Edges:")
            print("   • Format: node1 node2 weight")
            print("   • Weight harus berupa angka (positif)")
            print("   • Ketik 'done' untuk selesai")
            print("   • Contoh: A B 5 atau 1 2 3.5 atau v1 v2 10\n")
            
            edge_num = 1
            while True:
                edge_input = input(f"Edge #{edge_num}: ").strip()
                if edge_input.lower() == 'done':
                    break
                
                # ✅ Parse edge input dengan berbagai format
                parts = edge_input.split()
                
                if len(parts) < 3:
                    print("⚠ Format salah! Gunakan: node1 node2 weight")
                    continue
                
                node1_str = parts[0]
                node2_str = parts[1]
                weight_str = parts[2]
                
                # ✅ Normalize nodes
                node1 = self._normalize_node(node1_str)
                node2 = self._normalize_node(node2_str)
                
                if node1 is None or node2 is None:
                    print("⚠ Node tidak valid!")
                    continue
                
                # ✅ Parse weight
                try:
                    weight = float(weight_str)
                    if weight <= 0:
                        print("⚠ Weight harus positif!")
                        continue
                except ValueError:
                    print("⚠ Weight harus berupa angka!")
                    continue
                
                edges.append((node1, node2, weight))
                print(f"  ✓ Edge ({node1}, {node2}, weight={weight}) ditambahkan")
                edge_num += 1
            
            if not edges:
                print("❌ Minimal harus ada 1 edge!")
                time.sleep(2)
                return
            
            # Tambah edges ke graph
            self.graph.add_edges_weighted(edges)
            self.graph_type = "weighted"
            
            # Visualisasi
            filename = "custom_weighted_graph.html"
            if self.graph.visualize_graph(filename):
                print(f"\n✓ Graf berhasil divisualisasikan: {filename}")
            
            # Buat analyzer
            self.analyzer = AnotherClass(self.graph)
            
            print("\n✓ Graf berhasil dibuat!")
            self.wait_enter()
            
            # Langsung ke menu analisis
            self.analysis_menu()
            
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            self.wait_enter()
    
    def analysis_menu(self):
        """Menu analisis graf"""
        if self.graph is None or self.analyzer is None:
            print("❌ Belum ada graf yang dibuat!")
            time.sleep(2)
            return
        
        while True:
            self.clear_screen()
            self.print_header("MENU ANALISIS GRAF")
            
            print(f"\n📊 Graf Aktif: {self.graph_type.upper()}")
            print(f"   Nodes: {self.graph.get_graph().number_of_nodes()}")
            print(f"   Edges: {self.graph.get_graph().number_of_edges()}")
            
            print("\n🔍 Pilih Analisis:")
            print("   1. Derajat Setiap Simpul")
            print("   2. Deteksi Cycle")
            print("   3. Cek Graf Connected")
            print("   4. BFS (Breadth-First Search)")
            print("   5. DFS (Depth-First Search)")
            print("   6. Dijkstra - Jarak Terpendek")
            print("   7. Visualisasi Graf")
            print("   8. Buat Graf Baru")
            print("   0. Kembali ke Menu Utama")
            
            choice = input("\nPilihan Anda (0-8): ").strip()
            
            if choice == '1':
                self.analyze_degrees()
            elif choice == '2':
                self.analyze_cycle()
            elif choice == '3':
                self.analyze_connected()
            elif choice == '4':
                self.analyze_bfs()
            elif choice == '5':
                self.analyze_dfs()
            elif choice == '6':
                self.analyze_dijkstra()
            elif choice == '7':
                self.show_visualization()
            elif choice == '8':
                self.create_custom_graph()
            elif choice == '0':
                break
            else:
                print("❌ Pilihan tidak valid!")
                time.sleep(1)
    
    def analyze_degrees(self):
        """Analisis derajat simpul"""
        self.clear_screen()
        self.print_subheader("DERAJAT SETIAP SIMPUL")
        
        degrees = self.analyzer.degrees()
        
        if degrees:
            print("\n📊 Hasil Analisis:")
            print(f"{'Node':<15} {'Degree':<10}")
            print("-" * 25)
            
            for node in sorted(degrees.keys(), key=str):
                print(f"{str(node):<15} {degrees[node]:<10}")
        
        self.wait_enter()
    
    def analyze_cycle(self):
        """Analisis cycle"""
        self.clear_screen()
        self.print_subheader("DETEKSI CYCLE")
        
        has_cycle, cycles = self.analyzer.has_cycle()
        
        print("\n🔄 Hasil Analisis:")
        
        if has_cycle:
            print(f"  ✓ Graf memiliki {len(cycles)} cycle(s)")
            print("\n  Daftar Cycle:")
            for i, cycle in enumerate(cycles, 1):
                cycle_str = ' → '.join(str(n) for n in cycle) + f' → {cycle[0]}'
                print(f"    {i}. {cycle_str}")
        else:
            print("  ✗ Graf tidak memiliki cycle")
        
        self.wait_enter()
    
    def analyze_connected(self):
        """Analisis konektivitas"""
        self.clear_screen()
        self.print_subheader("CEK GRAF CONNECTED")
        
        is_connected = self.analyzer.is_connected()
        
        print("\n🔗 Hasil Analisis:")
        
        if is_connected:
            print("  ✓ Graf ini CONNECTED")
            print("\n  Penjelasan:")
            print("    Setiap pasang simpul dalam graf memiliki jalur yang")
            print("    menghubungkannya.")
        else:
            print("  ✗ Graf ini TIDAK CONNECTED")
            print("\n  Penjelasan:")
            print("    Terdapat simpul yang tidak dapat dicapai dari simpul lain.")
        
        self.wait_enter()
    
    def analyze_bfs(self):
        """Analisis BFS"""
        self.clear_screen()
        self.print_subheader("BREADTH-FIRST SEARCH (BFS)")
        
        # Pilih start node
        G = self.graph.get_graph()
        nodes = sorted(list(G.nodes()), key=str)
        
        print("\n📍 Nodes yang tersedia:")
        for i, node in enumerate(nodes, 1):
            print(f"   {i}. {node}")
        
        try:
            choice = int(input("\nPilih start node (nomor): ").strip())
            if 1 <= choice <= len(nodes):
                start_node = nodes[choice - 1]
                
                print(f"\n🔍 Menjalankan BFS dari node '{start_node}'...\n")
                bfs_result = self.analyzer.bfs(start_node)
                
                if bfs_result:
                    print(f"\n✓ Urutan kunjungan:")
                    print(f"  {' → '.join(str(n) for n in bfs_result)}")
            else:
                print("❌ Pilihan tidak valid!")
        except ValueError:
            print("❌ Input harus berupa angka!")
        
        self.wait_enter()
    
    def analyze_dfs(self):
        """Analisis DFS"""
        self.clear_screen()
        self.print_subheader("DEPTH-FIRST SEARCH (DFS)")
        
        # Pilih start node
        G = self.graph.get_graph()
        nodes = sorted(list(G.nodes()), key=str)
        
        print("\n📍 Nodes yang tersedia:")
        for i, node in enumerate(nodes, 1):
            print(f"   {i}. {node}")
        
        try:
            choice = int(input("\nPilih start node (nomor): ").strip())
            if 1 <= choice <= len(nodes):
                start_node = nodes[choice - 1]
                
                print(f"\n🔍 Menjalankan DFS dari node '{start_node}'...\n")
                dfs_result = self.analyzer.dfs(start_node)
                
                if dfs_result:
                    print(f"\n✓ Urutan kunjungan:")
                    print(f"  {' → '.join(str(n) for n in dfs_result)}")
            else:
                print("❌ Pilihan tidak valid!")
        except ValueError:
            print("❌ Input harus berupa angka!")
        
        self.wait_enter()
    
    def analyze_dijkstra(self):
        """Analisis Dijkstra"""
        self.clear_screen()
        self.print_subheader("ALGORITMA DIJKSTRA - SHORTEST PATH")
        
        G = self.graph.get_graph()
        nodes = sorted(list(G.nodes()), key=str)
        
        print("\n🎯 Pilih Analisis:")
        print("   1. Jarak ke Seluruh Node")
        print("   2. Jalur Terpendek ke Node Tertentu")
        print("   0. Kembali")
        
        choice = input("\nPilihan (0-2): ").strip()
        
        if choice == '1':
            self.dijkstra_all_nodes(nodes)
        elif choice == '2':
            self.dijkstra_to_node(nodes)
        
        self.wait_enter()
    
    def dijkstra_all_nodes(self, nodes):
        """Dijkstra ke semua node"""
        print("\n📍 Nodes yang tersedia:")
        for i, node in enumerate(nodes, 1):
            print(f"   {i}. {node}")
        
        try:
            choice = int(input("\nPilih start node (nomor): ").strip())
            if 1 <= choice <= len(nodes):
                start_node = nodes[choice - 1]
                
                print(f"\n🔍 Menghitung jarak dari '{start_node}'...\n")
                distances = self.analyzer.dijkstra_all(start_node)
                
                if distances:
                    print(f"\n✓ Jarak dari {start_node}:")
                    print(f"{'Node':<15} {'Jarak':<10}")
                    print("-" * 25)
                    
                    for node in sorted(distances.keys(), key=str):
                        print(f"{str(node):<15} {distances[node]:<10}")
            else:
                print("❌ Pilihan tidak valid!")
        except ValueError:
            print("❌ Input harus berupa angka!")
    
    def dijkstra_to_node(self, nodes):
        """Dijkstra ke node tertentu"""
        print("\n📍 Pilih Start Node:")
        for i, node in enumerate(nodes, 1):
            print(f"   {i}. {node}")
        
        try:
            start_choice = int(input("\nStart node (nomor): ").strip())
            if not (1 <= start_choice <= len(nodes)):
                print("❌ Pilihan tidak valid!")
                return
            
            start_node = nodes[start_choice - 1]
            
            print("\n📍 Pilih Target Node:")
            for i, node in enumerate(nodes, 1):
                if node != start_node:
                    print(f"   {i}. {node}")
            
            target_choice = int(input("\nTarget node (nomor): ").strip())
            if not (1 <= target_choice <= len(nodes)):
                print("❌ Pilihan tidak valid!")
                return
            
            target_node = nodes[target_choice - 1]
            
            if start_node == target_node:
                print("❌ Start dan target tidak boleh sama!")
                return
            
            print(f"\n🔍 Mencari jalur terpendek dari '{start_node}' ke '{target_node}'...\n")
            distance, path = self.analyzer.dijkstra_to(start_node, target_node)
            
            if path:
                print(f"\n✓ Jalur terpendek:")
                print(f"  {' → '.join(str(n) for n in path)}")
                print(f"\n✓ Jarak total: {distance}")
                      
        except ValueError:
            print("❌ Input harus berupa angka!")
    
    def show_visualization(self):
        """Tampilkan visualisasi"""
        self.clear_screen()
        self.print_subheader("VISUALISASI GRAF")
        
        filename = f"current_graph_{self.graph_type}.html"
        
        if self.graph.visualize_graph(filename):
            print(f"\n✓ Visualisasi disimpan: {filename}")
        
        self.wait_enter()
    
    def main_menu(self):
        """Menu utama"""
        while True:
            self.clear_screen()
            self.print_header("MENU UTAMA")
            
            print("\n🎯 Pilih Menu:")
            print("   1. Lihat Study Cases")
            print("   2. Buat Graf Custom")
            print("   3. Menu Analisis Graf")
            print("   0. Keluar")
            
            choice = input("\nPilihan Anda (0-3): ").strip()
            
            if choice == '1':
                self.show_study_cases()
            elif choice == '2':
                self.create_custom_graph()
            elif choice == '3':
                if self.graph is None:
                    print("\n❌ Belum ada graf! Silakan buat graf terlebih dahulu.")
                    time.sleep(2)
                else:
                    self.analysis_menu()
            elif choice == '0':
                self.goodbye_screen()
                break
            else:
                print("❌ Pilihan tidak valid!")
                time.sleep(1)
    
    def goodbye_screen(self):
        """Tampilan terima kasih"""
        self.clear_screen()
        self.print_header("TERIMA KASIH")
        print("\n🙏 Terima kasih telah menggunakan program ini!")
        print("   Program Analisis Graf - Matematika Diskrit")
        print("   Menggunakan GraphClass.py dan AnotherClass.py")
        print("\n✨ Semoga bermanfaat untuk pembelajaran Anda!")
        print("\n👋 Sampai jumpa lagi!")
        print("="*70 + "\n")
    
    def run(self):
        """Jalankan program utama"""
        try:
            # Tampilkan welcome screen
            self.welcome_screen()
            
            # Tampilkan study cases
            self.show_study_cases()
            
            # Jalankan menu utama
            self.main_menu()
            
        except KeyboardInterrupt:
            print("\n\n⚠ Program dihentikan oleh user")
            self.goodbye_screen()
        except Exception as e:
            print(f"\n❌ Error tidak terduga: {str(e)}")
            import traceback
            traceback.print_exc()
            self.goodbye_screen()


# ============================================================
# MAIN PROGRAM
# ============================================================
if __name__ == "__main__":
    program = MainProgram()
    program.run()