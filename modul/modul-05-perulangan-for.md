# Modul 5 — Perulangan `for`

## Tujuan Praktikum

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. Menggunakan `for` untuk mengulang sejumlah data atau rentang tertentu.
2. Memakai `range()` dengan nilai awal, batas, dan langkah.
3. Menelusuri teks dan kumpulan data sederhana dengan `for`.
4. Mengendalikan perulangan dengan `break` dan `continue`.
5. Menyusun perulangan bersarang dan menghitung akumulasi nilai.

**Prasyarat:** Modul 1–4.  
**Estimasi waktu:** 1.5 jam (90 menit teori dan praktik terbimbing).

> Modul ini membahas `for`, yaitu perulangan untuk jumlah putaran yang sudah diketahui. Perulangan `while` dibahas di Modul 6.

---

## Dasar Teori

### 1. Konsep Perulangan

# berikan penjelasan tentang perulangan

Perulangan (Loop) adalah salah satu konsep dasar dalam pemrograman yang memungkinkan kita untuk mengeksekusi blok kode tertentu berulang kali selama kondisi tertentu terpenuhi. Perulangan sangat berguna ketika kita ingin melakukan tugas yang sama berkali-kali tanpa harus menulis kode yang sama berulang kali.

Ada dua jenis perulangan utama di Python: `for` dan `while`.

Pada modul ini kita menggunakan `for`, yaitu perulangan yang cocok ketika jumlah putaran atau kumpulan datanya sudah diketahui.

### 2. Perulangan `for`

`for` digunakan untuk menelusuri kumpulan data atau rentang tertentu.

Loop `for` dalam Python digunakan untuk mengulang blok kode tertentu untuk setiap item dalam urutan (seperti list, tuple, string, atau range). Sintaks dasar dari loop `for` adalah:

```python
 for item in urutan:
     # blok kode yang akan diulang
```

`for` loop akan mengambil setiap item dari urutan satu per satu dan mengeksekusi blok kode yang ada di dalamnya. Loop ini sangat berguna untuk iterasi melalui elemen-elemen dalam koleksi data atau rentang tertentu untuk melakukan operasi berulang.

```python
for huruf in "Python":
    print(huruf)
```

Output:

```text
P
y
t
h
o
n
```

item dalam loop `for` bisa berupa variabel yang menyimpan nilai dari elemen saat ini dalam urutan. Setelah semua item dalam urutan telah diproses, loop akan berhenti.

Contoh dengan daftar:

```python
buah = ["apel", "jeruk", "mangga"]

for item in buah:
    print(f"Saya suka {item}")
```

Output:

```text
Saya suka apel
Saya suka jeruk
Saya suka mangga
```

### 3. Fungsi `range()`

Fungsi `range()` dalam Python digunakan untuk menghasilkan urutan angka atau bilangan. Ketika digunakan dalam sebuah loop `for`, `range()` memungkinkan kita untuk mengulang blok kode sejumlah kali tertentu.

| Bentuk            | Hasil           |
| ----------------- | --------------- |
| `range(5)`        | `0, 1, 2, 3, 4` |
| `range(1, 6)`     | `1, 2, 3, 4, 5` |
| `range(0, 10, 2)` | `0, 2, 4, 6, 8` |
| `range(5, 0, -1)` | `5, 4, 3, 2, 1` |

fungsi range() memiliki beberapa bentuk penggunaan:

1.  `range(stop)`: Menghasilkan angka dari 0 hingga stop-1
2.  `range(start, stop)`: Menghasilkan angka dari start hingga stop-1
3.  `range(start, stop, step)`: Menghasilkan angka dari start hingga stop-1 dengan langkah tertentu

Contoh:

```python
for i in range(5):  # Menghasilkan angka 0, 1, 2, 3, 4
    print(i)
for i in range(1, 6):  # Menghasilkan angka 1, 2, 3, 4, 5
    print(i)
for i in range(1, 10, 2):  # Menghasilkan angka 1, 3, 5, 7, 9
    print(i)
for i in range(10, 0, -1):  # Menghasilkan angka 10, 9, 8, ..., 1
    print(i)
```

#### kenapa range dari 10 ke 0 tidak menampilkan angka 0?

Karena dalam fungsi `range(start, stop, step)`, angka yang dihasilkan akan berhenti sebelum mencapai nilai `stop`. Jadi, jika kita menggunakan `range(10, 0, -1)`, angka yang dihasilkan adalah 10, 9, 8, ..., 1. Angka 0 tidak termasuk karena `stop` adalah 0 dan `range()` berhenti sebelum mencapai nilai tersebut.

#### kenapa range(3) mulai dari 0 bukan dari 1?

Fungsi `range(stop)` secara default dimulai dari 0 karena ini adalah konvensi yang umum dalam pemrograman. Banyak bahasa pemrograman menggunakan indeks berbasis nol, yang berarti bahwa penghitungan dimulai dari 0. Jadi, ketika kita menggunakan `range(3)`, itu menghasilkan angka 0, 1, dan 2, bukan 1, 2, dan 3. Jika kita ingin memulai dari angka lain, kita bisa menggunakan `range(start, stop)` dengan menentukan nilai `start` yang diinginkan.

Contoh:

```python
for i in range(1, 6):
    print(f"Putaran ke-{i}")
```

Output:

```text
Putaran ke-1
Putaran ke-2
Putaran ke-3
Putaran ke-4
Putaran ke-5
```

Perhatikan bahwa batas akhir **tidak termasuk**.

### 4. Akumulator dan Pencacah

**Akumulator** menjumlahkan nilai. **Pencacah** menghitung banyaknya kejadian.

```python
total = 0
jumlah_data = 0

for angka in range(1, 6):
    total += angka
    jumlah_data += 1

print(f"Total: {total}")
print(f"Banyak data: {jumlah_data}")
print(f"Rata-rata: {total / jumlah_data}")
```

Output:

```text
Total: 15
Banyak data: 5
Rata-rata: 3.0
```

### 5. `break` dan `continue`

- `break` menghentikan perulangan sepenuhnya.
- `continue` melewati putaran saat ini dan lanjut ke putaran berikutnya.

```python
for angka in range(1, 8):
    if angka == 5:
        break
    print(angka)
```

Output:

```text
1
2
3
4
```

```python
for angka in range(1, 8):
    if angka % 2 == 0:
        continue
    print(angka)
```

Output:

```text
1
3
5
7
```

### 6. Perulangan Bersarang

Perulangan di dalam perulangan disebut _nested loop_. Setiap putaran luar menjalankan seluruh putaran dalam.

```python
for baris in range(1, 4):
    for kolom in range(1, 4):
        print(f"{baris * kolom:3}", end="")
    print()
```

Output:

```text
  1  2  3
  2  4  6
  3  6  9
```

`end=""` mencegah `print()` pindah baris. `print()` tanpa isi dipakai untuk pindah baris setelah satu baris selesai.

### 7. Perulangan dengan `else`

Python memiliki `else` pada perulangan. Blok ini dijalankan jika loop selesai **tanpa** `break`.

```python
angka = 9

for pembagi in range(2, angka):
    if angka % pembagi == 0:
        print("Bukan prima")
        break
else:
    print("Prima")
```

Output:

```text
Prima
```

Gunakan fitur ini secukupnya; jika membingungkan, gunakan variabel penanda seperti `adalah_prima = True`.

### 8. Kesalahan Umum

| Kesalahan              | Contoh                               | Akibat                             | Perbaikan                             |
| ---------------------- | ------------------------------------ | ---------------------------------- | ------------------------------------- |
| Salah batas `range`    | `range(1, 5)` untuk 1–5              | Angka 5 tidak ikut                 | Gunakan `range(1, 6)`                 |
| `break` terlalu awal   | `break` di luar `if`                 | Loop berhenti pada putaran pertama | Tempatkan `break` di dalam kondisi    |
| Indentasi salah        | Perintah di luar loop                | Hanya dijalankan sekali            | Periksa indentasi                     |
| Mengubah variabel loop | `i += 1` di dalam `for`              | Hasil tidak seperti harapan        | Jangan ubah variabel loop             |
| Salah urutan nested    | Loop dalam ditulis di luar loop luar | `IndentationError`                 | Masukkan loop dalam ke blok loop luar |

### 9. Tips

- Gunakan `for` ketika jumlah putaran atau kumpulan datanya sudah diketahui.
- Tentukan nilai awal dan batas `range()` dengan cermat.
- Uji dengan data kecil, misalnya `n = 3`, sebelum data besar.
- Gunakan nama variabel yang jelas: `total`, `jumlah`, `baris`, `kolom`.

### 10. Contoh Implementasi

Beberapa contoh penerapan materi modul ini dalam kasus kecil.

**1. Menjumlahkan angka 1 sampai n**

```python
n = int(input("Masukkan n: "))
total = 0

for angka in range(1, n + 1):
    total += angka

print(f"Jumlah 1 sampai {n}: {total}")
```

Contoh interaksi:

```text
Masukkan n: 5
Jumlah 1 sampai 5: 15
```

**2. Tabel penjumlahan dengan perulangan bersarang**

```python
for baris in range(1, 4):
    for kolom in range(1, 4):
        print(f"{baris + kolom:3}", end="")
    print()
```

Output:

```text
  2  3  4
  3  4  5
  4  5  6
```

**3. Melewati angka genap dengan `continue`**

```python
for angka in range(1, 11):
    if angka % 2 == 0:
        continue
    print(angka, end=" ")
print()
```

Output:

```text
1 3 5 7 9
```

---

## Tugas Praktikum

Simpan setiap tugas sebagai file terpisah, misalnya `tugas5_1.py`.

### Tugas 5.1 — Deret Angka

Minta bilangan bulat positif `n`, lalu tampilkan angka 1 sampai `n`, jumlahnya, dan rata-ratanya.

Contoh interaksi:

```text
Masukkan n: 5
Deret: 1 2 3 4 5
Jumlah: 15
Rata-rata: 3.00
```

**Ketentuan:** gunakan `for` dan `range()`. Tampilkan rata-rata dua angka di belakang koma.

### Tugas 5.2 — Faktorial

Minta bilangan bulat `n` (minimal 1), lalu hitung `n!`.

Contoh:

```text
Masukkan n: 5
5! = 120
```

**Ketentuan:** gunakan perulangan, bukan fungsi bawaan. Tampilkan juga prosesnya bila memungkinkan:

```text
1 x 2 x 3 x 4 x 5 = 120
```

### Tugas 5.3 — Tabel Perkalian

Minta satu bilangan `n`, lalu tampilkan tabel perkalian `n x 1` sampai `n x 10`.

Contoh interaksi:

```text
Masukkan n: 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```

**Ketentuan:** gunakan `for` dan `range(1, 11)`.

### Tugas 5.4 — Bilangan Prima

Minta bilangan bulat `n`, lalu tentukan apakah `n` prima.

Contoh interaksi:

```text
Masukkan bilangan: 29
29 adalah bilangan prima.
```

```text
Masukkan bilangan: 30
30 bukan bilangan prima.
```

**Ketentuan:**

- Angka kurang dari 2 bukan prima.
- Gunakan perulangan untuk memeriksa pembagi.
- Gunakan `break` ketika pembagi ditemukan.
- Uji dengan `1`, `2`, `9`, `29`, dan `30`.

### Tugas 5.5 — Pola Bintang

Minta tinggi pola, lalu tampilkan segitiga bintang.

Contoh interaksi:

```text
Masukkan tinggi: 5
*
**
***
****
*****
```

**Ketentuan:** gunakan perulangan bersarang atau operator `*` pada string. Setelah segitiga naik, tampilkan juga segitiga turun.

Contoh tambahan:

```text
*****
****
***
**
*
```

### Tugas 5.6 — Tantangan: Deret Fibonacci

Deret Fibonacci dimulai dengan `0` dan `1`. Setiap angka berikutnya adalah jumlah dua angka sebelumnya.

```text
0, 1, 1, 2, 3, 5, 8, 13, ...
```

Minta bilangan bulat `n` (minimal 1), lalu tampilkan `n` angka pertama dan jumlahnya.

Contoh interaksi:

```text
Masukkan n: 7
Deret: 0 1 1 2 3 5 8
Jumlah: 20
```

**Ketentuan:**

- Gunakan `for` dan `range()`.
- Gunakan dua variabel untuk menyimpan dua angka terakhir.
- Hitung angka berikutnya tanpa menggunakan list.
- Tampilkan deret dalam satu baris dan jumlah seluruh angka.
- Uji dengan `n = 1`, `n = 2`, dan `n = 7`.

---

## Rangkuman

- `for` dipakai untuk menelusuri data atau rentang yang sudah diketahui.
- `range(awal, batas, langkah)` menghasilkan urutan bilangan; batas tidak termasuk.
- Akumulator menjumlahkan nilai, pencacah menghitung kejadian.
- `break` menghentikan loop, `continue` melewati satu putaran.
- Nested loop berguna untuk tabel dan pola, tetapi hati-hati dengan jumlah putarannya.
- `for-else` menjalankan blok `else` hanya jika loop selesai tanpa `break`.

## Istilah Penting

| Istilah     | Arti                                                         |
| ----------- | ------------------------------------------------------------ |
| Iterasi     | Satu kali putaran perulangan                                 |
| Akumulator  | Variabel penjumlah nilai                                     |
| Pencacah    | Variabel penghitung jumlah kejadian                          |
| Nested loop | Perulangan di dalam perulangan                               |
| `range`     | Fungsi pembuat urutan bilangan                               |
| `for-else`  | Blok `else` yang berjalan bila loop tidak dihentikan `break` |

## Checklist Sebelum Lanjut

- [ ] Saya dapat menggunakan `for` untuk rentang angka.
- [ ] Saya dapat menggunakan `range()` dengan benar.
- [ ] Saya dapat membuat akumulator dan pencacah.
- [ ] Saya dapat menggunakan `break` dan `continue`.
- [ ] Saya dapat menulis perulangan bersarang sederhana.
- [ ] Saya sudah mengerjakan seluruh tugas.

## Langkah Selanjutnya

Lanjutkan ke [Modul 6 — Perulangan `while`](modul-06-perulangan-while.md).
