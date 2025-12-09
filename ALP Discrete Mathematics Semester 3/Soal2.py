from GraphClass import GraphClass
from AnotherClass import AnotherClass
import os
import webbrowser

def print_header(title):
    """Helper function untuk print header"""
    print("\n" + "="*70)
    print(f"{title:^70}")
    print("="*70)

def print_subheader(title):
    """Helper function untuk print subheader"""
    print("\n" + "-"*70)
    print(f"{title}")
    print("-"*70)

def soal2_solution():
    """
    Menyelesaikan Soal 2:
    Diberikan graf berbobot:
    V = {A, B, C, D, E, F, G}
    E = {(A,B,2), (A,C,5), (B,D,4), (B,E,6), (C,F,3), (D,G,2), (E,F,4), (F,G,1)}
    
    a. Gambarkan Grafnya
    b. Tentukan urutan kunjungan menggunakan BFS dimulai dari simpul A
    c. Tentukan urutan kunjungan menggunakan DFS (rekursif) dengan simpul awal A 
       dan urutan tetangga berdasarkan alfabet
    d. Gunakan Algoritma Dijkstra dari simpul A untuk menentukan:
       1. Jarak minimum dari A ke seluruh simpul
       2. Jalur terpendek dari A ke G
    """
    
    print_header("SOAL 2 - GRAF BERBOBOT")
    
    # ============================================================
    # DATA SOAL
    # ============================================================
    print("\n📋 Data Graf:")
    print(f"  V = {{A, B, C, D, E, F, G}}")
    print(f"  E = {{(A,B,2), (A,C,5), (B,D,4), (B,E,6), (C,F,3), (D,G,2), (E,F,4), (F,G,1)}}")
    
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    edges = [
        ('A', 'B', 2),
        ('A', 'C', 5),
        ('B', 'D', 4),
        ('B', 'E', 6),
        ('C', 'F', 3),
        ('D', 'G', 2),
        ('E', 'F', 4),
        ('F', 'G', 1)
    ]
    
    # ============================================================
    # BAGIAN A: GAMBARKAN GRAF
    # ============================================================
    print_subheader("a. Gambarkan Grafnya")
    
    try:
        # ✅ Buat graph dengan GraphClass
        graph = GraphClass(directed=False)
        
        # ✅ Tambahkan nodes
        graph.add_nodes(nodes)
        
        # ✅ Tambahkan edges (weighted)
        graph.add_edges_weighted(edges)
        
        # ✅ Visualisasi graf
        filename = "soal2_graf_visualisasi.html"
        graph.visualize_graph(filename)
        
        print(f"\nJawaban:")
        print(f"  Graf berbobot telah divisualisasikan dan disimpan ke file: {filename}")
        
    except Exception as e:
        print(f"❌ Error saat membuat graf: {str(e)}")
        return
    
    # ============================================================
    # BUAT ANALYZER UNTUK ANALISIS LANJUTAN
    # ============================================================
    try:
        analyzer = AnotherClass(graph)
    except Exception as e:
        print(f"❌ Error saat membuat analyzer: {str(e)}")
        return
    
    # ============================================================
    # BAGIAN B: BFS dari simpul A
    # ============================================================
    print_subheader("b. Tentukan Urutan Kunjungan Menggunakan BFS Dimulai dari Simpul A")
    
    bfs_result = analyzer.bfs('A')
    
    if bfs_result:
        print(f"\nJawaban:")
        print(f"  Urutan kunjungan BFS dari A:")
        print(f"    {' → '.join(bfs_result)}")
    
    # ============================================================
    # BAGIAN C: DFS dari simpul A (urutan tetangga berdasarkan alfabet)
    # ============================================================
    print_subheader("c. Tentukan Urutan Kunjungan Menggunakan DFS (Rekursif)")
    print("   dengan Simpul Awal A dan Urutan Tetangga Berdasarkan Alfabet")
    
    dfs_result = analyzer.dfs('A')
    
    if dfs_result:
        print(f"\nJawaban:")
        print(f"  Urutan kunjungan DFS dari A:")
        print(f"    {' → '.join(dfs_result)}")
    
    # ============================================================
    # BAGIAN D: Algoritma Dijkstra dari simpul A
    # ============================================================
    print_subheader("d. Gunakan Algoritma Dijkstra dari Simpul A untuk Menentukan:")
    
    # ============================================================
    # D.1: Jarak minimum dari A ke seluruh simpul
    # ============================================================
    print("\n  1. Jarak Minimum dari A ke Seluruh Simpul")
    print("  " + "-"*66)
    
    dijkstra_all = analyzer.dijkstra_all('A')
    
    if dijkstra_all:
        print(f"\n  Jawaban:")
        print(f"    Jarak minimum dari A ke setiap simpul:")
        print(f"    {'Simpul':<15} {'Jarak dari A':<20}")
        print(f"    {'-'*35}")
        
        for node in sorted(dijkstra_all.keys()):
            distance = dijkstra_all[node]
            print(f"    {node:<15} {distance:<20}")
    
    # ============================================================
    # D.2: Jalur terpendek dari A ke G
    # ============================================================
    print("\n  2. Jalur Terpendek dari A ke G")
    print("  " + "-"*66)
    
    distance, path = analyzer.dijkstra_to('A', 'G')
    
    if path:
        print(f"\n  Jawaban:")
        print(f"    Jalur terpendek dari A ke G:")
        print(f"      {' → '.join(path)}")
        print(f"    Jarak total: {distance}")
        
        # ✅ Visualisasi shortest path
        filename_path = "soal2_shortest_path_A_to_G.html"
        graph.shortest_path_visualisation('A', 'G', filename_path)
        print(f"\n    Visualisasi jalur terpendek disimpan ke: {filename_path}")
    
    print("\n" + "="*70)


# ============================================================
# MAIN PROGRAM
# ============================================================
if __name__ == "__main__":
    try:
        soal2_solution()
        print("\n✅ Program selesai!")
        
    except KeyboardInterrupt:
        print("\n\n⚠ Program dihentikan oleh user")
    except Exception as e:
        print(f"\n❌ Error tidak terduga: {str(e)}")
        import traceback
        traceback.print_exc()