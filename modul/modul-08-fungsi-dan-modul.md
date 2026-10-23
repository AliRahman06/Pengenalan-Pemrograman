# Modul 8 — Fungsi dan Modul

## Tujuan Praktikum

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. Membuat fungsi dengan `def` dan memanggilnya.
2. Membedakan parameter dan argumen.
3. Menggunakan `return` untuk mengembalikan nilai.
4. Menggunakan parameter default dan argumen kata kunci.
5. Menjelaskan ruang lingkup variabel lokal dan global.
6. Mengimpor modul standar serta membuat modul sendiri.

**Prasyarat:** Modul 1–7.  
**Estimasi waktu:** 3 jam.

---

## Dasar Teori

### 1. Mengapa Menggunakan Fungsi?

Fungsi adalah blok kode bernama yang dapat dipakai berulang kali. Bayangkan fungsi seperti **tombol** pada mesin: kita menekan tombol, mesin melakukan tugas tertentu, lalu memberi hasil.

Manfaat fungsi:

- Menghindari penulisan kode yang sama berulang.
- Membuat program lebih mudah dibaca.
- Memudahkan pengujian dan perbaikan.
- Memecah masalah besar menjadi bagian kecil.

### 2. Membuat dan Memanggil Fungsi

```python
def sapa():
    print("Halo, selamat datang!")

sapa()
sapa()
```

Output:

```text
Halo, selamat datang!
Halo, selamat datang!
```

Aturan:

- Gunakan `def` diikuti nama fungsi dan tanda kurung.
- Nama fungsi ditulis dengan `snake_case`.
- Akhiri baris `def` dengan titik dua `:`.
- Isi fungsi harus menjorok ke dalam.
- Fungsi harus **didefinisikan sebelum dipanggil** saat script dijalankan.

### 3. Parameter dan Argumen

**Parameter** adalah variabel pada definisi fungsi. **Argumen** adalah nilai yang dikirim saat memanggil fungsi.

```python
def sapa(nama):
    print(f"Halo, {nama}!")

sapa("Ayu")
sapa("Budi")
```

Output:

```text
Halo, Ayu!
Halo, Budi!
```

Fungsi dapat memiliki beberapa parameter:

```python
def tampilkan_nilai(nama, nilai):
    print(f"{nama} mendapat nilai {nilai}")

tampilkan_nilai("Citra", 88)
```

Output:

```text
Citra mendapat nilai 88
```

### 4. `return`

`return` mengembalikan nilai dari fungsi. Nilai tersebut dapat disimpan atau diolah lagi.

```python
def luas_persegi(sisi):
    return sisi * sisi

luas = luas_persegi(5)
print(luas)
print(luas * 2)
```

Output:

```text
25
50
```

Perbedaan `print()` dan `return`:

- `print()` hanya menampilkan nilai ke layar.
- `return` mengirim nilai kembali ke pemanggil.

```python
def tambah_tanpa_return(a, b):
    print(a + b)

def tambah_dengan_return(a, b):
    return a + b

hasil1 = tambah_tanpa_return(2, 3)
hasil2 = tambah_dengan_return(2, 3)

print(hasil1)
print(hasil2)
```

Output:

```text
5
None
5
```

Fungsi tanpa `return` mengembalikan `None`.

`return` juga dapat mengembalikan beberapa nilai:

```python
def statistik(a, b):
    return a + b, a * b

jumlah, kali = statistik(4, 5)
print(jumlah)
print(kali)
```

Output:

```text
9
20
```

### 5. Parameter Default dan Argumen Kata Kunci

Parameter dapat diberi nilai default.

```python
def sapa(nama, salam="Halo"):
    print(f"{salam}, {nama}!")

sapa("Ayu")
sapa("Budi", "Selamat pagi")
```

Output:

```text
Halo, Ayu!
Selamat pagi, Budi!
```

Argumen juga dapat dikirim dengan nama parameter:

```python
sapa(salam="Selamat malam", nama="Citra")
```

Output:

```text
Selamat malam, Citra!
```

Aturan: parameter tanpa default harus ditulis sebelum parameter dengan default.

### 6. Ruang Lingkup Variabel

Variabel di dalam fungsi bersifat **lokal**: hanya dapat diakses di dalam fungsi tersebut.

```python
def hitung():
    hasil = 10
    print(hasil)

hitung()
print(hasil)
```

Output:

```text
10
NameError: name 'hasil' is not defined
```

Variabel di luar fungsi bersifat **global**. Sebaiknya fungsi menerima data melalui parameter dan mengembalikan hasil melalui `return`, bukan mengubah variabel global.

```python
def hitung(angka):
    return angka * 2

nilai = 5
print(hitung(nilai))
```

Output:

```text
10
```

### 7. Docstring

Docstring adalah penjelasan singkat di awal fungsi. Berguna untuk dokumentasi.

```python
def luas_lingkaran(r):
    """Menghitung luas lingkaran dengan jari-jari r."""
    return 3.14159 * r * r

print(luas_lingkaran(7))
```

Output:

```text
153.93791
```

### 8. Mengimpor Modul Standar

Python memiliki banyak modul siap pakai. Gunakan `import`.

**Modul `math`:**

```python
import math

print(math.pi)
print(math.sqrt(16))
print(math.ceil(3.2))
print(math.floor(3.8))
```

Output:

```text
3.141592653589793
4.0
4
3
```

**Modul `random`:**

```python
import random

print(random.randint(1, 6))
print(random.choice(["batu", "gunting", "kertas"]))
```

Contoh output (berubah setiap dijalankan):

```text
5
gunting
```

**Mengimpor nama tertentu:**

```python
from math import sqrt, pi

print(sqrt(25))
print(pi)
```

### 9. Membuat Modul Sendiri

Simpan fungsi dalam file `geometri.py`:

```python
def luas_persegi(sisi):
    return sisi * sisi

def luas_lingkaran(r):
    return 3.14159 * r * r
```

Buat file `main.py` di folder yang sama:

```python
import geometri

print(geometri.luas_persegi(4))
print(geometri.luas_lingkaran(7))
```

Output:

```text
16
153.93791
```

Nama file modul ditulis tanpa `.py` saat diimpor.

### 10. Menjalankan Modul Secara Langsung

Tambahkan blok berikut agar kode pengujian hanya berjalan saat file dieksekusi langsung, bukan saat diimpor.

```python
def luas_persegi(sisi):
    return sisi * sisi

if __name__ == "__main__":
    print(luas_persegi(4))
```

Saat `python geometri.py` dijalankan, output `16` muncul. Saat diimpor dari file lain, blok tersebut tidak dijalankan.

### 11. Kesalahan Umum

| Kesalahan | Contoh | Akibat | Perbaikan |
|---|---|---|---|
| Lupa `return` | Fungsi hanya `print` | Hasil tidak bisa diolah, bernilai `None` | Gunakan `return` |
| Lupa memanggil | `def sapa(): ...` lalu `sapa` | Fungsi tidak berjalan | Tulis `sapa()` |
| Salah jumlah argumen | `sapa()` padahal butuh `nama` | `TypeError` | Kirim argumen yang sesuai |
| Variabel lokal diakses di luar | `print(hasil)` | `NameError` | Kembalikan nilai dengan `return` |
| Fungsi dipanggil sebelum dibuat | Panggilan di atas `def` | `NameError` | Pindahkan `def` ke atas |
| Nama file sama dengan modul | `math.py` | Modul standar tertutupi | Ganti nama file |
| Indentasi salah | `return` di luar fungsi | `SyntaxError` | Periksa indentasi |

### 12. Penanganan Error Sederhana (Pengayaan)

`try-except` dapat mencegah program berhenti ketika input bukan angka.

```python
try:
    umur = int(input("Masukkan umur: "))
    print(f"Umur: {umur}")
except ValueError:
    print("Input harus berupa angka bulat.")
```

Jika pengguna mengetik `dua`, blok `except` dijalankan dan program tidak berhenti. Materi ini berguna untuk validasi input pada proyek akhir.

### 13. Tips Merancang Fungsi

- Satu fungsi sebaiknya mengerjakan **satu tugas**.
- Beri nama dengan kata kerja: `hitung_total`, `cari_mahasiswa`, `tampilkan_menu`.
- Gunakan parameter untuk data masukan.
- Gunakan `return` untuk hasil yang akan dipakai lagi.
- Hindari fungsi yang terlalu panjang; pecah menjadi fungsi kecil.

---

## Tugas Praktikum

Simpan setiap tugas sebagai file terpisah, misalnya `tugas8_1.py`.

### Tugas 8.1 — Fungsi Geometri

Buat tiga fungsi:

- `luas_persegi_panjang(panjang, lebar)`
- `luas_lingkaran(r)`
- `volume_balok(panjang, lebar, tinggi)`

Lalu buat program utama yang meminta input dan memanggil ketiga fungsi tersebut.

Contoh interaksi:

```text
Panjang: 8
Lebar: 5
Tinggi: 3
Jari-jari: 7
Luas persegi panjang: 40.0
Luas lingkaran: 153.94
Volume balok: 120.0
```

**Ketentuan:** setiap fungsi menggunakan `return`. Tampilkan luas lingkaran dua angka di belakang koma.

### Tugas 8.2 — Validasi dan Konversi Nilai

Buat dua fungsi:

- `validasi_nilai(nilai)` mengembalikan `True` jika `0 <= nilai <= 100`, selain itu `False`.
- `konversi_huruf(nilai)` mengembalikan huruf A–E berdasarkan rentang pada Modul 3.

Program meminta nilai, memvalidasi, lalu menampilkan huruf atau pesan `Nilai tidak valid`.

Contoh interaksi:

```text
Masukkan nilai: 82
Nilai huruf: B
```

**Ketentuan:** fungsi `konversi_huruf` hanya dipanggil jika nilai valid.

### Tugas 8.3 — Kalkulator Modular

Buat empat fungsi:

- `tambah(a, b)`
- `kurang(a, b)`
- `kali(a, b)`
- `bagi(a, b)`

Fungsi `bagi` mengembalikan `None` jika `b == 0`.

Buat program utama yang meminta dua bilangan dan pilihan operasi, lalu memanggil fungsi yang sesuai.

Contoh interaksi:

```text
Bilangan pertama: 10
Bilangan kedua: 4
Operasi (tambah/kurang/kali/bagi): bagi
Hasil: 2.5
```

Jika pembagi nol:

```text
Hasil: Pembagian dengan nol tidak diperbolehkan.
```

**Ketentuan:** gunakan `if-elif` atau `match-case` untuk memilih fungsi.

### Tugas 8.4 — Modul `math` dan `random`

Buat program yang:

1. Meminta sebuah bilangan, lalu menampilkan akar kuadrat, pembulatan ke atas, dan pembulatan ke bawah menggunakan `math`.
2. Melempar dadu 20 kali menggunakan `random.randint(1, 6)`.
3. Menghitung berapa kali setiap mata dadu muncul menggunakan `dict`.

Contoh interaksi:

```text
Masukkan bilangan: 20
Akar kuadrat: 4.47
Pembulatan ke atas: 5
Pembulatan ke bawah: 4
Hasil lemparan: [3, 6, 1, 4, ...]
Frekuensi: {1: 4, 2: 3, 3: 5, 4: 2, 5: 4, 6: 2}
```

**Ketentuan:** hasil random boleh berbeda; pastikan total frekuensi 20.

### Tugas 8.5 — Modul Buatan Sendiri

Buat dua file dalam satu folder:

**`konversi.py`** berisi:

- `celsius_ke_fahrenheit(celsius)`
- `km_ke_meter(km)`
- `kg_ke_gram(kg)`

**`main.py`** mengimpor `konversi` dan meminta input, lalu menampilkan hasil ketiga konversi.

Contoh interaksi:

```text
Suhu Celsius: 30
Jarak (km): 2.5
Berat (kg): 1.2
Fahrenheit: 86.0
Meter: 2500.0
Gram: 1200.0
```

**Ketentuan:** gunakan `import konversi`, bukan menyalin fungsi ke `main.py`.

### Tugas 8.6 — Tantangan: Refactor Program

Perhatikan program prosedural berikut.

```python
mahasiswa = []

for i in range(3):
    nama = input("Nama: ")
    tugas = float(input("Nilai tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))

    akhir = 0.3 * tugas + 0.3 * uts + 0.4 * uas

    if akhir >= 85:
        huruf = "A"
    elif akhir >= 75:
        huruf = "B"
    elif akhir >= 65:
        huruf = "C"
    elif akhir >= 55:
        huruf = "D"
    else:
        huruf = "E"

    mahasiswa.append({
        "nama": nama,
        "akhir": akhir,
        "huruf": huruf
    })

for data in mahasiswa:
    print(f"{data['nama']}: {data['akhir']:.2f} ({data['huruf']})")
```

Refactor program tersebut menjadi:

- `hitung_nilai_akhir(tugas, uts, uas)`
- `konversi_huruf(nilai)`
- `buat_data_mahasiswa(nama, tugas, uts, uas)`
- `tampilkan_data(mahasiswa)`
- `main()`

**Ketentuan:**

- Setiap fungsi memiliki satu tanggung jawab.
- Program utama meminta 3 data mahasiswa.
- Hasil output sama seperti program awal.
- Tidak boleh ada duplikasi logika perhitungan.

---

## Rangkuman

- Fungsi dibuat dengan `def` dan dipanggil dengan `nama_fungsi()`.
- Parameter menerima data; `return` mengembalikan hasil.
- Fungsi tanpa `return` menghasilkan `None`.
- Parameter default dan argumen kata kunci memberikan fleksibilitas.
- Variabel di dalam fungsi bersifat lokal.
- Modul standar seperti `math` dan `random` dapat diimpor.
- File Python dapat dijadikan modul sendiri dan diimpor ke file lain.

## Istilah Penting

| Istilah | Arti |
|---|---|
| Fungsi | Blok kode bernama yang dapat dipanggil |
| Parameter | Variabel pada definisi fungsi |
| Argumen | Nilai yang dikirim saat memanggil fungsi |
| `return` | Mengembalikan nilai dari fungsi |
| Scope | Ruang lingkup akses variabel |
| Modul | File Python berisi kode yang dapat diimpor |
| Docstring | Dokumentasi singkat di dalam fungsi |

## Checklist Sebelum Lanjut

- [ ] Saya dapat membuat dan memanggil fungsi.
- [ ] Saya dapat menggunakan parameter dan `return`.
- [ ] Saya dapat menggunakan parameter default dan argumen kata kunci.
- [ ] Saya memahami perbedaan variabel lokal dan global.
- [ ] Saya dapat mengimpor `math` dan `random`.
- [ ] Saya dapat membuat modul sendiri.
- [ ] Saya sudah mengerjakan seluruh tugas.

## Langkah Selanjutnya

Setelah menyelesaikan Modul 8, lanjutkan ke [Proyek Akhir Tahap 2](../proyek-akhir/README.md#tahap-2--proyek-lanjutan-modul-18) untuk menerapkan seluruh materi.
