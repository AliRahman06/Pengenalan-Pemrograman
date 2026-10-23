# Proyek 1 — Aplikasi Manajemen Nilai Mahasiswa

## Tujuan

Membuat aplikasi terminal untuk mengelola nilai mahasiswa dengan menerapkan materi Modul 1–8: input/output, tipe data, percabangan `if-else` dan `match-case`, perulangan `for` dan `while`, list, dict, serta fungsi. Proyek ini adalah **Proyek Tahap 2**.

## Deskripsi

Program menyimpan data beberapa mahasiswa di memori. Setiap mahasiswa memiliki NIM, nama, nilai tugas, nilai UTS, dan nilai UAS. Program menghitung nilai akhir dan nilai huruf, lalu menyediakan menu untuk mengelola data.

## Fitur Wajib

### 1. Menu Berulang

Program menampilkan menu sampai pengguna memilih keluar.

```text
=== MANAJEMEN NILAI MAHASISWA ===
1. Tambah mahasiswa
2. Tampilkan semua mahasiswa
3. Cari mahasiswa
4. Ubah data mahasiswa
5. Hapus mahasiswa
6. Statistik
0. Keluar
Pilihan:
```

### 2. Tambah Mahasiswa

Minta NIM, nama, nilai tugas, UTS, dan UAS.

- NIM harus unik. Jika sudah ada, tampilkan pesan dan batalkan penambahan.
- Nama tidak boleh kosong.
- Nilai harus berada pada rentang 0–100.
- Simpan data dalam `list` berisi `dict`.

### 3. Tampilkan Semua Mahasiswa

Tampilkan data dalam bentuk tabel, termasuk nilai akhir dan huruf.

```text
NIM        Nama            Tugas   UTS    UAS   Akhir  Huruf
-------------------------------------------------------------
2401001    Ayu             90.00   85.00  88.00  87.70  A
2401002    Budi            70.00   75.00  80.00  75.50  B
```

Jika belum ada data, tampilkan `Belum ada data mahasiswa.`

### 4. Cari Mahasiswa

Cari berdasarkan NIM. Tampilkan seluruh data mahasiswa tersebut atau `Mahasiswa tidak ditemukan.`

### 5. Ubah Data Mahasiswa

Cari berdasarkan NIM, lalu izinkan pengguna mengubah nama dan ketiga nilai. NIM tidak diubah agar data tetap unik.

### 6. Hapus Mahasiswa

Cari berdasarkan NIM, minta konfirmasi `y/n`, lalu hapus data bila pengguna memilih `y`.

### 7. Statistik

Tampilkan:

- jumlah mahasiswa,
- rata-rata nilai akhir,
- nilai akhir tertinggi beserta nama,
- nilai akhir terendah beserta nama,
- jumlah mahasiswa yang lulus (nilai akhir ≥ 60).

### 8. Validasi

- Pilihan menu di luar daftar harus ditolak dengan pesan yang jelas.
- Input nilai bukan angka harus ditangani agar program tidak berhenti.
- Nilai di luar 0–100 harus ditolak.
- NIM yang sudah terdaftar tidak boleh ditambahkan dua kali.

## Aturan Perhitungan

```text
Nilai akhir = (30% x tugas) + (30% x UTS) + (40% x UAS)
```

| Nilai akhir | Huruf |
|---|---|
| ≥ 85 | A |
| ≥ 75 | B |
| ≥ 65 | C |
| ≥ 55 | D |
| < 55 | E |

## Struktur Data yang Disarankan

```python
mahasiswa = [
    {
        "nim": "2401001",
        "nama": "Ayu",
        "tugas": 90.0,
        "uts": 85.0,
        "uas": 88.0
    }
]
```

Nilai akhir dan huruf sebaiknya **dihitung melalui fungsi**, tidak disimpan permanen, agar selalu konsisten ketika data diubah.

## Fungsi yang Disarankan

| Fungsi | Tugas |
|---|---|
| `hitung_nilai_akhir(tugas, uts, uas)` | Mengembalikan nilai akhir |
| `konversi_huruf(nilai)` | Mengembalikan huruf A–E |
| `tampilkan_menu()` | Menampilkan menu |
| `tampilkan_semua(data)` | Menampilkan tabel |
| `cari_indeks(data, nim)` | Mengembalikan indeks atau `-1` |
| `tambah_mahasiswa(data)` | Menambah data |
| `ubah_mahasiswa(data)` | Mengubah data |
| `hapus_mahasiswa(data)` | Menghapus data |
| `tampilkan_statistik(data)` | Menampilkan ringkasan |
| `main()` | Mengatur alur program |

## Contoh Interaksi

```text
=== MANAJEMEN NILAI MAHASISWA ===
1. Tambah mahasiswa
2. Tampilkan semua mahasiswa
3. Cari mahasiswa
4. Ubah data mahasiswa
5. Hapus mahasiswa
6. Statistik
0. Keluar
Pilihan: 1
NIM: 2401001
Nama: Ayu
Nilai tugas: 90
Nilai UTS: 85
Nilai UAS: 88
Data Ayu berhasil ditambahkan.

Pilihan: 1
NIM: 2401002
Nama: Budi
Nilai tugas: 70
Nilai UTS: 75
Nilai UAS: 80
Data Budi berhasil ditambahkan.

Pilihan: 2
NIM        Nama            Tugas   UTS    UAS   Akhir  Huruf
-------------------------------------------------------------
2401001    Ayu             90.00   85.00  88.00  87.70  A
2401002    Budi            70.00   75.00  80.00  75.50  B

Pilihan: 6
Jumlah mahasiswa: 2
Rata-rata nilai akhir: 81.60
Nilai tertinggi: Ayu (87.70)
Nilai terendah: Budi (75.50)
Jumlah lulus: 2

Pilihan: 0
Terima kasih.
```

## Fitur Bonus (Opsional)

- Simpan dan muat data dari file JSON.
- Urutkan tabel berdasarkan NIM atau nilai akhir.
- Ekspor data ke CSV.
- Tampilkan daftar mahasiswa per huruf mutu.
- Batasi input NIM hanya angka.

## Ketentuan Teknis

- Nama file utama: `manajemen_nilai.py`.
- Minimal 5 fungsi selain `main()`.
- Tidak menggunakan library eksternal.
- Program harus berjalan di Python 3.10+.
- Sertakan `README.md` berisi cara menjalankan dan daftar fitur.
- Kode harus dapat dibaca: nama variabel jelas, fungsi fokus pada satu tugas.

## Langkah Pengerjaan yang Disarankan

1. Buat struktur data awal dan fungsi `hitung_nilai_akhir()` serta `konversi_huruf()`.
2. Uji kedua fungsi dengan beberapa nilai, termasuk batas 85, 75, 65, dan 55.
3. Buat menu dan `main()` dengan loop.
4. Implementasikan tambah dan tampilkan data.
5. Tambahkan cari, ubah, hapus, dan statistik.
6. Uji skenario: data kosong, NIM duplikat, nilai negatif, nilai di atas 100, dan input bukan angka.
7. Tulis README dan siapkan demo.

## Kriteria Selesai

- [ ] Semua fitur wajib berjalan.
- [ ] NIM unik dan pencarian berdasarkan NIM berfungsi.
- [ ] Nilai akhir dan huruf dihitung dengan benar.
- [ ] Statistik menampilkan data yang sesuai.
- [ ] Input salah tidak membuat program berhenti.
- [ ] Program menggunakan minimal 5 fungsi.
- [ ] Program dapat dijalankan sesuai petunjuk README.

## Penilaian

Gunakan [rubrik penilaian Tahap 2](../README.md#rubrik-penilaian-tahap-2-modul-18).
