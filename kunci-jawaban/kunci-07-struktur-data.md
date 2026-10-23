# Kunci Jawaban Modul 7 — Struktur Data

## Tugas 7.1 — Statistik Nilai

```python
nilai = []

for i in range(5):
    angka = float(input(f"Nilai ke-{i + 1}: "))
    nilai.append(angka)

total = sum(nilai)
rata_rata = total / len(nilai)
di_atas_rata = 0

for angka in nilai:
    if angka > rata_rata:
        di_atas_rata += 1

print("Daftar nilai:", nilai)
print("Total:", total)
print(f"Rata-rata: {rata_rata:.2f}")
print("Tertinggi:", max(nilai))
print("Terendah:", min(nilai))
print("Di atas rata-rata:", di_atas_rata)
```

Contoh output:

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

## Tugas 7.2 — Buku Kontak

```python
kontak = {
    "Ayu": "081234567890",
    "Budi": "082345678901",
    "Citra": "083456789012"
}

print("Daftar kontak:")
for nama, nomor in kontak.items():
    print(f"{nama}: {nomor}")

cari = input("Cari nama: ")
nomor = kontak.get(cari)

if nomor is None:
    print("Kontak tidak ditemukan")
else:
    print(f"Nomor {cari}: {nomor}")

nama_baru = input("Nama baru: ")
nomor_baru = input("Nomor baru: ")
kontak[nama_baru] = nomor_baru

print(f"Kontak {nama_baru} ditambahkan.")
print("Daftar kontak terbaru:")
for nama, nomor in kontak.items():
    print(f"{nama}: {nomor}")
```

Contoh output:

```text
Daftar kontak:
Ayu: 081234567890
Budi: 082345678901
Citra: 083456789012
Cari nama: Budi
Nomor Budi: 082345678901
Nama baru: Dina
Nomor baru: 084567890123
Kontak Dina ditambahkan.
Daftar kontak terbaru:
Ayu: 081234567890
Budi: 082345678901
Citra: 083456789012
Dina: 084567890123
```

**Penjelasan:** `get()` mengembalikan `None` jika kunci tidak ada, sehingga program tidak berhenti dengan `KeyError`.

## Tugas 7.3 — Frekuensi Kata

```python
kalimat = input("Masukkan kalimat: ")
frekuensi = {}

for kata in kalimat.split():
    kata = kata.casefold()
    frekuensi[kata] = frekuensi.get(kata, 0) + 1

for kata, jumlah in frekuensi.items():
    print(f"{kata}: {jumlah}")
```

Contoh output:

```text
Masukkan kalimat: saya suka python dan saya suka belajar
saya: 2
suka: 2
python: 1
dan: 1
belajar: 1
```

**Penjelasan:** `frekuensi.get(kata, 0)` mengambil jumlah sebelumnya. Jika kata belum ada, nilainya 0, lalu ditambah 1.

## Tugas 7.4 — Operasi Himpunan

```python
kelas_a = {"Ayu", "Budi", "Citra", "Dina"}
kelas_b = {"Citra", "Dina", "Eka", "Fajar"}

print("Semua peserta:", kelas_a | kelas_b)
print("Peserta kedua kegiatan:", kelas_a & kelas_b)
print("Hanya kelas A:", kelas_a - kelas_b)
print("Hanya di salah satu:", kelas_a ^ kelas_b)
```

Contoh output (urutan dapat berbeda):

```text
Semua peserta: {'Fajar', 'Budi', 'Ayu', 'Eka', 'Dina', 'Citra'}
Peserta kedua kegiatan: {'Dina', 'Citra'}
Hanya kelas A: {'Budi', 'Ayu'}
Hanya di salah satu: {'Fajar', 'Budi', 'Ayu', 'Eka'}
```

**Penjelasan:** `|` adalah union, `&` intersection, `-` difference, dan `^` symmetric difference. Urutan elemen `set` tidak dijamin.

## Tugas 7.5 — Penjumlahan Matriks

```python
matriks_a = [
    [1, 2],
    [3, 4]
]

matriks_b = [
    [5, 6],
    [7, 8]
]

print("Hasil penjumlahan:")
for i in range(2):
    baris = []
    for j in range(2):
        baris.append(matriks_a[i][j] + matriks_b[i][j])
    print(*baris)
```

Contoh output:

```text
Hasil penjumlahan:
6 8
10 12
```

**Penjelasan:** `matriks_a[i][j]` mengambil elemen pada baris `i` dan kolom `j`. `print(*baris)` mencetak setiap elemen dengan spasi.

## Tugas 7.6 — Inventaris Barang

```python
barang = [
    {"nama": "Pena", "harga": 3000, "stok": 10},
    {"nama": "Buku", "harga": 5000, "stok": 5},
    {"nama": "Penggaris", "harga": 4000, "stok": 8}
]

while True:
    print("\n=== INVENTARIS ===")
    print("1. Lihat barang")
    print("2. Tambah barang")
    print("3. Cari barang")
    print("4. Ubah stok")
    print("5. Hapus barang")
    print("6. Total nilai inventaris")
    print("0. Keluar")

    pilihan = input("Pilihan: ")

    if pilihan == "1":
        if not barang:
            print("Inventaris kosong.")
        else:
            for item in barang:
                print(
                    f"Nama: {item['nama']} | "
                    f"Harga: Rp{item['harga']:,.0f} | "
                    f"Stok: {item['stok']}"
                )

    elif pilihan == "2":
        nama = input("Nama barang: ")
        harga = float(input("Harga: "))
        stok = int(input("Stok: "))
        barang.append({"nama": nama, "harga": harga, "stok": stok})
        print(f"{nama} ditambahkan.")

    elif pilihan == "3":
        nama = input("Cari nama: ").casefold()
        ditemukan = False

        for item in barang:
            if item["nama"].casefold() == nama:
                print(
                    f"Nama: {item['nama']} | "
                    f"Harga: Rp{item['harga']:,.0f} | "
                    f"Stok: {item['stok']}"
                )
                ditemukan = True
                break

        if not ditemukan:
            print("Barang tidak ditemukan.")

    elif pilihan == "4":
        nama = input("Nama barang: ").casefold()
        ditemukan = False

        for item in barang:
            if item["nama"].casefold() == nama:
                stok_baru = int(input("Stok baru: "))
                item["stok"] = stok_baru
                print("Stok berhasil diperbarui.")
                ditemukan = True
                break

        if not ditemukan:
            print("Barang tidak ditemukan.")

    elif pilihan == "5":
        nama = input("Nama barang: ").casefold()

        ditemukan = False

        for i in range(len(barang)):
            if barang[i]["nama"].casefold() == nama:
                del barang[i]
                print("Barang berhasil dihapus.")
                ditemukan = True
                break

        if not ditemukan:
            print("Barang tidak ditemukan.")

    elif pilihan == "6":
        total = 0

        for item in barang:
            total += item["harga"] * item["stok"]

        print(f"Total nilai inventaris: Rp{total:,.0f}")

    elif pilihan == "0":
        print("Terima kasih.")
        break

    else:
        print("Pilihan tidak valid.")
```

Contoh output:

```text
=== INVENTARIS ===
1. Lihat barang
2. Tambah barang
3. Cari barang
4. Ubah stok
5. Hapus barang
6. Total nilai inventaris
0. Keluar
Pilihan: 1
Nama: Pena | Harga: Rp3,000 | Stok: 10
Nama: Buku | Harga: Rp5,000 | Stok: 5
Nama: Penggaris | Harga: Rp4,000 | Stok: 8

Pilihan: 6
Total nilai inventaris: Rp87,000

Pilihan: 0
Terima kasih.
```

**Penjelasan:**

- `barang` adalah list berisi dict, sehingga setiap barang memiliki nama, harga, dan stok.
- `range(len(barang))` menghasilkan indeks yang valid untuk penghapusan.
- Variabel `ditemukan` menandai apakah barang berhasil dihapus.
- `casefold()` membuat pencarian tidak membedakan huruf besar dan kecil.
