# Modul 1 — Pengenalan Pemrograman dan Instalasi Lingkungan Kerja

## Tujuan Praktikum

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. Menjelaskan konsep dasar pemrograman dan algoritma.
2. Menginstal Python dan Visual Studio Code pada perangkat masing-masing.
3. Menulis dan menjalankan program Python sederhana tanpa error.
4. Menggunakan komentar pada kode program.

**Prasyarat:** tidak ada.  
**Estimasi waktu:** 2 jam (60 menit teori dan praktik terbimbing, 60 menit tugas).

---

## Dasar Teori

### 1. Apa itu Pemrograman dan Algoritma?

**Pemrograman** adalah proses menulis instruksi-instruksi yang akan dijalankan oleh komputer untuk menyelesaikan suatu masalah tertentu. Instruksi tersebut ditulis menggunakan bahasa pemrograman yang dapat dipahami oleh komputer.

**Algoritma** adalah urutan langkah-langkah logis dan sistematis untuk menyelesaikan suatu masalah. Algoritma bersifat independen terhadap bahasa pemrograman tertentu. Algoritma yang sama dapat diimplementasikan dalam berbagai bahasa pemrograman seperti Python, C, ataupun Java.

**Analogi sederhana:** algoritma dapat diibaratkan seperti resep masakan. Langkah-langkahnya harus diikuti secara berurutan agar menghasilkan masakan yang diinginkan. Bahasa pemrograman adalah "bahasa" yang digunakan untuk menuliskan resep tersebut agar dapat dipahami dan dijalankan oleh komputer.

### 2. Ciri-Ciri Algoritma yang Baik

- Memiliki input dan output yang jelas.
- Setiap langkah harus jelas dan tidak menimbulkan makna ganda (tidak ambigu).
- Memiliki batas akhir atau berhenti (*finite*), tidak berjalan tanpa henti.
- Efektif dan efisien dalam menyelesaikan masalah.

### 3. Mengenal Bahasa Pemrograman Python

Python adalah bahasa pemrograman tingkat tinggi (*high-level language*) yang bersifat *interpreted*, dinamis, dan mudah dipelajari. Python pertama kali dikembangkan oleh Guido van Rossum dan dirilis pada tahun 1991.

Beberapa alasan Python dipilih sebagai bahasa pengantar pemrograman bagi pemula:

- Sintaksnya sederhana dan mudah dibaca, mendekati bahasa manusia (bahasa Inggris).
- Bersifat *interpreted*, sehingga kode dapat langsung dijalankan tanpa proses kompilasi terpisah.
- Memiliki komunitas besar dan dokumentasi yang lengkap.
- Digunakan secara luas di berbagai bidang: pengembangan web, *data science*, kecerdasan buatan, otomasi, dan lain-lain.

### 4. Interpreter vs Compiler

Secara umum, bahasa pemrograman dijalankan melalui dua pendekatan:

| Aspek | Compiler | Interpreter |
|---|---|---|
| Proses eksekusi | Seluruh kode diterjemahkan sekaligus menjadi kode mesin sebelum dijalankan | Kode diterjemahkan dan dijalankan baris per baris |
| Contoh bahasa | C, C++, Pascal | Python, JavaScript |
| Deteksi error | Error terdeteksi setelah seluruh kode dikompilasi | Error terdeteksi langsung saat baris tersebut dijalankan |
| Kecepatan eksekusi | Umumnya lebih cepat | Umumnya lebih lambat, tetapi lebih mudah diuji |

### 5. Instalasi Python

Python dapat diunduh secara gratis melalui situs resmi <https://www.python.org/downloads/>. Berikut langkah instalasi pada sistem operasi Windows:

1. Buka browser dan akses situs <https://www.python.org/downloads/>.
2. Klik tombol **Download Python 3.x.x** (pilih versi terbaru yang stabil).
3. Jalankan file installer yang telah diunduh.
4. Pada jendela instalasi, centang kotak **Add Python to PATH** sebelum melanjutkan.
5. Klik **Install Now** dan tunggu proses instalasi hingga selesai.
6. Setelah selesai, buka Command Prompt (CMD) dan ketikkan perintah berikut untuk memastikan Python telah terinstal:

```text
python --version
```

Jika instalasi berhasil, perintah tersebut akan menampilkan versi Python yang terinstal, misalnya `Python 3.12.0`.

**Catatan untuk pengguna macOS/Linux:** pada macOS dan sebagian besar distribusi Linux, Python biasanya sudah terpasang secara default. Gunakan perintah `python3 --version` pada terminal untuk memeriksa versi yang terpasang. Jika belum ada, macOS dapat menginstal melalui <https://www.python.org/downloads/macos/>, sedangkan Linux dapat menggunakan perintah `sudo apt install python3` (Ubuntu/Debian).

### 6. Instalasi dan Pengenalan IDE (Visual Studio Code)

IDE (*Integrated Development Environment*) adalah aplikasi yang digunakan untuk menulis, menjalankan, dan men-debug kode program. Pada praktikum ini digunakan Visual Studio Code (VS Code) karena ringan, gratis, dan mendukung banyak bahasa pemrograman.

1. Unduh VS Code melalui <https://code.visualstudio.com/>.
2. Jalankan installer dan ikuti proses instalasi hingga selesai.
3. Buka VS Code, lalu buka menu **Extensions** (ikon kotak di sisi kiri) dan cari ekstensi **Python** dari Microsoft, kemudian klik **Install**.
4. Buat folder baru untuk menyimpan seluruh file praktikum, misalnya `praktikum-pemrograman`.
5. Buka folder tersebut melalui menu **File > Open Folder** di VS Code.

### 7. Struktur Dasar Program Python dan Komentar

Program Python ditulis dalam file berekstensi `.py`. Berikut adalah contoh struktur dasar program Python beserta penggunaan komentar:

```python
# Ini adalah komentar satu baris
# Program ini akan menampilkan tulisan ke layar
print("Hello, World!")  # menampilkan teks ke layar

"""
Ini adalah komentar
yang terdiri atas beberapa baris
"""
```

Beberapa hal penting mengenai sintaks dasar Python:

- Python bersifat *case-sensitive* (membedakan huruf besar dan kecil).
- Komentar satu baris ditulis menggunakan tanda pagar (`#`).
- Komentar banyak baris dapat ditulis menggunakan tiga tanda kutip (`""" ... """`).
- Python tidak memerlukan tanda titik koma (`;`) di akhir baris perintah.
- Python menggunakan indentasi (spasi atau tab di awal baris) untuk menentukan blok kode, bukan tanda kurung kurawal `{ }`.

### 8. Kesalahan Umum

| Kesalahan | Penyebab | Contoh | Perbaikan |
|---|---|---|---|
| `NameError` | Nama perintah salah eja atau huruf besar/kecil tidak sesuai | `Print("Halo")` | Gunakan `print("Halo")` |
| `SyntaxError` | Tanda kutip atau kurung tidak lengkap | `print("Halo` | Lengkapi menjadi `print("Halo")` |
| `IndentationError` | Indentasi tidak konsisten | Spasi di awal baris yang tidak diperlukan | Hapus atau samakan indentasi |
| File tidak berjalan | Ekstensi file bukan `.py` | `hello.txt` | Simpan sebagai `hello.py` |

### 9. Tips Praktikum

- Tulis kode sedikit demi sedikit, lalu jalankan.
- Baca pesan error dari **baris terakhir**; biasanya di situ letak masalahnya.
- Perhatikan tanda kutip, tanda kurung, dan huruf besar/kecil.
- Simpan file dengan akhiran `.py`.
- Biasakan memberi komentar singkat untuk menjelaskan tujuan program.

---

## Kegiatan Praktikum

### Percobaan 1 — Verifikasi Instalasi Python

**Tujuan:** memastikan Python telah terinstal dengan benar pada perangkat.

1. Buka Command Prompt atau terminal.
2. Ketikkan perintah berikut, lalu tekan Enter:

```text
python --version
```

3. Amati output yang muncul dan catat versi Python yang terinstal pada lembar laporan.

### Percobaan 2 — Program "Hello, World!"

**Tujuan:** menulis dan menjalankan program Python pertama.

1. Buka VS Code, buat file baru dengan nama `hello.py`.
2. Ketikkan kode berikut:

```python
print("Hello, World!")
```

3. Simpan file dengan `Ctrl+S`, kemudian jalankan program melalui terminal VS Code:

```text
python hello.py
```

4. Pastikan terminal menampilkan `Hello, World!`.

### Percobaan 3 — Menggunakan Komentar dan Beberapa Perintah `print()`

**Tujuan:** memahami penggunaan komentar dan beberapa baris perintah `print()`.

1. Buat file baru dengan nama `biodata.py`.
2. Ketikkan kode berikut:

```python
# Program menampilkan biodata sederhana
print("=== BIODATA MAHASISWA ===")
print("Nama  : Budi Santoso")
print("NIM   : 2026010001")
print("Prodi : Teknik Informatika")
```

3. Jalankan program dan amati hasilnya.
4. Tambahkan komentar sendiri sebelum salah satu perintah `print()`, lalu jalankan kembali. Pastikan program tetap berjalan normal karena baris komentar diabaikan oleh Python.

---

## Tugas Praktikum

Kerjakan setiap tugas pada file terpisah, misalnya `tugas1_1.py`, `tugas1_2.py`, dan seterusnya. Tugas konseptual dapat ditulis pada lembar laporan.

### Tugas 1.1 — Pemrograman dan Algoritma

Jelaskan dengan bahasa sendiri perbedaan antara **pemrograman** dan **algoritma**. Berikan satu contoh algoritma sederhana dari kehidupan sehari-hari.

**Ketentuan:** tulis jawaban minimal dua paragraf.

### Tugas 1.2 — Kelebihan Python

Sebutkan minimal tiga kelebihan bahasa Python dibandingkan bahasa pemrograman lain. Jelaskan alasan setiap kelebihan.

### Tugas 1.3 — Interpreter dan Compiler

Buat tabel perbandingan antara interpreter dan compiler. Sertakan minimal tiga aspek perbandingan dan satu contoh bahasa untuk masing-masing.

### Tugas 1.4 — Perbaiki Kode

Potongan kode berikut mengalami error. Salin, jalankan, catat pesan error, lalu perbaiki.

```python
Print("Selamat belajar Python")
```

**Ketentuan:** tuliskan penyebab error dan kode yang sudah diperbaiki.

### Tugas 1.5 — Puisi atau Pantun

Buat program Python yang menampilkan sebuah puisi atau pantun singkat minimal empat baris menggunakan beberapa perintah `print()`.

**Ketentuan:** gunakan minimal satu komentar untuk memberi judul program.

### Tugas 1.6 — Tantangan: Biodata Diri

Buat program Python yang menampilkan biodata diri secara lengkap, mencakup nama lengkap, NIM, program studi, tanggal lahir, alamat, dan hobi.

Gunakan komentar untuk memberi judul atau keterangan, dan buat tampilan output rapi dengan garis pembatas.

Contoh format output yang diharapkan:

```text
==============================
BIODATA DIRI
==============================
Nama                 : Budi Santoso
NIM                  : 2026010001
Prodi                : Teknik Informatika
Tempat, Tanggal Lahir: Sumenep, 1 Januari 2007
Alamat               : Jl. Pendidikan No. 1
Hobi                 : Membaca
==============================
```

**Ketentuan:** gunakan data diri sendiri dan hanya perintah `print()`. Tidak perlu meminta input.

---

## Ketentuan Pengumpulan

- File dikumpulkan dalam format laporan melalui <https://shorturl.at/OJKHx>.
- Nama file: `NIM_Nama_Pertemuan1.pdf`.
- Tugas dikumpulkan melalui <https://shorturl.at/T1rzg>.
- Tugas dikumpulkan paling lambat sebelum pertemuan praktikum berikutnya dimulai.

---

## Rangkuman

- Pemrograman adalah proses menulis instruksi agar komputer menyelesaikan masalah.
- Algoritma adalah urutan langkah logis dan sistematis untuk menyelesaikan masalah.
- Algoritma yang baik memiliki input/output jelas, tidak ambigu, berbatas, serta efektif dan efisien.
- Python adalah bahasa tingkat tinggi yang mudah dibaca dan dijalankan oleh interpreter.
- Python dapat diinstal dari situs resmi, sedangkan VS Code digunakan sebagai editor dan IDE.
- Program Python disimpan dalam file `.py` dan dijalankan dengan `python nama_file.py`.
- Komentar diawali `#` untuk satu baris atau diapit tiga tanda kutip untuk banyak baris.

## Istilah Penting

| Istilah | Arti |
|---|---|
| Pemrograman | Proses menulis instruksi untuk dijalankan komputer |
| Algoritma | Urutan langkah logis dan sistematis untuk menyelesaikan masalah |
| Interpreter | Program yang menerjemahkan dan menjalankan kode baris per baris |
| Compiler | Program yang menerjemahkan seluruh kode sebelum dijalankan |
| IDE | Aplikasi untuk menulis, menjalankan, dan men-debug kode |
| Script | File berisi kode Python, biasanya berakhiran `.py` |
| Komentar | Catatan pada kode yang tidak dijalankan oleh Python |

## Checklist Sebelum Lanjut

- [ ] Saya dapat menjelaskan perbedaan pemrograman dan algoritma.
- [ ] Saya dapat menyebutkan ciri-ciri algoritma yang baik.
- [ ] Saya sudah menginstal Python dan memeriksa versinya.
- [ ] Saya sudah menginstal VS Code dan ekstensi Python.
- [ ] Saya dapat menjalankan file `.py` dengan perintah `python nama_file.py`.
- [ ] Saya dapat menggunakan komentar satu baris dan banyak baris.
- [ ] Saya sudah mengerjakan seluruh tugas.

## Langkah Selanjutnya

Lanjutkan ke [Modul 2 — Variabel, Tipe Data, Operator, dan Ekspresi](modul-02-tipe-data-operator.md).
