# Kunci Jawaban Modul 8 — Fungsi dan Modul

## Tugas 8.1 — Fungsi Geometri

```python
def luas_persegi_panjang(panjang, lebar):
    return panjang * lebar


def luas_lingkaran(r):
    return 3.14159 * r * r


def volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi


panjang = float(input("Panjang: "))
lebar = float(input("Lebar: "))
tinggi = float(input("Tinggi: "))
jari_jari = float(input("Jari-jari: "))

print(f"Luas persegi panjang: {luas_persegi_panjang(panjang, lebar)}")
print(f"Luas lingkaran: {luas_lingkaran(jari_jari):.2f}")
print(f"Volume balok: {volume_balok(panjang, lebar, tinggi)}")
```

Contoh output:

```text
Panjang: 8
Lebar: 5
Tinggi: 3
Jari-jari: 7
Luas persegi panjang: 40.0
Luas lingkaran: 153.94
Volume balok: 120.0
```

**Penjelasan:** hasil perkalian bilangan `float` menampilkan `.0`. Jika ingin selalu dua desimal, gunakan format `:.2f`.

## Tugas 8.2 — Validasi dan Konversi Nilai

```python
def validasi_nilai(nilai):
    return 0 <= nilai <= 100


def konversi_huruf(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 55:
        return "D"
    else:
        return "E"


nilai = float(input("Masukkan nilai: "))

if validasi_nilai(nilai):
    print(f"Nilai huruf: {konversi_huruf(nilai)}")
else:
    print("Nilai tidak valid")
```

Contoh output:

```text
Masukkan nilai: 82
Nilai huruf: B
```

**Penjelasan:** `0 <= nilai <= 100` adalah penulisan ringkas untuk `nilai >= 0 and nilai <= 100`.

## Tugas 8.3 — Kalkulator Modular

```python
def tambah(a, b):
    return a + b


def kurang(a, b):
    return a - b


def kali(a, b):
    return a * b


def bagi(a, b):
    if b == 0:
        return None
    return a / b


angka1 = float(input("Bilangan pertama: "))
angka2 = float(input("Bilangan kedua: "))
operasi = input("Operasi (tambah/kurang/kali/bagi): ").lower()

if operasi == "tambah":
    hasil = tambah(angka1, angka2)
    print(f"Hasil: {hasil}")
elif operasi == "kurang":
    hasil = kurang(angka1, angka2)
    print(f"Hasil: {hasil}")
elif operasi == "kali":
    hasil = kali(angka1, angka2)
    print(f"Hasil: {hasil}")
elif operasi == "bagi":
    hasil = bagi(angka1, angka2)
    if hasil is None:
        print("Hasil: Pembagian dengan nol tidak diperbolehkan.")
    else:
        print(f"Hasil: {hasil}")
else:
    print("Operasi tidak valid.")
```

Contoh output:

```text
Bilangan pertama: 10
Bilangan kedua: 4
Operasi (tambah/kurang/kali/bagi): bagi
Hasil: 2.5
```

**Penjelasan:** `bagi()` mengembalikan `None` sebagai penanda kegagalan. Program utama memeriksa nilai tersebut sebelum menampilkan hasil.

## Tugas 8.4 — Modul `math` dan `random`

```python
import math
import random

angka = float(input("Masukkan bilangan: "))

print(f"Akar kuadrat: {math.sqrt(angka):.2f}")
print(f"Pembulatan ke atas: {math.ceil(angka)}")
print(f"Pembulatan ke bawah: {math.floor(angka)}")

hasil_lemparan = []
frekuensi = {}

for _ in range(20):
    dadu = random.randint(1, 6)
    hasil_lemparan.append(dadu)
    frekuensi[dadu] = frekuensi.get(dadu, 0) + 1

print("Hasil lemparan:", hasil_lemparan)
print("Frekuensi:", frekuensi)
```

Contoh output:

```text
Masukkan bilangan: 20
Akar kuadrat: 4.47
Pembulatan ke atas: 5
Pembulatan ke bawah: 4
Hasil lemparan: [3, 6, 1, 4, 2, 6, 5, 3, 1, 2, 4, 6, 3, 5, 2, 1, 4, 6, 3, 5]
Frekuensi: {3: 4, 6: 4, 1: 3, 4: 3, 2: 3, 5: 3}
```

**Catatan:** hasil `random` berbeda setiap kali program dijalankan. Jumlah seluruh frekuensi harus 20. Jika akar kuadrat dari bilangan negatif dihitung, `math.sqrt()` menimbulkan `ValueError`.

## Tugas 8.5 — Modul Buatan Sendiri

### `konversi.py`

```python
def celsius_ke_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def km_ke_meter(km):
    return km * 1000


def kg_ke_gram(kg):
    return kg * 1000
```

### `main.py`

```python
import konversi

celsius = float(input("Suhu Celsius: "))
jarak_km = float(input("Jarak (km): "))
berat_kg = float(input("Berat (kg): "))

fahrenheit = konversi.celsius_ke_fahrenheit(celsius)
meter = konversi.km_ke_meter(jarak_km)
gram = konversi.kg_ke_gram(berat_kg)

print(f"Fahrenheit: {fahrenheit}")
print(f"Meter: {meter}")
print(f"Gram: {gram}")
```

Contoh output:

```text
Suhu Celsius: 30
Jarak (km): 2.5
Berat (kg): 1.2
Fahrenheit: 86.0
Meter: 2500.0
Gram: 1200.0
```

**Penjelasan:** kedua file harus berada di folder yang sama. Nama modul saat diimpor adalah `konversi`, tanpa `.py`.

## Tugas 8.6 — Refactor Program

```python
def hitung_nilai_akhir(tugas, uts, uas):
    return 0.3 * tugas + 0.3 * uts + 0.4 * uas


def konversi_huruf(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 55:
        return "D"
    else:
        return "E"


def buat_data_mahasiswa(nama, tugas, uts, uas):
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    return {
        "nama": nama,
        "akhir": nilai_akhir,
        "huruf": konversi_huruf(nilai_akhir)
    }


def tampilkan_data(mahasiswa):
    for data in mahasiswa:
        print(f"{data['nama']}: {data['akhir']:.2f} ({data['huruf']})")


def main():
    mahasiswa = []

    for i in range(3):
        nama = input("Nama: ")
        tugas = float(input("Nilai tugas: "))
        uts = float(input("Nilai UTS: "))
        uas = float(input("Nilai UAS: "))
        mahasiswa.append(buat_data_mahasiswa(nama, tugas, uts, uas))

    tampilkan_data(mahasiswa)


if __name__ == "__main__":
    main()
```

Contoh output:

```text
Nama: Ayu
Nilai tugas: 90
Nilai UTS: 85
Nilai UAS: 88
Nama: Budi
Nilai tugas: 70
Nilai UTS: 75
Nilai UAS: 80
Nama: Citra
Nilai tugas: 60
Nilai UTS: 55
Nilai UAS: 65
Ayu: 87.70 (A)
Budi: 75.50 (B)
Citra: 60.50 (D)
```

**Penjelasan:**

- `hitung_nilai_akhir()` hanya bertanggung jawab menghitung nilai akhir.
- `konversi_huruf()` hanya mengubah nilai menjadi huruf.
- `buat_data_mahasiswa()` menggabungkan keduanya menjadi satu dict.
- `tampilkan_data()` menangani output.
- `main()` mengatur alur program.
- Blok `if __name__ == "__main__"` memastikan `main()` hanya berjalan saat file dieksekusi langsung.
