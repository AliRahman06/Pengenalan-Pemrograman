# Modul 6 — Perulangan `while`

## Tujuan Praktikum

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. Menggunakan `while` untuk mengulang selama kondisi bernilai `True`.
2. Membuat pencacah dan akumulator pada perulangan `while`.
3. Menggunakan nilai sentinel untuk menghentikan perulangan.
4. Membuat validasi input berulang sampai data benar.
5. Menghindari perulangan tak berujung dan memilih antara `for` dan `while`.

**Prasyarat:** Modul 1–5.  
**Estimasi waktu:** 2–3 jam.

> `for` cocok ketika jumlah putaran sudah diketahui. `while` cocok ketika perulangan bergantung pada kondisi yang dapat berubah, misalnya menunggu pengguna memasukkan nilai yang benar.

---

## Dasar Teori

### 1. Konsep `while`

`while` mengulang blok kode **selama** kondisinya bernilai `True`.

```python
hitung = 1

while hitung <= 3:
    print(f"Hitung: {hitung}")
    hitung += 1
```

Output:

```text
Hitung: 1
Hitung: 2
Hitung: 3
```

Alur:

1. Periksa kondisi `hitung <= 3`.
2. Jika `True`, jalankan isi loop.
3. Setelah isi selesai, periksa kondisi lagi.
4. Jika `False`, loop berhenti.

### 2. Mengubah Variabel Agar Loop Berhenti

Variabel yang dipakai pada kondisi harus berubah di dalam loop.

```python
angka = 5

while angka > 0:
    print(angka)
    angka -= 1

print("Selesai!")
```

Output:

```text
5
4
3
2
1
Selesai!
```

Jika `angka -= 1` dihilangkan, kondisi selalu `True` dan program berjalan tanpa henti.

### 3. Pencacah dan Akumulator

```python
jumlah = 0
pencacah = 0

while pencacah < 5:
    pencacah += 1
    jumlah += pencacah

print(f"Jumlah: {jumlah}")
print(f"Banyak data: {pencacah}")
print(f"Rata-rata: {jumlah / pencacah}")
```

Output:

```text
Jumlah: 15
Banyak data: 5
Rata-rata: 3.0
```

- **Pencacah** (`pencacah`) menghitung banyaknya putaran.
- **Akumulator** (`jumlah`) menjumlahkan nilai.

### 4. Nilai Sentinel

Sentinel adalah nilai khusus yang menandakan perulangan harus berhenti.

```python
total = 0

angka = int(input("Masukkan angka (0 untuk selesai): "))

while angka != 0:
    total += angka
    angka = int(input("Masukkan angka (0 untuk selesai): "))

print(f"Total: {total}")
```

Contoh interaksi:

```text
Masukkan angka (0 untuk selesai): 10
Masukkan angka (0 untuk selesai): 20
Masukkan angka (0 untuk selesai): 5
Masukkan angka (0 untuk selesai): 0
Total: 35
```

Nilai `0` tidak ikut dijumlahkan karena loop berhenti sebelum blok dijalankan.

### 5. Validasi Input Berulang

`while` sering dipakai untuk meminta input sampai benar.

```python
nilai = int(input("Masukkan nilai 0-100: "))

while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    nilai = int(input("Masukkan nilai 0-100: "))

print(f"Nilai yang disimpan: {nilai}")
```

Contoh interaksi:

```text
Masukkan nilai 0-100: 120
Nilai tidak valid.
Masukkan nilai 0-100: -5
Nilai tidak valid.
Masukkan nilai 0-100: 80
Nilai yang disimpan: 80
```

### 6. `break` dan `continue`

- `break` menghentikan loop sepenuhnya.
- `continue` langsung melanjutkan ke pemeriksaan kondisi berikutnya.

```python
angka = 1

while angka <= 10:
    if angka == 5:
        break
    print(angka)
    angka += 1
```

Output:

```text
1
2
3
4
```

```python
angka = 0

while angka < 6:
    angka += 1
    if angka % 2 == 0:
        continue
    print(angka)
```

Output:

```text
1
3
5
```

### 7. `while ... else`

Blok `else` dijalankan jika loop selesai tanpa `break`.

```python
percobaan = 0

while percobaan < 3:
    percobaan += 1
    if percobaan == 2:
        print("Berhasil pada percobaan kedua.")
        break
else:
    print("Tidak ada percobaan yang berhasil.")
```

Output:

```text
Berhasil pada percobaan kedua.
```

Jika `break` tidak pernah dijalankan, blok `else` akan tampil.

### 8. Perulangan Bersarang

```python
baris = 1

while baris <= 3:
    kolom = 1
    while kolom <= 3:
        print(f"{baris * kolom:3}", end="")
        kolom += 1
    print()
    baris += 1
```

Output:

```text
  1  2  3
  2  4  6
  3  6  9
```

Pastikan setiap loop memiliki cara untuk berhenti.

### 9. `for` atau `while`?

| Gunakan `for` | Gunakan `while` |
|---|---|
| Jumlah putaran diketahui | Jumlah putaran belum diketahui |
| Menelusuri `range`, teks, atau data | Menunggu kondisi tertentu |
| Contoh: 10 kali, 1 sampai n | Contoh: sampai input benar, sampai saldo cukup |

### 10. Kesalahan Umum

| Kesalahan | Contoh | Akibat | Perbaikan |
|---|---|---|---|
| Lupa mengubah variabel | `while i < 5:` tanpa `i += 1` | Loop tak berujung | Tambahkan perubahan variabel |
| Kondisi tidak pernah salah | `while i > 0:` dengan `i += 1` | Loop tak berujung | Pastikan nilai menuju kondisi berhenti |
| `break` di luar `if` | `break` langsung di awal loop | Loop berhenti pada putaran pertama | Tempatkan `break` di dalam kondisi |
| Sentinel salah | `while angka == 0:` | Loop tidak berjalan atau berhenti terlalu cepat | Periksa operator perbandingan |
| Indentasi salah | Perintah keluar dari loop | Hanya dijalankan sekali | Periksa indentasi |
| Lupa input ulang | Input hanya di luar loop | Nilai tidak pernah berubah | Minta input di dalam loop |

### 11. Tips

- Tulis kondisi berhenti terlebih dahulu.
- Pastikan variabel pada kondisi berubah di dalam loop.
- Gunakan sentinel yang jelas, misalnya `0` atau `-1`.
- Untuk validasi, ulangi input di dalam loop.
- Uji dengan kasus batas: nilai terkecil, nilai terbesar, dan input salah.
- Jika jumlah putaran pasti, `for` biasanya lebih sederhana.

---

## Tugas Praktikum

Simpan setiap tugas sebagai file terpisah, misalnya `tugas6_1.py`.

### Tugas 6.1 — Hitung Mundur

Minta bilangan bulat positif `n`, lalu tampilkan hitung mundur dari `n` sampai 1.

Contoh interaksi:

```text
Masukkan n: 5
5
4
3
2
1
Selesai!
```

**Ketentuan:** gunakan `while`. Jika `n <= 0`, tampilkan `n harus bilangan positif.`

### Tugas 6.2 — Jumlahkan Angka sampai 0

Minta angka berulang kali. Perulangan berhenti ketika pengguna memasukkan `0`. Tampilkan total, banyak angka, dan rata-rata.

Contoh interaksi:

```text
Masukkan angka (0 untuk selesai): 10
Masukkan angka (0 untuk selesai): 20
Masukkan angka (0 untuk selesai): 30
Masukkan angka (0 untuk selesai): 0
Total: 60
Banyak angka: 3
Rata-rata: 20.00
```

**Ketentuan:**

- Angka `0` tidak ikut dihitung.
- Jika tidak ada angka yang dimasukkan, tampilkan `Tidak ada data.`
- Gunakan pencacah dan akumulator.

### Tugas 6.3 — Validasi Nilai

Minta nilai 0–100 berulang sampai pengguna memasukkan nilai yang valid. Tampilkan nilai dan jumlah percobaan.

Contoh interaksi:

```text
Percobaan 1: 120
Nilai tidak valid.
Percobaan 2: -5
Nilai tidak valid.
Percobaan 3: 80
Nilai 80 disimpan setelah 3 percobaan.
```

**Ketentuan:** gunakan `while` dengan kondisi `nilai < 0 or nilai > 100`.

### Tugas 6.4 — Tebak Angka

Buat permainan menebak angka rahasia `42` dengan maksimal 5 percobaan.

Contoh interaksi:

```text
Percobaan 1: 20
Terlalu kecil.
Percobaan 2: 60
Terlalu besar.
Percobaan 3: 42
Selamat, tebakan Anda benar!
```

Jika percobaan habis:

```text
Percobaan habis. Angka rahasianya 42.
```

**Ketentuan:**

- Gunakan `while` dan penghitung percobaan.
- Gunakan `break` saat tebakan benar.
- Beri petunjuk `Terlalu kecil.` atau `Terlalu besar.`
- Setelah loop, tampilkan pesan yang sesuai.

### Tugas 6.5 — Simpan Uang sampai Target

Minta target tabungan dan setoran. Minta setoran berulang sampai total tabungan mencapai atau melebihi target.

Contoh interaksi:

```text
Target tabungan: 100000
Setoran: 30000
Total sementara: Rp30,000
Setoran: 50000
Total sementara: Rp80,000
Setoran: 25000
Target tercapai. Total tabungan: Rp105,000
```

**Ketentuan:**

- Tolak setoran `0` atau negatif.
- Gunakan `while` dengan kondisi total belum mencapai target.
- Tampilkan total sementara setiap kali setoran diterima.

### Tugas 6.6 — Tantangan: Menu Kalkulator Berulang

Buat kalkulator dengan menu yang terus tampil sampai pengguna memilih keluar.

```text
=== KALKULATOR ===
1. Tambah
2. Kurang
3. Kali
4. Bagi
0. Keluar
Pilihan:
```

Contoh interaksi:

```text
Pilihan: 1
Bilangan pertama: 10
Bilangan kedua: 5
Hasil: 15.0

Pilihan: 4
Bilangan pertama: 10
Bilangan kedua: 0
Pembagian dengan nol tidak diperbolehkan.

Pilihan: 0
Terima kasih.
```

**Ketentuan:**

- Gunakan `while` untuk menu berulang.
- Gunakan `match-case` untuk memilih operasi.
- Tangani pembagian dengan nol.
- Tampilkan `Pilihan tidak valid.` untuk menu yang salah.
- Pilihan `0` menghentikan program.

---

## Rangkuman

- `while` mengulang selama kondisi `True`.
- Variabel pada kondisi harus berubah agar loop dapat berhenti.
- Sentinel adalah nilai khusus penanda berhenti.
- `while` cocok untuk validasi input dan jumlah putaran yang belum diketahui.
- `break` menghentikan loop; `continue` melewati satu putaran.
- `while-else` berjalan bila loop selesai tanpa `break`.
- Selalu pastikan ada jalur keluar dari loop.

## Istilah Penting

| Istilah | Arti |
|---|---|
| Kondisi | Ekspresi yang menentukan lanjut atau berhentinya loop |
| Sentinel | Nilai penanda berhenti |
| Pencacah | Variabel penghitung jumlah putaran |
| Akumulator | Variabel penjumlah nilai |
| Infinite loop | Perulangan yang tidak pernah berhenti |
| `while-else` | Blok `else` yang berjalan bila loop tidak dihentikan `break` |

## Checklist Sebelum Lanjut

- [ ] Saya dapat menulis `while` dengan kondisi yang benar.
- [ ] Saya dapat membuat pencacah dan akumulator.
- [ ] Saya dapat menggunakan sentinel.
- [ ] Saya dapat membuat validasi input berulang.
- [ ] Saya dapat menghindari loop tak berujung.
- [ ] Saya dapat memilih antara `for` dan `while`.
- [ ] Saya sudah mengerjakan seluruh tugas.

## Langkah Selanjutnya

Lanjutkan ke [Modul 7 — Struktur Data](modul-07-struktur-data.md).
