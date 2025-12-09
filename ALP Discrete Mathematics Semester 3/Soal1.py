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

def soal1_solution():
    """
    Menyelesaikan Soal 1:
    Diberikan graf tak berarah G = (V, E) dengan:
    V = {A, B, C, D, E, F}
    E = {(A,B), (A,C), (B,D), (C,E), (D,E), (E,F), (C,F)}
    
    a. Gambarkan graf berdasarkan himpunan sisi di atas
    b. Tentukan derajat setiap simpul
    c. Tentukan apakah graf memiliki cycle. Jika ada, sebutkan
    d. Tentukan apakah graf ini connected. Jelaskan
    """
    
    print_header("SOAL 1 - GRAF TAK BERARAH")
    
    # ============================================================
    # DATA SOAL
    # ============================================================
    print("\n📋 Data Graf:")
    print(f"  V = {{A, B, C, D, E, F}}")
    print(f"  E = {{(A,B), (A,C), (B,D), (C,E), (D,E), (E,F), (C,F)}}")
    
    nodes = ['A', 'B', 'C', 'D', 'E', 'F']
    edges = [
        ('A', 'B'),
        ('A', 'C'),
        ('B', 'D'),
        ('C', 'E'),
        ('D', 'E'),
        ('E', 'F'),
        ('C', 'F')
    ]
    
    # ============================================================
    # BAGIAN A: GAMBARKAN GRAF
    # ============================================================
    print_subheader("a. Gambarkan Graf Berdasarkan Himpunan Sisi di Atas")
    
    try:
        # ✅ Buat graph dengan GraphClass
        graph = GraphClass(directed=False)
        
        # ✅ Tambahkan nodes
        if not graph.add_nodes(nodes):
            print("❌ Gagal menambahkan nodes")
            return
        
        # ✅ Tambahkan edges (unweighted)
        if not graph.add_edges_unweighted(edges):
            print("❌ Gagal menambahkan edges")
            return
        
        # ✅ Visualisasi graf
        filename = "soal1_graf_visualisasi.html"
        if graph.visualize_graph(filename):
            print(f"\n✓ Graf berhasil divisualisasikan!")
            print(f"  File: {filename}")
        
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
    # BAGIAN B: DERAJAT SETIAP SIMPUL
    # ============================================================
    print_subheader("b. Tentukan Derajat Setiap Simpul")
    
    degrees = analyzer.degrees()
    
    if degrees:
        print("\n📊 Derajat Setiap Simpul:")
        print(f"{'Node':<10} {'Degree':<10}")
        print("-" * 20)
        
        for node in sorted(degrees.keys()):
            print(f"{node:<10} {degrees[node]:<10}")
    
    # ============================================================
    # BAGIAN C: DETEKSI CYCLE
    # ============================================================
    print_subheader("c. Tentukan Apakah Graf Memiliki Cycle. Jika Ada, Sebutkan")
    
    has_cycle, cycles = analyzer.has_cycle()
    
    print(f"\n🔄 Hasil Analisis Cycle:")
    
    if has_cycle:
        print(f"  ✓ Graf MEMILIKI cycle")
        print(f"  • Jumlah cycle yang ditemukan: {len(cycles)}")
        print(f"\n  📋 Daftar Cycle:")
        
        for i, cycle in enumerate(cycles, 1):
            # ✅ Format cycle dengan arrow
            cycle_path = ' → '.join(cycle) + f' → {cycle[0]}'
            print(f"    Cycle {i}: {cycle_path}")
            print(f"             Panjang: {len(cycle)} node(s)")
        
        print(f"\n  💡 Penjelasan:")
        print(f"     Graf ini memiliki cycle karena terdapat jalur tertutup")
        print(f"     yang dimulai dan berakhir di node yang sama tanpa mengulang edge.")
    else:
        print(f"  ✗ Graf TIDAK memiliki cycle")
        print(f"\n  💡 Penjelasan:")
        print(f"     Graf ini adalah pohon (tree) atau hutan (forest).")
    
    # ============================================================
    # BAGIAN D: KONEKTIVITAS GRAF
    # ============================================================
    print_subheader("d. Tentukan Apakah Graf Ini Connected. Jelaskan")
    
    is_connected = analyzer.is_connected()
    
    print(f"\n🔗 Hasil Analisis Konektivitas:")
    
    if is_connected:
        print(f"  ✓ Graf ini CONNECTED")
        print(f"\n  💡 Penjelasan:")
        print(f"     Graf dikatakan connected jika terdapat jalur antara")
        print(f"     setiap pasang simpul dalam graf. Dalam graf ini,")
        print(f"     setiap node dapat dicapai dari node lain melalui")
        print(f"     serangkaian edge yang ada.")
        
    else:
        print(f"  ✗ Graf ini TIDAK CONNECTED")
        print(f"\n  💡 Penjelasan:")
        print(f"     Graf tidak connected karena tidak semua simpul")
        print(f"     dapat dicapai dari simpul lain. Graf terdiri dari")
        print(f"     beberapa komponen terpisah.")
    
    # ============================================================
    # RINGKASAN HASIL
    # ============================================================
    print_header("RINGKASAN HASIL ANALISIS")
    
    print(f"\n📊 Informasi Graf:")
    print(f"  • Jumlah Node (Vertices) : {len(nodes)}")
    print(f"  • Jumlah Edge            : {len(edges)}")
    print(f"  • Tipe Graf              : Tak Berarah (Undirected)")
    print(f"  • Memiliki Cycle         : {'Ya' if has_cycle else 'Tidak'}")
    print(f"  • Connected              : {'Ya' if is_connected else 'Tidak'}")
    
    print(f"\n✓ Analisis selesai!")
    print("="*70)

# ============================================================
# MAIN PROGRAM
# ============================================================
if __name__ == "__main__":
    try:
        # ✅ Jalankan solusi soal 1
        soal1_solution()      
        print("\n✅ Program selesai!")
        
    except KeyboardInterrupt:
        print("\n\n⚠ Program dihentikan oleh user")
    except Exception as e:
        print(f"\n❌ Error tidak terduga: {str(e)}")
        import traceback
        traceback.print_exc()