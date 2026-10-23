# Kunci Jawaban Modul 3 — Percabangan `if-else`

## Tugas 3.1 — Ganjil atau Genap

```python
bilangan = int(input("Masukkan bilangan: "))

if bilangan % 2 == 0:
    print(f"{bilangan} adalah bilangan genap.")
else:
    print(f"{bilangan} adalah bilangan ganjil.")
```

Contoh output:

```text
Masukkan bilangan: 7
7 adalah bilangan ganjil.
```

**Penjelasan:** bilangan genap habis dibagi 2, sehingga sisa baginya (`% 2`) sama dengan 0.

## Tugas 3.2 — Nilai Huruf

```python
nilai = float(input("Masukkan nilai: "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
elif nilai >= 85:
    print("Nilai huruf: A")
elif nilai >= 75:
    print("Nilai huruf: B")
elif nilai >= 65:
    print("Nilai huruf: C")
elif nilai >= 55:
    print("Nilai huruf: D")
else:
    print("Nilai huruf: E")
```

Contoh output:

```text
Masukkan nilai: 82
Nilai huruf: B
```

**Penjelasan:** validasi rentang dilakukan lebih dulu. Setelah itu, kondisi diperiksa dari batas tertinggi ke terendah agar nilai seperti 85 tidak tertangkap oleh kondisi yang lebih rendah.

## Tugas 3.3 — Tahun Kabisat

```python
tahun = int(input("Masukkan tahun: "))

if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
    print(f"{tahun} adalah tahun kabisat.")
else:
    print(f"{tahun} bukan tahun kabisat.")
```

Contoh output:

```text
Masukkan tahun: 2024
2024 adalah tahun kabisat.
```

```text
Masukkan tahun: 1900
1900 bukan tahun kabisat.
```

**Penjelasan:** tahun 1900 habis dibagi 4, tetapi juga habis dibagi 100 dan tidak habis dibagi 400, sehingga bukan kabisat.

## Tugas 3.4 — Diskon Belanja

```python
total_belanja = float(input("Total belanja: "))

if total_belanja >= 500000:
    diskon = 0.20
elif total_belanja >= 250000:
    diskon = 0.10
elif total_belanja >= 100000:
    diskon = 0.05
else:
    diskon = 0

potongan = total_belanja * diskon
total_bayar = total_belanja - potongan

print(f"Diskon: Rp{potongan:,.0f}")
print(f"Total bayar: Rp{total_bayar:,.0f}")
```

Contoh output:

```text
Total belanja: 300000
Diskon: Rp30,000
Total bayar: Rp270,000
```

**Penjelasan:** kondisi diperiksa dari nominal terbesar. Jika `total_belanja >= 100000` diletakkan paling atas, belanja 300000 hanya akan mendapat diskon 5%.

## Tugas 3.5 — Login Sederhana

```python
username = input("Username: ")
password = input("Password: ")

if username == "admin" and password == "python123":
    print("Login berhasil")
else:
    print("Username atau password salah")
```

Contoh output:

```text
Username: admin
Password: python123
Login berhasil
```

**Penjelasan:** `and` memastikan kedua syarat terpenuhi. Jika salah satu salah, blok `else` dijalankan.

## Tugas 3.6 — Tarif Parkir

```python
jenis = input("Jenis kendaraan (motor/mobil/truk): ").lower()
durasi = int(input("Durasi (jam): "))

if durasi <= 0:
    print("Durasi harus lebih dari 0.")
elif jenis == "motor":
    tarif = 2000
elif jenis == "mobil":
    tarif = 5000
elif jenis == "truk":
    tarif = 10000
else:
    print("Jenis kendaraan tidak valid.")
    tarif = 0

if tarif > 0:
    tarif_dasar = tarif * durasi

    if durasi > 5:
        diskon = tarif_dasar * 0.10
    else:
        diskon = 0

    total = tarif_dasar - diskon

    print(f"Tarif dasar: Rp{tarif_dasar:,.0f}")
    print(f"Diskon 10%: Rp{diskon:,.0f}")
    print(f"Total bayar: Rp{total:,.0f}")
```

Contoh output:

```text
Jenis kendaraan (motor/mobil/truk): mobil
Durasi (jam): 6
Tarif dasar: Rp30,000
Diskon 10%: Rp3,000
Total bayar: Rp27,000
```

Contoh kendaraan tidak dikenal:

```text
Jenis kendaraan (motor/mobil/truk): sepeda
Durasi (jam): 2
Jenis kendaraan tidak valid.
```

**Penjelasan:**

- `lower()` membuat input `Mobil` diperlakukan sama seperti `mobil`.
- `tarif` diisi sesuai jenis kendaraan. Jika jenis tidak dikenal, program menampilkan pesan dan tidak menghitung.
- Diskon hanya diberikan jika durasi lebih dari 5 jam.
- Blok `if tarif > 0:` mencegah perhitungan ketika kendaraan tidak valid.
