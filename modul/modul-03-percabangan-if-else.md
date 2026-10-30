# Modul 3 — Percabangan `if-else`

## Tujuan Praktikum

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. Menjelaskan cara program mengambil keputusan dengan `if`.
2. Menggunakan `if`, `elif`, dan `else` untuk beberapa kemungkinan.
3. Menyusun percabangan bersarang (*nested*) dengan benar.
4. Menggabungkan beberapa kondisi menggunakan `and`, `or`, dan `not`.
5. Menentukan urutan kondisi yang tepat agar hasil sesuai aturan.

**Prasyarat:** Modul 1 dan Modul 2.  
**Estimasi waktu:** 2 jam.

> Setelah modul ini, pilihan berbasis menu akan dipelajari di Modul 4 dengan `match-case`.

---

## Dasar Teori

### 1. Konsep Percabangan

Percabangan membuat program memilih langkah berdasarkan kondisi. Bayangkan lampu lalu lintas: jika lampu hijau, kendaraan berjalan; jika merah, kendaraan berhenti.

Kondisi pada Python berupa ekspresi yang bernilai `True` atau `False`.

### 2. Percabangan `if`

Bentuk dasar:

```python
if kondisi:
    perintah_yang_dijalankan
```

Contoh:

```python
nilai = 80

if nilai >= 75:
    print("Selamat, Anda lulus.")
```

Output:

```text
Selamat, Anda lulus.
```

Perhatikan:

- Setelah kondisi wajib ada tanda titik dua `:`.
- Baris di dalam `if` harus menjorok ke dalam (umumnya 4 spasi).
- Jika kondisi `False`, blok di dalam `if` dilewati.

### 3. `if` dan `else`

`else` dijalankan jika kondisi `if` bernilai `False`.

```python
nilai = 60

if nilai >= 75:
    print("Lulus")
else:
    print("Belum lulus")
```

Output:

```text
Belum lulus
```

`else` tidak memiliki kondisi dan tidak boleh ditulis sebelum `if`.

### 4. `if`, `elif`, dan `else`

Gunakan `elif` (singkatan dari *else if*) untuk memeriksa beberapa kemungkinan secara berurutan. Python berhenti memeriksa setelah menemukan kondisi pertama yang `True`.

```python
nilai = 82

if nilai >= 85:
    print("A")
elif nilai >= 75:
    print("B")
elif nilai >= 65:
    print("C")
else:
    print("D")
```

Output:

```text
B
```

Urutan penting. Jika `if nilai >= 65` ditulis paling atas, semua nilai di atas 65 akan mendapat `C` dan kondisi berikutnya tidak diperiksa.

### 5. Percabangan Bersarang

Percabangan bersarang adalah `if` di dalam `if`. Gunakan hanya bila memang diperlukan agar kode tidak sulit dibaca.

```python
umur = 20
punya_sim = True

if umur >= 17:
    if punya_sim:
        print("Boleh mengendarai mobil.")
    else:
        print("Cukup umur, tetapi belum memiliki SIM.")
else:
    print("Belum cukup umur.")
```

Output:

```text
Boleh mengendarai mobil.
```

### 6. Menggabungkan Kondisi

| Operator | Arti | Contoh | Hasil |
|---|---|---|---|
| `and` | Semua kondisi harus benar | `umur >= 17 and punya_sim` | `True` bila keduanya benar |
| `or` | Salah satu kondisi benar | `nilai < 0 or nilai > 100` | `True` bila salah satu benar |
| `not` | Membalik kondisi | `not lulus` | `True` bila `lulus` bernilai `False` |

Contoh:

```python
nilai = 105

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
```

Output:

```text
Nilai tidak valid
```

### 7. Indentasi

Python menggunakan indentasi untuk menentukan blok kode.

```python
if True:
    print("Baris ini di dalam if")
print("Baris ini di luar if")
```

Output:

```text
Baris ini di dalam if
Baris ini di luar if
```

Jika indentasi tidak konsisten, muncul `IndentationError`. Pilih 4 spasi dan gunakan secara konsisten.

### 8. Kesalahan Umum

| Kesalahan | Contoh | Akibat | Perbaikan |
|---|---|---|---|
| Lupa titik dua | `if nilai > 75` | `SyntaxError` | `if nilai > 75:` |
| Memakai `=` | `if nilai = 75:` | `SyntaxError` | `if nilai == 75:` |
| Indentasi salah | Blok `if` tidak menjorok | `IndentationError` | Beri 4 spasi |
| `elif` setelah `else` | `else:` lalu `elif` | `SyntaxError` | Letakkan `elif` sebelum `else` |
| Membandingkan tipe berbeda | `input(...) > 75` | `TypeError` | Ubah dengan `int()` |
| Urutan kondisi salah | Rentang besar diperiksa lebih dulu | Hasil keliru | Periksa dari kondisi paling spesifik |

### 9. Tips Menulis Kondisi

- Baca kondisi seperti kalimat: "jika nilai lebih besar atau sama dengan 75, maka ...".
- Gunakan tanda kurung untuk memperjelas kondisi gabungan.
- Uji batas nilai, misalnya `74`, `75`, dan `76`.
- Hindari percabangan terlalu dalam; pertimbangkan `elif` atau fungsi.

### 10. Contoh Implementasi

Beberapa contoh penerapan materi modul ini dalam kasus kecil.

**1. Kategori suhu**

```python
suhu = float(input("Suhu udara (°C): "))

if suhu < 0:
    print("Dingin sekali")
elif suhu < 20:
    print("Sejuk")
elif suhu < 30:
    print("Hangat")
else:
    print("Panas")
```

Contoh interaksi:

```text
Suhu udara (°C): 25
Hangat
```

**2. Pemeriksaan SIM dengan percabangan bersarang**

```python
umur = int(input("Umur: "))
punya_sim = input("Punya SIM? (ya/tidak): ")

if umur >= 17:
    if punya_sim == "ya" or punya_sim == "Ya":
        print("Boleh mengendarai mobil.")
    else:
        print("Cukup umur, tetapi belum memiliki SIM.")
else:
    print("Belum cukup umur.")
```

Contoh interaksi:

```text
Umur: 20
Punya SIM? (ya/tidak): ya
Boleh mengendarai mobil.
```

**3. Validasi nilai dengan `or`**

```python
nilai = int(input("Nilai: "))

if nilai < 0 or nilai > 100:
    print("Nilai tidak valid")
else:
    print("Nilai valid")
```

Contoh interaksi:

```text
Nilai: 120
Nilai tidak valid
```

---

## Tugas Praktikum

Simpan setiap tugas sebagai file terpisah, misalnya `tugas3_1.py`.

### Tugas 3.1 — Ganjil atau Genap

Minta satu bilangan bulat, lalu tentukan apakah bilangan tersebut ganjil atau genap.

Contoh interaksi:

```text
Masukkan bilangan: 7
7 adalah bilangan ganjil.
```

**Ketentuan:** gunakan operator modulo `%`.

### Tugas 3.2 — Nilai Huruf

Minta nilai akhir 0–100, lalu tampilkan nilai huruf dengan aturan:

| Rentang | Huruf |
|---|---|
| 85–100 | A |
| 75–84 | B |
| 65–74 | C |
| 55–64 | D |
| 0–54 | E |

Jika nilai di luar 0–100, tampilkan `Nilai tidak valid`.

Contoh interaksi:

```text
Masukkan nilai: 82
Nilai huruf: B
```

**Ketentuan:** gunakan `if-elif-else`. Uji nilai `85`, `84`, `75`, `0`, `-1`, dan `101`.

### Tugas 3.3 — Tahun Kabisat

Minta tahun, lalu tentukan apakah tahun tersebut kabisat.

Aturan tahun kabisat:

- Habis dibagi 400, atau
- Habis dibagi 4 tetapi tidak habis dibagi 100.

Contoh interaksi:

```text
Masukkan tahun: 2024
2024 adalah tahun kabisat.
```

```text
Masukkan tahun: 1900
1900 bukan tahun kabisat.
```

**Ketentuan:** gunakan `and`, `or`, dan `%`.

### Tugas 3.4 — Diskon Belanja

Minta total belanja, lalu hitung diskon dan total yang harus dibayar.

| Total belanja | Diskon |
|---|---|
| ≥ 500000 | 20% |
| ≥ 250000 | 10% |
| ≥ 100000 | 5% |
| < 100000 | 0% |

Contoh interaksi:

```text
Total belanja: 300000
Diskon: Rp30,000
Total bayar: Rp270,000
```

**Ketentuan:** periksa dari nominal terbesar, lalu tampilkan diskon dalam rupiah dan total akhir.

### Tugas 3.5 — Login Sederhana

Buat program login dengan ketentuan:

- Username yang benar: `admin`
- Password yang benar: `python123`

Tampilkan `Login berhasil` jika keduanya benar, dan `Username atau password salah` jika tidak.

Contoh interaksi:

```text
Username: admin
Password: python123
Login berhasil
```

**Ketentuan:** gunakan `and`. Jangan tampilkan password yang diketik.

### Tugas 3.6 — Tantangan: Tarif Parkir

Buat program penghitung tarif parkir dengan aturan:

| Jenis kendaraan | Tarif per jam |
|---|---|
| Motor | Rp2,000 |
| Mobil | Rp5,000 |
| Truk | Rp10,000 |

Ketentuan tambahan:

- Durasi parkir dihitung dalam jam bulat dan harus lebih dari 0.
- Jika durasi lebih dari 5 jam, pengguna mendapat diskon 10% dari tarif dasar.
- Jenis kendaraan yang tidak dikenal harus ditolak.

Contoh interaksi:

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
Jenis kendaraan tidak valid.
```

**Ketentuan:**

- Gunakan `if-elif-else` dan percabangan bersarang.
- Gunakan `lower()` agar input `Mobil` dan `mobil` dianggap sama.
- Tampilkan biaya dengan format rupiah tanpa desimal.

---

## Rangkuman

- `if` menjalankan blok bila kondisi `True`.
- `else` menangani kondisi yang tidak terpenuhi.
- `elif` memeriksa kemungkinan tambahan secara berurutan.
- Kondisi dapat digabung dengan `and`, `or`, dan `not`.
- Urutan kondisi menentukan hasil, terutama untuk rentang nilai.
- Indentasi menentukan blok kode dan harus konsisten.
- Untuk memilih menu berdasarkan satu nilai, pelajari `match-case` di Modul 4.

## Istilah Penting

| Istilah | Arti |
|---|---|
| Kondisi | Ekspresi yang bernilai `True` atau `False` |
| Blok kode | Sekumpulan baris dengan indentasi sama |
| Nested | Berada di dalam blok lain |
| `elif` | Singkatan dari *else if* |
| Indentasi | Jarak menjorok di awal baris |

## Checklist Sebelum Lanjut

- [ ] Saya dapat menulis `if`, `elif`, dan `else` dengan benar.
- [ ] Saya memahami pengaruh urutan kondisi.
- [ ] Saya dapat menggabungkan kondisi dengan `and`, `or`, dan `not`.
- [ ] Saya dapat menggunakan percabangan bersarang.
- [ ] Saya dapat menentukan urutan kondisi yang benar.
- [ ] Saya sudah mengerjakan seluruh tugas.

## Langkah Selanjutnya

Lanjutkan ke [Modul 4 — Switch Case dengan `match-case`](modul-04-switch-case.md).
