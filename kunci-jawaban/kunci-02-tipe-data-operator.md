# Kunci Jawaban Modul 2 — Variabel, Tipe Data, Operator, dan Ekspresi

## Tugas 2.1 — Biodata Interaktif

```python
nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
kota = input("Masukkan kota: ")

print(f"Halo {nama}, umur Anda {umur} tahun dan Anda tinggal di {kota}.")
print(f"Tahun depan umur Anda {umur + 1} tahun.")
```

Contoh output:

```text
Masukkan nama: Rina
Masukkan umur: 18
Masukkan kota: Bandung
Halo Rina, umur Anda 18 tahun dan Anda tinggal di Bandung.
Tahun depan umur Anda 19 tahun.
```

**Penjelasan:** `umur` harus diubah dengan `int()` agar dapat ditambah 1. Tanpa konversi, `umur + 1` menghasilkan `TypeError`.

## Tugas 2.2 — Rata-rata Nilai

```python
nilai1 = float(input("Nilai 1: "))
nilai2 = float(input("Nilai 2: "))
nilai3 = float(input("Nilai 3: "))

rata_rata = (nilai1 + nilai2 + nilai3) / 3

print(f"Rata-rata: {rata_rata:.2f}")
print(f"Tipe data hasil: {type(rata_rata)}")
```

Contoh output:

```text
Nilai 1: 80
Nilai 2: 90
Nilai 3: 75
Rata-rata: 81.67
Tipe data hasil: <class 'float'>
```

## Tugas 2.3 — Prediksi Ekspresi

| No | Ekspresi | Hasil | Tipe |
|---|---|---|---|
| 1 | `7 + 3 * 2` | `13` | `int` |
| 2 | `(7 + 3) * 2` | `20` | `int` |
| 3 | `10 / 4` | `2.5` | `float` |
| 4 | `10 // 4` | `2` | `int` |
| 5 | `10 % 4` | `2` | `int` |
| 6 | `2 ** 5` | `32` | `int` |
| 7 | `"2" + "3"` | `"23"` | `str` |
| 8 | `"2" * 3` | `"222"` | `str` |
| 9 | `5 > 3 and 2 < 1` | `False` | `bool` |
| 10 | `not (4 == 4)` | `False` | `bool` |

Kode pembuktian:

```python
print(7 + 3 * 2, type(7 + 3 * 2))
print((7 + 3) * 2, type((7 + 3) * 2))
print(10 / 4, type(10 / 4))
print(10 // 4, type(10 // 4))
print(10 % 4, type(10 % 4))
print(2 ** 5, type(2 ** 5))
print("2" + "3", type("2" + "3"))
print("2" * 3, type("2" * 3))
print(5 > 3 and 2 < 1, type(5 > 3 and 2 < 1))
print(not (4 == 4), type(not (4 == 4)))
```

Output:

```text
13 <class 'int'>
20 <class 'int'>
2.5 <class 'float'>
2 <class 'int'>
2 <class 'int'>
32 <class 'int'>
23 <class 'str'>
222 <class 'str'>
False <class 'bool'>
False <class 'bool'>
```

## Tugas 2.4 — Indeks Massa Tubuh (BMI)

```python
berat = float(input("Berat badan (kg): "))
tinggi_cm = float(input("Tinggi badan (cm): "))

tinggi_m = tinggi_cm / 100
bmi = berat / (tinggi_m ** 2)

print(f"BMI: {bmi:.2f}")
```

Contoh output:

```text
Berat badan (kg): 60
Tinggi badan (cm): 165
BMI: 22.04
```

**Penjelasan:** tinggi harus diubah ke meter sebelum dihitung. Tanda kurung pada `(tinggi_m ** 2)` memastikan pangkat dihitung lebih dulu.

## Tugas 2.5 — Struk Belanja

```python
nama_barang = input("Nama barang: ")
harga = float(input("Harga satuan: "))
jumlah = int(input("Jumlah: "))

subtotal = harga * jumlah
pajak = subtotal * 0.11
total = subtotal + pajak

print(f"Subtotal: Rp{subtotal:,.0f}")
print(f"Pajak 11%: Rp{pajak:,.0f}")
print(f"Total: Rp{total:,.0f}")
```

Contoh output:

```text
Nama barang: Buku
Harga satuan: 45000
Jumlah: 3
Subtotal: Rp135,000
Pajak 11%: Rp14,850
Total: Rp149,850
```

## Tugas 2.6 — Kartu Profil

```python
nama = input("Masukkan nama: ")
tahun_lahir = int(input("Masukkan tahun lahir: "))
tinggi = int(input("Masukkan tinggi badan (cm): "))

umur = 2026 - tahun_lahir

print("=" * 20)
print("KARTU PROFIL")
print("=" * 20)
print(f"{'Nama':<12}: {nama}")
print(f"{'Umur':<12}: {umur} tahun")
print(f"{'Tinggi':<12}: {tinggi} cm")
print("=" * 20)
```

Contoh output:

```text
Masukkan nama: Fajar
Masukkan tahun lahir: 2007
Masukkan tinggi badan (cm): 170
====================
KARTU PROFIL
====================
Nama        : Fajar
Umur        : 19 tahun
Tinggi      : 170 cm
====================
```

**Penjelasan:** `{'Nama':<12}` membuat teks rata kiri dengan lebar 12 karakter agar titik dua sejajar.
