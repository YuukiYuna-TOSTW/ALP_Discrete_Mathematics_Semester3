# 📚 ALP Discrete Mathematics Semester 3 - Program Analisis Graf

Program pembelajaran interaktif untuk memahami konsep **Graf (Graph)** dalam Matematika Diskrit dengan visualisasi dan analisis mendalam.

---

## 📋 Daftar Isi
1. [Cara Kerja](#cara-kerja)
2. [Apa Saja yang Ada](#apa-saja-yang-ada)
3. [Kegunaan dari Kode](#kegunaan-dari-kode)

---

## 🔧 Cara Kerja

### Alur Program Utama

Program ini bekerja dengan sistem **menu interaktif** yang memandu pengguna melalui berbagai operasi graf:

```
START
  ↓
[Menu Utama]
  ├── Soal 1: Graf Tak Berarah
  │    ├── Input nodes (V) dan edges (E)
  │    ├── Visualisasi graf
  │    ├── Analisis derajat setiap node
  │    ├── Deteksi cycle
  │    └── Cek apakah graf connected
  │
  ├── Soal 2: Graf Berbobot
  │    ├── Input nodes dan weighted edges
  │    ├── Visualisasi graf berbobot
  │    ├── BFS (Breadth-First Search)
  │    ├── DFS (Depth-First Search)
  │    └── Dijkstra's Algorithm (Shortest Path)
  │
  └── [Exit]
```

### Komponen Utama

#### 1. **GraphClass.py** (Kelas Graf)
- **Inisialisasi**: Membuat graph directed atau undirected menggunakan NetworkX
- **Add Nodes**: Menambahkan simpul dengan support tipe data (String, Integer, Float)
- **Add Edges**: Menambahkan sisi dengan atau tanpa bobot
- **Analisis Graph**:
  - `get_node_degree()` → Menghitung derajat setiap node
  - `find_cycles()` → Mendeteksi cycle dalam graf
  - `is_connected()` → Mengecek konektivitas graf
  - `bfs()` → Traversal Breadth-First Search
  - `dfs()` → Traversal Depth-First Search (Rekursif)
  - `dijkstra()` → Algoritma Dijkstra untuk shortest path
- **Visualisasi**: Menggunakan PyVis untuk membuat HTML interactive visualization

#### 2. **AnotherClass.py** (Kelas Tambahan)
- Menyediakan utility functions untuk:
  - Input validation
  - Data formatting
  - Helper functions untuk analisis tambahan

#### 3. **Soal1.py** (Study Case 1 - Graf Tak Berarah)
- **Kasus**: Diberikan graf `G = (V, E)` dengan 6 simpul (A-F) dan 7 sisi
- **Analisis**:
  - Menghitung derajat setiap simpul
  - Menemukan cycle dalam graf
  - Menentukan konektivitas graf
- **Output**: Visualisasi HTML dan hasil analisis di terminal

#### 4. **Soal2.py** (Study Case 2 - Graf Berbobot)
- **Kasus**: Diberikan graf berbobot dengan 7 simpul (A-G) dan weighted edges
- **Analisis**:
  - BFS traversal dari simpul A
  - DFS traversal dari simpul A (dengan urutan alfabet)
  - Dijkstra algorithm untuk jalur terpendek A → G
- **Output**: Visualisasi HTML dan hasil analisis di terminal

#### 5. **main.py** (Program Utama)
- Menu interaktif untuk menjalankan kedua study case
- Menampilkan welcome screen dengan informasi program
- Navigasi antar soal dan opsi analisis

---

## 📁 Apa Saja yang Ada

### File Utama
```
├── main.py                          # Program utama dengan menu interaktif
├── GraphClass.py                    # Kelas untuk membuat dan analisis graf
├── AnotherClass.py                  # Kelas utility dan helper functions
├── Soal1.py                         # Study Case 1: Graf Tak Berarah (6 nodes)
├── Soal2.py                         # Study Case 2: Graf Berbobot (7 nodes)
└── README.md                        # File dokumentasi (file ini)
```

### File Output (HTML Visualization)
```
├── custom_weighted_graph.html       # Visualisasi graf berbobot custom
├── soal2_graf_visualisasi.html      # Visualisasi Soal 2 lengkap
└── soal2_shortest_path_A_to_G.html  # Visualisasi jalur terpendek Soal 2
```

### Library & Dependencies
```
lib/
├── bindings/
│   └── utils.js                     # JavaScript utilities
├── tom-select/
│   ├── tom-select.complete.min.js   # Tom Select library (dropdown)
│   └── tom-select.css               # Tom Select styling
└── vis-9.1.2/
    ├── vis-network.min.js           # Vis.js network visualization
    └── vis-network.css              # Vis.js network styling
```

### Dependencies Python
- **networkx** - Pembuatan dan analisis struktur graf
- **pyvis** - Visualisasi graf interaktif (HTML output)

---

## 🎯 Kegunaan dari Kode

### 1. **Pembelajaran Matematika Diskrit**
Program ini dirancang untuk membantu pemahaman konsep-konsep penting dalam Discrete Mathematics:
- **Teori Graf**: Definisi, representasi, dan properti graf
- **Graph Properties**: Degree, cycle, connected components
- **Graph Algorithms**: BFS, DFS, Dijkstra
- **Weighted Graphs**: Konsep bobot sisi dan shortest path

### 2. **Visualisasi Interaktif**
- Setiap graf ditampilkan dalam format HTML interaktif
- Pengguna dapat zoom, drag nodes, dan explore struktur graf
- Membantu pemahaman visual struktur data yang kompleks

### 3. **Analisis Otomatis**
Kode secara otomatis menghitung:
- **Derajat Simpul**: Jumlah sisi yang terhubung ke setiap node
- **Cycle Detection**: Menemukan semua cycle dalam graf
- **Konektivitas**: Mengecek apakah graf connected atau tidak
- **Shortest Path**: Menentukan rute terpendek dengan Dijkstra
- **Traversal Order**: Urutan kunjungan BFS dan DFS

### 4. **Study Cases Praktis**
- **Soal 1**: Menganalisis struktur graf sederhana (undirected, 6 nodes)
- **Soal 2**: Menyelesaikan masalah kompleks dengan graf berbobot (7 nodes, weighted edges)

### 5. **Flexible Graph Input**
Kode mendukung berbagai format input:
- Node identifier: String (`A`, `B`, `C`) atau Integer (`1`, `2`, `3`)
- Edge format: `(u, v)` untuk undirected atau `(u, v, weight)` untuk weighted
- Bobot dapat berupa integer atau float

### 6. **Terminal & Web Output**
- **Terminal Output**: Hasil analisis ditampilkan dalam format tabel dan teks
- **HTML Output**: Visualisasi interaktif disimpan sebagai file `.html`
- Auto-open di browser untuk kemudahan viewing

---

## 🚀 Cara Menggunakan

### 1. Install Dependencies
```bash
pip install networkx pyvis
```

### 2. Jalankan Program
```bash
python main.py
```

### 3. Pilih Menu
- Menu akan menampilkan opsi untuk Soal 1 atau Soal 2
- Ikuti prompt di terminal
- Output HTML akan otomatis dibuka di browser

### 4. Interpretasi Hasil
- Periksa visualisasi graf di browser
- Baca hasil analisis di terminal (degree, cycles, paths)
- Gunakan untuk belajar dan memahami konsep

---

## 📊 Contoh Output

### Terminal Output
```
======================================================================
                     SOAL 1 - GRAF TAK BERARAH
======================================================================

📋 Data Graf:
  V = {A, B, C, D, E, F}
  E = {(A,B), (A,C), (B,D), (C,E), (D,E), (E,F), (C,F)}

✓ Derajat Setiap Simpul:
  • Node A: degree = 2
  • Node B: degree = 2
  • Node C: degree = 3
  • Node D: degree = 2
  • Node E: degree = 3
  • Node F: degree = 2

✓ Cycle Detection:
  Cycle ditemukan: ['A', 'B', 'D', 'E', 'C', 'A']
```

### HTML Visualization
- Interaktif graph dengan nodes dan edges
- Warna dan layout untuk kemudahan visualisasi
- Informasi tooltip saat hover pada nodes/edges

---

## 📝 Catatan Penting

1. **Python Version**: Gunakan Python 3.7+
2. **Internet Access**: Diperlukan untuk membuka HTML files di browser
3. **Node Identifier**: Dapat berupa kombinasi string dan angka (e.g., `A1`, `Node2`)
4. **Graph Type**: 
   - Undirected: Untuk Soal 1
   - Directed/Weighted: Untuk Soal 2

---

## 🎓 Materi Pembelajaran

Setiap bagian program mengajarkan:
- **Basic Graph Theory**: V, E, degree, edges, vertices
- **Graph Traversal**: BFS & DFS algorithms
- **Shortest Path**: Dijkstra's algorithm
- **Graph Properties**: Connectivity, cycles
- **Visualization**: Mewujudkan teori menjadi visual

---

**Created for**: ALP (Algoritma dan Pemrograman) - Discrete Mathematics Semester 3
**Status**: Educational Project ✓
