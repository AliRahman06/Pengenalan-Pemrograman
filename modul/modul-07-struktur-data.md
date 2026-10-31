# Modul 7 — Struktur Data

## Tujuan Praktikum

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. Menggunakan `list` untuk menyimpan banyak data berurutan.
2. Menggunakan `tuple` untuk data yang tidak boleh diubah.
3. Menggunakan `dict` untuk menyimpan pasangan kunci–nilai.
4. Menggunakan `set` untuk data unik dan operasi himpunan.
5. Mengakses, menambah, mengubah, dan menghapus elemen struktur data.
6. Menelusuri struktur data dengan perulangan.

**Prasyarat:** Modul 1–6.  
**Estimasi waktu:** 1.5 jam (90 menit teori dan praktik terbimbing).

---

## Dasar Teori

### 1. Mengapa Perlu Struktur Data?

Variabel tunggal cocok untuk satu nilai. Namun, jika kita memiliki 100 nilai, membuat `nilai1`, `nilai2`, sampai `nilai100` tidak praktis. Struktur data memungkinkan banyak nilai disimpan dalam satu wadah.

Bayangkan struktur data seperti lemari dengan kompartemen berbeda: ada lemari berurutan (`list`), lemari terkunci (`tuple`), buku alamat (`dict`), dan kantong benda unik (`set`).

### 2. `list`

`list` adalah kumpulan data **berurutan** dan **dapat diubah**. Ditulis dengan tanda kurung siku `[]`.

```python
buah = ["apel", "jeruk", "mangga"]
print(buah)
print(buah[0])
print(buah[-1])
```

Output:

```text
['apel', 'jeruk', 'mangga']
apel
mangga
```

Indeks dimulai dari `0`. Indeks negatif menghitung dari belakang: `-1` adalah elemen terakhir.

**Slicing** mengambil sebagian list:

```python
angka = [10, 20, 30, 40, 50]
print(angka[1:4])
print(angka[:2])
print(angka[3:])
```

Output:

```text
[20, 30, 40]
[10, 20]
[40, 50]
```

**Method penting pada list:**

| Method         | Fungsi                                  | Contoh                    |
| -------------- | --------------------------------------- | ------------------------- |
| `append(x)`    | Menambah di akhir                       | `buah.append("pisang")`   |
| `insert(i, x)` | Menyisipkan di indeks                   | `buah.insert(1, "melon")` |
| `remove(x)`    | Menghapus nilai tertentu                | `buah.remove("apel")`     |
| `pop()`        | Menghapus dan mengambil elemen terakhir | `buah.pop()`              |
| `sort()`       | Mengurutkan                             | `angka.sort()`            |
| `reverse()`    | Membalik urutan                         | `angka.reverse()`         |
| `count(x)`     | Menghitung kemunculan                   | `angka.count(20)`         |

Fungsi bawaan yang sering dipakai: `len()`, `sum()`, `min()`, `max()`.

```python
nilai = [80, 90, 75, 85]
print(len(nilai))
print(sum(nilai))
print(max(nilai))
print(min(nilai))
print(85 in nilai)
```

Output:

```text
4
330
90
75
True
```

### 3. `tuple`

`tuple` mirip `list`, tetapi **tidak dapat diubah** setelah dibuat. Ditulis dengan tanda kurung biasa `()`.

```python
koordinat = (10, 20)
print(koordinat[0])
```

Output:

```text
10
```

Jika mencoba mengubah elemen:

```python
koordinat[0] = 15
```

Muncul `TypeError: 'tuple' object does not support item assignment`.

Tuple cocok untuk data tetap, misalnya koordinat, data identitas, atau nilai yang dikembalikan fungsi.

**Unpacking:**

```python
x, y = (10, 20)
print(x)
print(y)
```

Output:

```text
10
20
```

### 4. `dict`

`dict` menyimpan data dalam pasangan **kunci: nilai**. Kunci harus unik.

```python
mahasiswa = {
    "nama": "Ayu",
    "nim": "2401001",
    "nilai": 88
}

print(mahasiswa["nama"])
print(mahasiswa.get("nim"))
print(mahasiswa.get("alamat", "Tidak ada data"))
```

Output:

```text
Ayu
2401001
Tidak ada data
```

**Menambah dan mengubah data:**

```python
mahasiswa["alamat"] = "Bandung"
mahasiswa["nilai"] = 90
print(mahasiswa)
```

Output:

```text
{'nama': 'Ayu', 'nim': '2401001', 'nilai': 90, 'alamat': 'Bandung'}
```

**Menghapus data:**

```python
del mahasiswa["alamat"]
```

**Menelusuri dict:**

```python
for kunci, nilai in mahasiswa.items():
    print(f"{kunci}: {nilai}")
```

Output:

```text
nama: Ayu
nim: 2401001
nilai: 90
```

Method penting: `keys()`, `values()`, `items()`, `get()`, `update()`, `pop()`.

Gunakan `get()` agar tidak muncul `KeyError` ketika kunci tidak ada.

### 5. `set`

`set` adalah kumpulan data **unik** dan **tidak berurutan**. Ditulis dengan `{}`.

```python
buah_unik = {"apel", "jeruk", "apel", "mangga"}
print(buah_unik)
```

Output (urutan bisa berbeda):

```text
{'jeruk', 'apel', 'mangga'}
```

Karena tidak berurutan, `set` tidak mendukung indeks seperti `buah_unik[0]`.

**Operasi himpunan:**

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)
print(a & b)
print(a - b)
print(a ^ b)
```

Output:

```text
{1, 2, 3, 4, 5, 6}
{3, 4}
{1, 2}
{1, 2, 5, 6}
```

| Operasi              | Simbol                     | Arti                                 |
| -------------------- | -------------------------- | ------------------------------------ | ------------- |
| Union                | `                          | `atau`.union()`                      | Semua anggota |
| Intersection         | `&` atau `.intersection()` | Anggota bersama                      |
| Difference           | `-` atau `.difference()`   | Anggota `a` yang tidak ada di `b`    |
| Symmetric difference | `^`                        | Anggota yang hanya ada di salah satu |

Method: `add()`, `remove()`, `discard()`, `clear()`.

### 6. Struktur Data Bersarang

List dapat berisi list, dan dict dapat berisi list atau dict.

```python
siswa = [
    {"nama": "Ayu", "nilai": 88},
    {"nama": "Budi", "nilai": 75}
]

for data in siswa:
    print(f"{data['nama']} mendapat nilai {data['nilai']}")
```

Output:

```text
Ayu mendapat nilai 88
Budi mendapat nilai 75
```

**Matriks** sebagai list bersarang:

```python
matriks = [
    [1, 2],
    [3, 4]
]
print(matriks[1][0])
```

Output:

```text
3
```

### 7. List Comprehension (Pengayaan)

List comprehension membuat list baru secara ringkas.

```python
angka = [1, 2, 3, 4, 5]
kuadrat = [x ** 2 for x in angka]
print(kuadrat)
```

Output:

```text
[1, 4, 9, 16, 25]
```

Dengan filter:

```python
genap = [x for x in angka if x % 2 == 0]
print(genap)
```

Output:

```text
[2, 4]
```

### 8. Kesalahan Umum

| Kesalahan              | Contoh                          | Akibat                      | Perbaikan                                 |
| ---------------------- | ------------------------------- | --------------------------- | ----------------------------------------- |
| Indeks di luar batas   | `buah[5]` pada list 3 elemen    | `IndexError`                | Periksa `len()` atau gunakan indeks valid |
| Kunci tidak ada        | `data["alamat"]`                | `KeyError`                  | Gunakan `get()` atau periksa `in`         |
| Mengubah tuple         | `t[0] = 1`                      | `TypeError`                 | Gunakan list bila data perlu diubah       |
| Salah memakai `append` | `buah.append(["pisang"])`       | Menambah list di dalam list | Gunakan `append("pisang")`                |
| Menghapus saat iterasi | `for x in data: data.remove(x)` | Sebagian data terlewat      | Iterasi salinan atau kumpulkan lalu hapus |
| `set` diindeks         | `s[0]`                          | `TypeError`                 | Ubah ke list bila perlu urutan            |

### 9. Tips

- Pilih struktur data sesuai kebutuhan:
  - Butuh urutan dan perubahan → `list`.
  - Butuh data tetap → `tuple`.
  - Butuh pencarian berdasarkan kunci → `dict`.
  - Butuh data unik → `set`.
- Gunakan nama variabel jamak untuk kumpulan data: `nilai`, `mahasiswa`, `barang`.
- Tampilkan isi struktur data saat pengembangan untuk memastikan bentuknya benar, misalnya `print(data)`.

### 10. Contoh Implementasi

Beberapa contoh penerapan materi modul ini dalam kasus kecil.

**1. Statistik nilai dengan `list`**

```python
nilai = []

for i in range(3):
    nilai.append(float(input(f"Nilai ke-{i + 1}: ")))

print(f"Daftar nilai: {nilai}")
print(f"Total: {sum(nilai)}")
print(f"Rata-rata: {sum(nilai) / len(nilai):.2f}")
print(f"Tertinggi: {max(nilai)}")
print(f"Terendah: {min(nilai)}")
```

Contoh interaksi:

```text
Nilai ke-1: 80
Nilai ke-2: 90
Nilai ke-3: 75
Daftar nilai: [80.0, 90.0, 75.0]
Total: 245.0
Rata-rata: 81.67
Tertinggi: 90.0
Terendah: 75.0
```

**2. Data mahasiswa dengan `dict`**

```python
mahasiswa = {"nama": "Ayu", "nim": "2401001", "nilai": 88}

print(mahasiswa["nama"])
print(mahasiswa.get("alamat", "Tidak ada data"))

for kunci, nilai in mahasiswa.items():
    print(f"{kunci}: {nilai}")
```

Output:

```text
Ayu
Tidak ada data
nama: Ayu
nim: 2401001
nilai: 88
```

**3. Operasi himpunan dengan `set`**

```python
kelas_a = {"Ayu", "Budi", "Citra"}
kelas_b = {"Citra", "Dina", "Eka"}

print(f"Semua peserta: {kelas_a | kelas_b}")
print(f"Kedua kelas: {kelas_a & kelas_b}")
print(f"Hanya kelas A: {kelas_a - kelas_b}")
```

Contoh output (urutan bisa berbeda):

```text
Semua peserta: {'Eka', 'Dina', 'Ayu', 'Citra', 'Budi'}
Kedua kelas: {'Citra'}
Hanya kelas A: {'Ayu', 'Budi'}
```

---

## Tugas Praktikum

Simpan setiap tugas sebagai file terpisah, misalnya `tugas7_1.py`.

### Tugas 7.1 — Statistik Nilai

Minta 5 nilai mahasiswa, simpan dalam `list`, lalu tampilkan:

- daftar nilai,
- total,
- rata-rata,
- nilai tertinggi dan terendah,
- banyak nilai di atas rata-rata.

Contoh interaksi:

```text
Nilai ke-1: 80
Nilai ke-2: 90
Nilai ke-3: 70
Nilai ke-4: 85
Nilai ke-5: 75
Daftar nilai: [80.0, 90.0, 70.0, 85.0, 75.0]
Total: 400.0
Rata-rata: 80.00
Tertinggi: 90.0
Terendah: 70.0
Di atas rata-rata: 2
```

**Ketentuan:** gunakan `list`, `append()`, `sum()`, `len()`, `max()`, dan `min()`.

### Tugas 7.2 — Buku Kontak

Buat `dict` kontak awal:

```python
kontak = {
    "Ayu": "081234567890",
    "Budi": "082345678901",
    "Citra": "083456789012"
}
```

Program harus:

1. Menampilkan seluruh kontak.
2. Meminta nama yang dicari, lalu menampilkan nomornya atau `Kontak tidak ditemukan`.
3. Meminta nama dan nomor baru, lalu menambahkannya.
4. Menampilkan seluruh kontak setelah penambahan.

Contoh interaksi:

```text
Daftar kontak:
Ayu: 081234567890
Budi: 082345678901
Citra: 083456789012
Cari nama: Budi
Nomor Budi: 082345678901
Nama baru: Dina
Nomor Dina: 084567890123
Kontak Dina ditambahkan.
```

**Ketentuan:** gunakan `get()` untuk pencarian.

### Tugas 7.3 — Frekuensi Kata

Minta satu kalimat, lalu hitung berapa kali setiap kata muncul. Abaikan perbedaan huruf besar dan kecil.

Contoh interaksi:

```text
Masukkan kalimat: saya suka python dan saya suka belajar
saya: 2
suka: 2
python: 1
dan: 1
belajar: 1
```

**Ketentuan:**

- Gunakan `split()` untuk memecah kalimat.
- Gunakan `casefold()` atau `lower()`.
- Simpan hasil dalam `dict`.
- Tampilkan setiap kata dan jumlahnya menggunakan `items()`.

### Tugas 7.4 — Operasi Himpunan

Dua kelas mengikuti kegiatan ekstrakurikuler.

```python
kelas_a = {"Ayu", "Budi", "Citra", "Dina"}
kelas_b = {"Citra", "Dina", "Eka", "Fajar"}
```

Tampilkan:

1. Semua peserta dari kedua kelas.
2. Peserta yang mengikuti kedua kegiatan.
3. Peserta yang hanya ada di kelas A.
4. Peserta yang hanya ada di salah satu kelas.

Contoh output:

```text
Semua peserta: {'Ayu', 'Budi', 'Citra', 'Dina', 'Eka', 'Fajar'}
Peserta kedua kegiatan: {'Citra', 'Dina'}
Hanya kelas A: {'Ayu', 'Budi'}
Hanya di salah satu: {'Ayu', 'Budi', 'Eka', 'Fajar'}
```

**Ketentuan:** gunakan operasi `set`, bukan perulangan manual. Urutan output boleh berbeda.

### Tugas 7.5 — Penjumlahan Matriks

Diberikan dua matriks 2×2:

```python
matriks_a = [
    [1, 2],
    [3, 4]
]

matriks_b = [
    [5, 6],
    [7, 8]
]
```

Hitung dan tampilkan hasil penjumlahannya.

Contoh output:

```text
Hasil penjumlahan:
6 8
10 12
```

**Ketentuan:** gunakan perulangan bersarang dan indeks `matriks[i][j]`.

### Tugas 7.6 — Tantangan: Inventaris Barang

Buat program inventaris sederhana dengan data awal:

```python
barang = [
    {"nama": "Pena", "harga": 3000, "stok": 10},
    {"nama": "Buku", "harga": 5000, "stok": 5},
    {"nama": "Penggaris", "harga": 4000, "stok": 8}
]
```

Program memiliki menu berulang:

```text
=== INVENTARIS ===
1. Lihat barang
2. Tambah barang
3. Cari barang
4. Ubah stok
5. Hapus barang
6. Total nilai inventaris
0. Keluar
Pilihan:
```

**Ketentuan:**

- Gunakan `while` untuk menu dan `if-elif` untuk pilihan.
- Pilihan 1 menampilkan semua barang beserta harga dan stok.
- Pilihan 2 meminta nama, harga, dan stok, lalu menambahkan `dict` baru.
- Pilihan 3 mencari berdasarkan nama (tanpa membedakan huruf besar/kecil).
- Pilihan 4 mengubah stok barang tertentu.
- Pilihan 5 menghapus barang berdasarkan nama.
- Pilihan 6 menghitung total `harga * stok` seluruh barang.
- Tangani nama barang yang tidak ditemukan.
- Pilihan `0` menghentikan program.

Contoh tampilan:

```text
Nama: Pena | Harga: Rp3,000 | Stok: 10
Nama: Buku | Harga: Rp5,000 | Stok: 5
Nama: Penggaris | Harga: Rp4,000 | Stok: 8
Total nilai inventaris: Rp87,000
```

---

## Rangkuman

- `list` berurutan dan dapat diubah; indeks dimulai dari 0.
- `tuple` berurutan tetapi tidak dapat diubah.
- `dict` menyimpan pasangan kunci–nilai dan cocok untuk pencarian.
- `set` menyimpan data unik serta mendukung operasi himpunan.
- Struktur data dapat bersarang, misalnya list berisi dict atau matriks.
- Pilih struktur data berdasarkan kebutuhan, bukan kebiasaan.

## Istilah Penting

| Istilah | Arti                                    |
| ------- | --------------------------------------- |
| Elemen  | Satu nilai di dalam struktur data       |
| Indeks  | Posisi elemen, dimulai dari 0           |
| Slicing | Mengambil sebagian list                 |
| Kunci   | Nama penanda pada `dict`                |
| Nilai   | Isi yang dipasangkan dengan kunci       |
| Unik    | Tidak ada duplikat                      |
| Matriks | Kumpulan data berbentuk baris dan kolom |

## Checklist Sebelum Lanjut

- [ ] Saya dapat membuat dan mengubah `list`.
- [ ] Saya dapat menggunakan `tuple` dan menjelaskan bedanya dengan `list`.
- [ ] Saya dapat membuat, mencari, dan memperbarui data pada `dict`.
- [ ] Saya dapat menggunakan `set` dan operasi himpunan.
- [ ] Saya dapat menelusuri struktur data bersarang.
- [ ] Saya sudah mengerjakan seluruh tugas.

## Langkah Selanjutnya

Lanjutkan ke [Modul 8 — Fungsi dan Modul](modul-08-fungsi-dan-modul.md).
