# Proyek 2 Tahap 1 — Pemesanan Tiket Bioskop

## Tujuan

Membuat aplikasi pemesanan tiket bioskop untuk menerapkan materi Modul 1–6: input/output, tipe data, `if-else`, `match-case`, perulangan `for`, dan perulangan `while`.

## Deskripsi

Program menampilkan daftar film, menerima jumlah tiket, menghitung harga berdasarkan usia penonton, memberi diskon member, memproses pembayaran, dan mencetak ringkasan transaksi. Program dapat melayani beberapa transaksi sampai pengguna keluar.

## Batasan Materi

Proyek ini **hanya menggunakan materi Modul 1–6**. Artinya:

- Tidak menggunakan `list`, `tuple`, `dict`, atau `set`.
- Tidak menggunakan fungsi buatan sendiri (`def`).
- Tidak menggunakan library eksternal.
- Semua data transaksi dihitung secara langsung tanpa penyimpanan kumpulan data.

## Fitur Wajib

### 1. Menu Utama Berulang

```text
=== TIKET BIOSKOP ===
1. Pesan tiket
2. Lihat total pendapatan
0. Keluar
Pilihan:
```

Menu terus tampil sampai pengguna memilih `0`.

### 2. Daftar Film

Gunakan `match-case` untuk memilih film:

| Kode | Judul | Harga per tiket |
|---|---|---|
| A | Petualangan Angka | Rp35,000 |
| B | Logika Malam | Rp45,000 |
| C | Kode Rahasia | Rp55,000 |

Kode film tidak membedakan huruf besar dan kecil. Kode lain harus ditolak.

### 3. Jumlah Tiket

- Minta jumlah tiket.
- Jumlah harus 1–10.
- Gunakan `for` untuk meminta usia setiap penonton.

### 4. Harga Berdasarkan Usia

| Usia penonton | Kategori | Persentase harga |
|---|---|---|
| < 13 tahun | Anak | 70% |
| 13–59 tahun | Dewasa | 100% |
| ≥ 60 tahun | Senior | 80% |

Usia harus 0–120. Jika tidak valid, minta ulang usia tersebut.

### 5. Diskon Member

Setelah total harga tiket dihitung, tanyakan apakah pelanggan memiliki kartu member (`y/n`).

- Jika `y`, berikan diskon 10% dari total.
- Jika `n`, tidak ada diskon.
- Input selain `y` dan `n` harus ditolak dan ditanyakan ulang.

### 6. Pembayaran

- Tampilkan total yang harus dibayar.
- Minta nominal pembayaran.
- Tolak pembayaran yang kurang dari total.
- Hitung kembalian.

### 7. Ringkasan Transaksi

Tampilkan:

- judul film,
- jumlah tiket,
- rincian kategori setiap tiket,
- total sebelum diskon,
- diskon member,
- total bayar,
- pembayaran,
- kembalian.

### 8. Total Pendapatan

Setiap transaksi yang berhasil ditambahkan ke total pendapatan. Pilihan menu `2` menampilkan total pendapatan selama program berjalan.

## Contoh Interaksi

```text
=== TIKET BIOSKOP ===
1. Pesan tiket
2. Lihat total pendapatan
0. Keluar
Pilihan: 1

Daftar film:
A. Petualangan Angka - Rp35,000
B. Logika Malam - Rp45,000
C. Kode Rahasia - Rp55,000
Pilih film (A/B/C): A
Jumlah tiket (1-10): 2

Umur penonton 1: 10
Tiket 1: Anak - Rp24,500
Umur penonton 2: 65
Tiket 2: Senior - Rp28,000

Total sebelum diskon: Rp52,500
Member (y/n): y
Diskon member 10%: Rp5,250
Total bayar: Rp47,250

Bayar: Rp50000
Ringkasan:
Film: Petualangan Angka
Jumlah tiket: 2
Total sebelum diskon: Rp52,500
Diskon member: Rp5,250
Total bayar: Rp47,250
Bayar: Rp50,000
Kembalian: Rp2,750

Pilihan: 2
Total pendapatan: Rp47,250

Pilihan: 0
Terima kasih.
```

## Ketentuan Teknis

- Nama file utama: `tiket_bioskop.py`.
- Tidak menggunakan `def`, `list`, `dict`, `tuple`, atau `set`.
- Gunakan `while` untuk menu, pengulangan transaksi, dan validasi usia.
- Gunakan `for` untuk memproses setiap tiket.
- Gunakan `match-case` untuk menu utama dan pilihan film.
- Gunakan `if-else` untuk kategori usia, diskon, dan pembayaran.
- Program harus berjalan di Python 3.10+.
- Sertakan `README.md` berisi cara menjalankan dan daftar fitur.

## Langkah Pengerjaan

1. Buat menu utama dan daftar film.
2. Implementasikan pemilihan film dan validasi kode.
3. Buat perulangan `for` untuk meminta usia setiap penonton.
4. Hitung harga per kategori dan akumulasikan total.
5. Tambahkan diskon member, pembayaran, kembalian, dan ringkasan.
6. Akumulasikan total pendapatan dan tampilkan melalui menu.
7. Uji kode film salah, jumlah tiket di luar batas, usia tidak valid, dan pembayaran kurang.
8. Tulis README dan siapkan demo.

## Kriteria Selesai

- [ ] Menu berulang berjalan sampai pilihan `0`.
- [ ] Pemilihan film menggunakan `match-case` dan kode salah ditolak.
- [ ] Jumlah tiket divalidasi 1–10.
- [ ] Usia setiap penonton divalidasi dan kategorinya benar.
- [ ] Total, diskon member, pembayaran, dan kembalian benar.
- [ ] Ringkasan transaksi dan total pendapatan ditampilkan.
- [ ] Tidak menggunakan fungsi, list, atau dict.
- [ ] Program dapat dijalankan sesuai README.

## Penilaian

Gunakan [rubrik penilaian Tahap 1](../README.md#rubrik-penilaian-tahap-1-modul-16).
