# Proyek 1 Tahap 1 — Kalkulator Menu Interaktif

## Tujuan

Membuat kalkulator berbasis menu untuk menerapkan materi Modul 1–6: variabel, tipe data, `if-else`, `match-case`, perulangan `for`, dan perulangan `while`.

## Deskripsi

Program menampilkan menu berulang. Pengguna memilih jenis perhitungan, memasukkan data, lalu melihat hasil. Program kembali ke menu sampai pengguna memilih keluar.

## Batasan Materi

Proyek ini **hanya menggunakan materi Modul 1–6**. Artinya:

- Tidak menggunakan `list`, `tuple`, `dict`, atau `set`.
- Tidak menggunakan fungsi buatan sendiri (`def`).
- Tidak menggunakan library eksternal.
- Semua logika ditulis langsung di alur program.

Batasan ini bertujuan memastikan mahasiswa menguasai percabangan dan perulangan sebelum mempelajari struktur data dan fungsi.

## Fitur Wajib

### 1. Menu Berulang

```text
=== KALKULATOR MENU ===
1. Operasi aritmatika
2. Luas bangun
3. Konversi suhu
4. Tabel perkalian
5. Faktorial
6. Deret angka
0. Keluar
Pilihan:
```

Menu terus tampil sampai pengguna memilih `0`.

### 2. Operasi Aritmatika

Minta dua bilangan dan operator `+`, `-`, `*`, atau `/`.

- Gunakan `match-case` untuk memilih operator.
- Tolak pembagian dengan nol.
- Tampilkan operator tidak valid bila perlu.

Contoh:

```text
Bilangan pertama: 10
Bilangan kedua: 4
Operator (+, -, *, /): /
Hasil: 2.50
```

### 3. Luas Bangun

Sediakan submenu:

```text
1. Persegi
2. Persegi panjang
3. Lingkaran
4. Segitiga
Pilihan bangun:
```

Rumus:

```text
Persegi         = sisi x sisi
Persegi panjang = panjang x lebar
Lingkaran       = 3.14159 x r x r
Segitiga        = 0.5 x alas x tinggi
```

Tampilkan hasil dua angka di belakang koma.

### 4. Konversi Suhu

Sediakan submenu:

```text
1. Celsius ke Fahrenheit
2. Fahrenheit ke Celsius
3. Celsius ke Kelvin
Pilihan konversi:
```

Rumus:

```text
C ke F = (C x 9/5) + 32
F ke C = (F - 32) x 5/9
C ke K = C + 273.15
```

Tampilkan hasil dua angka di belakang koma.

### 5. Tabel Perkalian

Minta satu bilangan `n`, lalu tampilkan `n x 1` sampai `n x 10` menggunakan `for`.

Contoh:

```text
Masukkan n: 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
...
3 x 10 = 30
```

### 6. Faktorial

Minta bilangan bulat `n` (minimal 0), lalu hitung `n!` menggunakan `for`.

Contoh:

```text
Masukkan n: 5
5! = 120
```

### 7. Deret Angka

Minta bilangan bulat positif `n`, lalu tampilkan angka 1 sampai `n`, jumlahnya, dan rata-ratanya menggunakan `for`.

Contoh:

```text
Masukkan n: 5
Deret: 1 2 3 4 5
Jumlah: 15
Rata-rata: 3.00
```

### 8. Validasi

- Pilihan menu di luar daftar harus ditolak.
- Pembagian dengan nol harus ditangani.
- Input `n` untuk faktorial dan deret harus sesuai ketentuan.
- Program tidak boleh berhenti karena pilihan menu yang salah.

## Contoh Interaksi

```text
=== KALKULATOR MENU ===
1. Operasi aritmatika
2. Luas bangun
3. Konversi suhu
4. Tabel perkalian
5. Faktorial
6. Deret angka
0. Keluar
Pilihan: 1
Bilangan pertama: 10
Bilangan kedua: 4
Operator (+, -, *, /): /
Hasil: 2.50

Pilihan: 4
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

Pilihan: 6
Masukkan n: 5
Deret: 1 2 3 4 5
Jumlah: 15
Rata-rata: 3.00

Pilihan: 9
Pilihan tidak valid.

Pilihan: 0
Terima kasih.
```

## Ketentuan Teknis

- Nama file utama: `kalkulator_menu.py`.
- Tidak menggunakan `def`, `list`, `dict`, `tuple`, atau `set`.
- Gunakan `while` untuk menu dan `for` pada fitur yang membutuhkan perulangan berhitungan.
- Gunakan `match-case` untuk menu utama dan submenu.
- Gunakan `if-else` untuk validasi dan perhitungan bersyarat.
- Program harus berjalan di Python 3.10+.
- Sertakan `README.md` berisi cara menjalankan dan daftar fitur.

## Langkah Pengerjaan

1. Buat menu utama dengan `while` dan `match-case`.
2. Implementasikan operasi aritmatika beserta validasi pembagian nol.
3. Tambahkan submenu luas bangun dan konversi suhu.
4. Tambahkan tabel perkalian, faktorial, dan deret menggunakan `for`.
5. Uji pilihan salah, nilai nol, nilai negatif, dan pembagian dengan nol.
6. Tulis README dan siapkan demo.

## Kriteria Selesai

- [ ] Menu berulang berjalan sampai pilihan `0`.
- [ ] Operasi aritmatika dan pembagian nol ditangani.
- [ ] Luas bangun dan konversi suhu menghasilkan nilai benar.
- [ ] Tabel perkalian, faktorial, dan deret menggunakan `for`.
- [ ] Pilihan menu salah tidak menghentikan program.
- [ ] Tidak menggunakan fungsi, list, atau dict.
- [ ] Program dapat dijalankan sesuai README.

## Penilaian

Gunakan [rubrik penilaian Tahap 1](../README.md#rubrik-penilaian-tahap-1-modul-16).
