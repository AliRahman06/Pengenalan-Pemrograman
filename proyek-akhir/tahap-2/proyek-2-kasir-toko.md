# Proyek 2 — Aplikasi Kasir Toko

## Tujuan

Membuat aplikasi terminal untuk melayani transaksi penjualan dengan menerapkan materi Modul 1–8: input/output, tipe data, percabangan `if-else` dan `match-case`, perulangan `for` dan `while`, list, dict, serta fungsi. Proyek ini adalah **Proyek Tahap 2**.

## Deskripsi

Program menyimpan daftar produk, menerima transaksi beberapa item, menghitung diskon dan pajak, memproses pembayaran, lalu mencetak struk. Stok produk berkurang setelah transaksi berhasil.

## Fitur Wajib

### 1. Menu Berulang

```text
=== KASIR TOKO ===
1. Lihat produk
2. Transaksi baru
0. Keluar
Pilihan:
```

### 2. Lihat Produk

Tampilkan seluruh produk dalam bentuk tabel: kode, nama, harga, dan stok.

```text
Kode   Nama             Harga        Stok
------------------------------------------
P001   Pena             Rp3,000      10
P002   Buku             Rp5,000      5
P003   Penggaris        Rp4,000      8
```

### 3. Transaksi Baru

- Minta kode produk dan jumlah. Ulangi sampai pengguna mengosongkan kode produk.
- Kode produk tidak membedakan huruf besar/kecil.
- Tolak kode yang tidak terdaftar.
- Tolak jumlah ≤ 0.
- Tolak jumlah yang melebihi stok. Perhitungkan juga jumlah yang sudah masuk keranjang.
- Setelah item selesai dimasukkan, tampilkan ringkasan belanja.

### 4. Perhitungan

```text
Subtotal = jumlah x harga untuk semua item
```

Aturan diskon berdasarkan subtotal:

| Subtotal | Diskon |
|---|---|
| ≥ Rp200,000 | 15% |
| ≥ Rp100,000 | 10% |
| ≥ Rp50,000 | 5% |
| < Rp50,000 | 0% |

```text
Pajak   = 11% x (subtotal - diskon)
Total   = subtotal - diskon + pajak
```

### 5. Pembayaran

- Minta jumlah uang yang dibayarkan.
- Tolak pembayaran yang kurang dari total.
- Hitung kembalian.
- Stok produk baru dikurangi setelah pembayaran berhasil.
- Jika transaksi dibatalkan, stok tidak boleh berubah.

### 6. Struk

Cetak struk berisi item, jumlah, harga, subtotal, diskon, pajak, total, pembayaran, dan kembalian.

```text
==============================
STRUK PEMBELIAN
==============================
Pena
  3 x Rp3,000 = Rp9,000
Buku
  2 x Rp5,000 = Rp10,000
------------------------------
Subtotal      : Rp19,000
Diskon 0%     : Rp0
Pajak 11%     : Rp2,090
Total         : Rp21,090
Bayar         : Rp25,000
Kembalian     : Rp3,910
==============================
Terima kasih.
```

## Data Produk Awal

Gunakan data berikut agar pengujian seragam.

```python
produk = [
    {"kode": "P001", "nama": "Pena", "harga": 3000, "stok": 10},
    {"kode": "P002", "nama": "Buku", "harga": 5000, "stok": 5},
    {"kode": "P003", "nama": "Penggaris", "harga": 4000, "stok": 8}
]
```

## Fungsi yang Disarankan

| Fungsi | Tugas |
|---|---|
| `tampilkan_menu()` | Menampilkan menu utama |
| `tampilkan_produk(produk)` | Menampilkan tabel produk |
| `cari_produk(produk, kode)` | Mengembalikan dict produk atau `None` |
| `transaksi(produk)` | Mengelola keranjang dan pembayaran |
| `hitung_subtotal(keranjang)` | Menghitung subtotal |
| `hitung_diskon(subtotal)` | Mengembalikan persentase diskon |
| `hitung_total(subtotal, diskon)` | Menghitung pajak dan total |
| `cetak_struk(...)` | Menampilkan struk |
| `main()` | Mengatur alur program |

## Contoh Interaksi

```text
=== KASIR TOKO ===
1. Lihat produk
2. Transaksi baru
0. Keluar
Pilihan: 2

Kode produk (kosong untuk selesai): P001
Jumlah: 3
Pena x3 ditambahkan.

Kode produk (kosong untuk selesai): p002
Jumlah: 2
Buku x2 ditambahkan.

Kode produk (kosong untuk selesai):
Subtotal: Rp19,000
Diskon 0%: Rp0
Pajak 11%: Rp2,090
Total: Rp21,090
Bayar: Rp25000
==============================
STRUK PEMBELIAN
==============================
Pena
  3 x Rp3,000 = Rp9,000
Buku
  2 x Rp5,000 = Rp10,000
------------------------------
Subtotal      : Rp19,000
Diskon 0%     : Rp0
Pajak 11%     : Rp2,090
Total         : Rp21,090
Bayar         : Rp25,000
Kembalian     : Rp3,910
==============================
Terima kasih.
```

## Fitur Bonus (Opsional)

- Riwayat transaksi selama program berjalan.
- Laporan total pendapatan dan produk terlaris.
- Fitur restock produk.
- Simpan dan muat data produk dari JSON.
- Simpan struk ke file teks.

## Ketentuan Teknis

- Nama file utama: `kasir_toko.py`.
- Minimal 5 fungsi selain `main()`.
- Tidak menggunakan library eksternal.
- Program harus berjalan di Python 3.10+.
- Sertakan `README.md` berisi cara menjalankan dan daftar fitur.
- Gunakan `try-except` bila perlu agar input bukan angka tidak menghentikan program.

## Langkah Pengerjaan yang Disarankan

1. Siapkan data produk dan fungsi `cari_produk()`.
2. Buat `tampilkan_produk()` dan uji tampilan tabel.
3. Buat fungsi perhitungan diskon dan total, lalu uji batas Rp50,000, Rp100,000, dan Rp200,000.
4. Buat proses keranjang dengan validasi stok.
5. Tambahkan pembayaran, pengurangan stok, dan struk.
6. Uji skenario: kode salah, jumlah nol, stok kurang, uang kurang, dan keranjang kosong.
7. Tulis README dan siapkan demo.

## Kriteria Selesai

- [ ] Menu dan transaksi berjalan berulang.
- [ ] Pencarian produk tidak membedakan huruf besar/kecil.
- [ ] Stok tervalidasi, termasuk item yang sudah ada di keranjang.
- [ ] Diskon, pajak, dan total dihitung dengan benar.
- [ ] Pembayaran kurang ditolak.
- [ ] Stok berkurang hanya setelah pembayaran berhasil.
- [ ] Struk menampilkan seluruh informasi wajib.
- [ ] Program menggunakan minimal 5 fungsi.
- [ ] Program dapat dijalankan sesuai petunjuk README.

## Penilaian

Gunakan [rubrik penilaian Tahap 2](../README.md#rubrik-penilaian-tahap-2-modul-18).
