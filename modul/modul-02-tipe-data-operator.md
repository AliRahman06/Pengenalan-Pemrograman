# Modul 2 — Variabel, Tipe Data, Operator, dan Ekspresi

## Tujuan Praktikum

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. Membuat dan menggunakan variabel dengan aturan penamaan yang benar.
2. Menerima input, mengubah tipe data, dan menampilkan nilai dengan f-string.
3. Membedakan tipe data `int`, `float`, `str`, dan `bool`.
4. Menggunakan operator aritmatika, perbandingan, logika, dan penugasan.
5. Menghitung ekspresi dengan urutan operasi yang benar serta menampilkan hasil dengan format yang rapi.

**Prasyarat:** Modul 1 — Pengenalan Pemrograman dan Instalasi Lingkungan Kerja.  
**Estimasi waktu:** 2 jam.

---

## Dasar Teori

### 1. Variabel dan Penugasan

Variabel adalah **wadah bernama** untuk menyimpan nilai. Nilai dimasukkan dengan tanda `=`.

```python
nama = "Ayu"
umur = 18
print(nama)
print(umur)
```

Output:

```text
Ayu
18
```

Variabel dapat digunakan kembali dan nilainya dapat diganti:

```python
skor = 70
print(skor)

skor = 90
print(skor)
```

Output:

```text
70
90
```

Penugasan `skor = 90` mengganti nilai lama. Variabel hanya menyimpan nilai terakhir yang diberikan.

### 2. Aturan Nama Variabel

- Boleh mengandung huruf, angka, dan garis bawah `_`.
- Tidak boleh diawali angka.
- Tidak boleh memakai spasi.
- Tidak boleh memakai kata kunci Python seperti `if`, `for`, atau `class`.
- Bersifat *case-sensitive*: `nama` berbeda dengan `Nama`.
- Gunakan gaya `snake_case`, contoh `nilai_akhir`.
- Pilih nama yang menjelaskan isi variabel, bukan nama acak.

Contoh nama yang benar:

```python
nama_mahasiswa = "Budi"
nilai_uts = 85
jumlah_barang = 3
```

### 3. Tipe Data Dasar

Tipe data menentukan **jenis nilai** yang disimpan. Bayangkan tipe data seperti jenis wadah: ada wadah untuk angka, ada wadah untuk teks.

| Tipe | Nama | Contoh | Keterangan |
|---|---|---|---|
| `int` | Bilangan bulat | `10`, `-3`, `0` | Tidak memiliki titik desimal |
| `float` | Bilangan desimal | `3.14`, `-0.5`, `2.0` | Menggunakan titik, bukan koma |
| `str` | Teks (string) | `"Halo"`, `'123'` | Selalu diapit tanda kutip |
| `bool` | Boolean | `True`, `False` | Hanya dua nilai |

Perhatikan bahwa `123` adalah `int`, sedangkan `"123"` adalah `str`. Keduanya terlihat mirip, tetapi berbeda tipe.

### 4. Memeriksa Tipe Data

Gunakan `type()`.

```python
print(type(10))
print(type(3.14))
print(type("Halo"))
print(type(True))
```

Output:

```text
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
```

### 5. Menerima Input dan Casting

`input()` membaca teks yang diketik pengguna. **Hasil `input()` selalu berupa teks (`str`).**

```python
nama = input("Masukkan nama: ")
print(f"Halo, {nama}!")
```

Contoh interaksi:

```text
Masukkan nama: Sari
Halo, Sari!
```

Jika input berupa angka, ubah tipenya terlebih dahulu:

```python
umur = int(input("Masukkan umur: "))
print(f"Tahun depan umurmu {umur + 1} tahun.")
```

Contoh interaksi:

```text
Masukkan umur: 18
Tahun depan umurmu 19 tahun.
```

Casting adalah proses mengubah tipe data.

```python
angka_teks = "25"
angka_bulat = int(angka_teks)
angka_desimal = float(angka_teks)

print(angka_bulat + 5)
print(angka_desimal + 0.5)
print(str(100) + " poin")
```

Output:

```text
30
25.5
100 poin
```

Aturan penting:

- `int("25")` berhasil, tetapi `int("dua puluh lima")` gagal dengan `ValueError`.
- `int("3.5")` gagal; gunakan `int(float("3.5"))` bila ingin memotong desimal.
- `int(3.9)` menghasilkan `3` karena bagian desimal dibuang, bukan dibulatkan.
- Hampir semua nilai dapat diubah menjadi teks dengan `str()`.

### 6. Menampilkan Variabel

Tiga cara yang umum:

```python
nama = "Budi"
umur = 19

print("Nama:", nama)
print("Nama: " + nama)
print(f"Nama: {nama}, umur: {umur}")
```

Output:

```text
Nama: Budi
Nama: Budi
Nama: Budi, umur: 19
```

Cara ketiga disebut **f-string**. Awali teks dengan `f`, lalu tulis variabel di dalam `{}`. F-string adalah cara yang paling disarankan karena dapat menggabungkan teks dan beberapa nilai dengan rapi.

### 7. Operator Aritmatika

| Operator | Nama | Contoh | Hasil |
|---|---|---|---|
| `+` | Penjumlahan | `7 + 3` | `10` |
| `-` | Pengurangan | `7 - 3` | `4` |
| `*` | Perkalian | `7 * 3` | `21` |
| `/` | Pembagian | `7 / 2` | `3.5` |
| `//` | Pembagian bulat | `7 // 2` | `3` |
| `%` | Modulo (sisa bagi) | `7 % 2` | `1` |
| `**` | Pangkat | `2 ** 3` | `8` |

Catatan:

- `/` selalu menghasilkan `float`.
- `//` membuang bagian desimal ke bawah.
- `%` menghasilkan sisa pembagian.
- `**` digunakan untuk pangkat, bukan `^`.

Contoh:

```python
print(17 / 5)
print(17 // 5)
print(17 % 5)
print(2 ** 4)
```

Output:

```text
3.4
3
2
16
```

### 8. Operator pada String

Tanda `+` menggabungkan teks, sedangkan `*` mengulang teks.

```python
print("Py" + "thon")
print("ha" * 3)
```

Output:

```text
Python
hahaha
```

Teks tidak dapat langsung dijumlahkan dengan angka:

```python
print("Umur: " + 18)
```

Kode di atas menghasilkan `TypeError`. Perbaiki dengan `str(18)` atau f-string:

```python
print("Umur: " + str(18))
print(f"Umur: {18}")
```

### 9. Operator Perbandingan

Perbandingan menghasilkan `bool`.

| Operator | Arti | Contoh | Hasil |
|---|---|---|---|
| `==` | Sama dengan | `5 == 5` | `True` |
| `!=` | Tidak sama dengan | `5 != 3` | `True` |
| `>` | Lebih besar | `5 > 3` | `True` |
| `<` | Lebih kecil | `5 < 3` | `False` |
| `>=` | Lebih besar atau sama | `5 >= 5` | `True` |
| `<=` | Lebih kecil atau sama | `4 <= 5` | `True` |

Jangan tertukar antara `=` (penugasan) dan `==` (perbandingan).

### 10. Operator Logika

| Operator | Arti | Contoh | Hasil |
|---|---|---|---|
| `and` | Keduanya benar | `True and False` | `False` |
| `or` | Salah satu benar | `True or False` | `True` |
| `not` | Membalik nilai | `not True` | `False` |

Operator logika akan banyak dipakai pada modul percabangan.

### 11. Operator Penugasan

Selain `=`, ada bentuk singkat:

```python
skor = 10
skor += 5
skor *= 2
print(skor)
```

Output:

```text
30
```

`skor += 5` sama dengan `skor = skor + 5`.

### 12. Urutan Operasi

Python mengikuti urutan berikut:

1. Tanda kurung `()`
2. Pangkat `**`
3. Perkalian, pembagian, pembagian bulat, modulo: `* / // %`
4. Penjumlahan dan pengurangan: `+ -`
5. Perbandingan: `== != > < >= <=`
6. `not`
7. `and`
8. `or`

Contoh:

```python
hasil = 2 + 3 * 4
print(hasil)
```

Output:

```text
14
```

Bukan `20`, karena perkalian dikerjakan lebih dulu. Gunakan tanda kurung jika ingin mengubah urutan:

```python
print((2 + 3) * 4)
```

Output:

```text
20
```

### 13. Format Angka dengan f-string

```python
nilai = 87.4567
print(f"Nilai: {nilai:.2f}")
print(f"Harga: Rp{nilai:,.0f}")
```

Output:

```text
Nilai: 87.46
Harga: Rp87
```

Penjelasan:

- `:.2f` menampilkan dua angka di belakang koma.
- `:,` menambahkan pemisah ribuan.
- `:.0f` menampilkan bilangan bulat tanpa desimal.
- `:02d` menambahkan nol di depan agar lebar angka selalu dua digit.
- `:<12` membuat teks rata kiri dengan lebar minimum 12 karakter.

### 14. Kesalahan Umum

| Kesalahan | Contoh | Penyebab | Perbaikan |
|---|---|---|---|
| `NameError` | `print(nama)` | Variabel belum dibuat | Buat dulu: `nama = "Ayu"` |
| `TypeError` | `"5" + 5` | Teks dijumlahkan dengan angka | `int("5") + 5` |
| `ValueError` | `int("3.5")` | Format teks bukan bilangan bulat | `int(float("3.5"))` |
| `ZeroDivisionError` | `10 / 0` | Pembagian dengan nol | Periksa nilai pembagi |
| Hasil tak terduga | `1 / 2` dianggap `0` | `/` menghasilkan desimal | Gunakan `//` bila ingin bulat |
| Salah urutan | `2 + 3 * 4` dianggap `20` | Perkalian didahulukan | Tambahkan `(2 + 3) * 4` |

### 15. Tips Praktikum

- Buat variabel dengan nama yang menjelaskan isinya.
- Konversi input ke `int()` atau `float()` sebelum melakukan perhitungan.
- Gunakan f-string agar output lebih mudah dibaca.
- Uji ekspresi kecil di mode interaktif sebelum memasukkannya ke program besar.
- Jika muncul error, periksa tipe data dan nama variabel terlebih dahulu.

### 16. Contoh Implementasi

Beberapa contoh penerapan materi modul ini dalam kasus kecil.

**1. Total belanja**

```python
nama_barang = input("Nama barang: ")
harga = float(input("Harga satuan: "))
jumlah = int(input("Jumlah beli: "))

subtotal = harga * jumlah
print(f"{nama_barang} x {jumlah} = Rp{subtotal:,.0f}")
```

Contoh interaksi:

```text
Nama barang: Buku
Harga satuan: 45000
Jumlah beli: 3
Buku x 3 = Rp135,000
```

**2. Konversi detik ke jam, menit, dan detik**

```python
total_detik = int(input("Total detik: "))

jam = total_detik // 3600
menit = (total_detik % 3600) // 60
detik = total_detik % 60

print(f"{total_detik} detik = {jam} jam {menit} menit {detik} detik")
```

Contoh interaksi:

```text
Total detik: 3675
3675 detik = 1 jam 1 menit 15 detik
```

**3. Konversi suhu Celsius ke Fahrenheit**

```python
celsius = float(input("Suhu Celsius: "))
fahrenheit = celsius * 9 / 5 + 32

print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")
```

Contoh interaksi:

```text
Suhu Celsius: 30
30.0°C = 86.0°F
```

---

## Tugas Praktikum

Simpan setiap tugas sebagai file terpisah, misalnya `tugas2_1.py`.

### Tugas 2.1 — Biodata Interaktif

Minta pengguna memasukkan nama, umur, dan kota. Tampilkan hasilnya.

Contoh interaksi:

```text
Masukkan nama: Rina
Masukkan umur: 18
Masukkan kota: Bandung
Halo Rina, umur Anda 18 tahun dan Anda tinggal di Bandung.
```

**Ketentuan:**

- Simpan umur sebagai bilangan bulat.
- Tampilkan umur tahun depan.
- Gunakan f-string.

Contoh tambahan output:

```text
Tahun depan umur Anda 19 tahun.
```

### Tugas 2.2 — Rata-rata Nilai

Minta tiga nilai praktikum, lalu tampilkan rata-ratanya.

Contoh interaksi:

```text
Nilai 1: 80
Nilai 2: 90
Nilai 3: 75
Rata-rata: 81.67
```

**Ketentuan:** gunakan `float()`, tampilkan dua angka di belakang koma, dan tampilkan juga tipe data hasil rata-rata dengan `type()`.

### Tugas 2.3 — Prediksi Ekspresi

Tanpa menjalankan program, tuliskan hasil dan tipe data dari ekspresi berikut. Setelah itu, buktikan dengan kode Python.

1. `7 + 3 * 2`
2. `(7 + 3) * 2`
3. `10 / 4`
4. `10 // 4`
5. `10 % 4`
6. `2 ** 5`
7. `"2" + "3"`
8. `"2" * 3`
9. `5 > 3 and 2 < 1`
10. `not (4 == 4)`

**Ketentuan:** tulis jawaban di kertas atau komentar file, lalu bandingkan dengan hasil program. Gunakan perintah `print()` terpisah untuk setiap ekspresi.

### Tugas 2.4 — Indeks Massa Tubuh (BMI)

Rumus BMI:

```text
BMI = berat (kg) / (tinggi dalam meter) ** 2
```

Contoh interaksi:

```text
Berat badan (kg): 60
Tinggi badan (cm): 165
BMI: 22.04
```

**Ketentuan:** input tinggi dalam cm, ubah ke meter dengan membagi 100, lalu tampilkan dua angka di belakang koma.

### Tugas 2.5 — Struk Belanja

Minta nama barang, harga satuan, dan jumlah beli. Hitung subtotal, pajak 11%, dan total.

Contoh interaksi:

```text
Nama barang: Buku
Harga satuan: 45000
Jumlah: 3
Subtotal: Rp135,000
Pajak 11%: Rp14,850
Total: Rp149,850
```

**Ketentuan:** gunakan `int()` untuk jumlah, `float()` untuk harga, dan format rupiah tanpa desimal.

### Tugas 2.6 — Tantangan: Kartu Profil

Buat program yang meminta nama, tahun lahir, dan tinggi badan (cm). Program menampilkan kartu profil.

Contoh interaksi:

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

**Ketentuan:**

- Asumsikan tahun sekarang 2026.
- Hitung umur dari tahun lahir.
- Gunakan f-string dan perataan teks secukupnya.

---

## Rangkuman

- Variabel dibuat dengan `nama_variabel = nilai` dan harus mengikuti aturan penamaan.
- Tipe data utama: `int`, `float`, `str`, dan `bool`.
- `input()` selalu menghasilkan teks; gunakan `int()` atau `float()` untuk perhitungan.
- `type()` memeriksa tipe; `int()`, `float()`, dan `str()` mengubah tipe.
- `/` menghasilkan desimal, `//` menghasilkan pembagian bulat, `%` menghasilkan sisa bagi.
- `==` membandingkan, sedangkan `=` memberi nilai.
- Python mendahulukan kurung, pangkat, perkalian, lalu penjumlahan.
- f-string dapat menggabungkan teks dan variabel serta mengatur format angka.

## Istilah Penting

| Istilah | Arti |
|---|---|
| Variabel | Nama yang menyimpan sebuah nilai |
| Penugasan | Proses memberi nilai ke variabel dengan `=` |
| Casting | Proses mengubah tipe data |
| Operand | Nilai yang dioperasikan, misalnya `5` dan `3` pada `5 + 3` |
| Operator | Simbol yang melakukan operasi, misalnya `+` atau `*` |
| Ekspresi | Kombinasi nilai dan operator yang menghasilkan nilai baru |
| Modulo | Sisa hasil pembagian |
| Precedence | Urutan prioritas operasi |
| f-string | Format teks yang memungkinkan penyisipan variabel dengan `{}` |

## Checklist Sebelum Lanjut

- [ ] Saya dapat membuat variabel dengan nama yang benar.
- [ ] Saya dapat menerima input dan mengubah tipenya.
- [ ] Saya dapat menampilkan variabel dengan f-string.
- [ ] Saya dapat membedakan `int`, `float`, `str`, dan `bool`.
- [ ] Saya dapat melakukan casting dengan benar.
- [ ] Saya dapat menggunakan operator aritmatika dan perbandingan.
- [ ] Saya memahami perbedaan `/`, `//`, dan `%`.
- [ ] Saya dapat memformat angka dengan f-string.
- [ ] Saya sudah mengerjakan seluruh tugas.

## Langkah Selanjutnya

Lanjutkan ke [Modul 3 — Percabangan `if-else`](modul-03-percabangan-if-else.md).
