# Modul 4 — Switch Case dengan `match-case`

## Tujuan Praktikum

Setelah menyelesaikan modul ini, mahasiswa mampu:

1. Menjelaskan bahwa Python menggunakan `match-case` sebagai padanan `switch-case`.
2. Menulis `match-case` untuk memilih berdasarkan satu nilai.
3. Menggunakan wildcard `_` untuk menangani pilihan yang tidak dikenal.
4. Menggabungkan beberapa pola dengan `|` dan menambahkan guard `if`.
5. Memilih antara `match-case` dan `if-elif` sesuai kebutuhan.

**Prasyarat:** Modul 1–3, Python 3.10 atau lebih baru.  
**Estimasi waktu:** 2 jam.

> Banyak bahasa lain memiliki `switch-case`. Python tidak memakai kata kunci `switch`, tetapi menyediakan `match-case` dengan tujuan yang sama: memilih satu blok berdasarkan nilai tertentu.

---

## Dasar Teori

### 1. Konsep Switch Case

Switch case adalah struktur untuk memilih satu kemungkinan dari beberapa nilai. Bayangkan tombol lantai pada lift: menekan tombol `3` membawa kita ke lantai 3, tombol `5` ke lantai 5, dan tombol lain tidak melakukan apa-apa.

Pada Python, struktur ini ditulis dengan `match-case`.

### 2. Sintaks Dasar

```python
pilihan = "2"

match pilihan:
    case "1":
        print("Mulai permainan")
    case "2":
        print("Lihat skor")
    case "3":
        print("Keluar")
    case _:
        print("Pilihan tidak dikenal")
```

Output:

```text
Lihat skor
```

Penjelasan:

- `match pilihan:` menentukan nilai yang diperiksa.
- Setiap `case nilai:` adalah kemungkinan.
- `case _:` adalah wildcard, yaitu semua nilai yang tidak cocok dengan case sebelumnya.
- Setiap blok case harus menjorok dan diakhiri dengan titik dua.

### 3. Mencocokkan Angka

```python
hari = 3

match hari:
    case 1:
        print("Senin")
    case 2:
        print("Selasa")
    case 3:
        print("Rabu")
    case _:
        print("Hari tidak valid")
```

Output:

```text
Rabu
```

Nilai `hari` bertipe `int`. Jika input dari pengguna, ubah dulu dengan `int()`.

### 4. Menggabungkan Pola dengan `|`

Tanda `|` berarti **atau**. Beberapa nilai dapat menuju blok yang sama.

```python
huruf = "a"

match huruf:
    case "a" | "i" | "u" | "e" | "o":
        print("Huruf vokal")
    case _:
        print("Bukan huruf vokal")
```

Output:

```text
Huruf vokal
```

### 5. Guard `if` pada Case

Guard adalah kondisi tambahan pada case. Tulis `if` setelah pola.

```python
umur = 15

match umur:
    case u if u < 0:
        print("Umur tidak valid")
    case u if u < 13:
        print("Anak")
    case u if u < 18:
        print("Remaja")
    case u if u < 60:
        print("Dewasa")
    case _:
        print("Lansia")
```

Output:

```text
Remaja
```

Variabel `u` adalah nama sementara untuk nilai yang dicocokkan. Guard diperiksa dari atas ke bawah.

### 6. Blok Lebih dari Satu Baris

Satu case dapat berisi beberapa perintah.

```python
pilihan = "2"

match pilihan:
    case "1":
        nama = "Budi"
        print(f"Selamat datang, {nama}.")
    case "2":
        print("Menu bantuan")
        print("Pilih 1 untuk mulai.")
    case _:
        print("Pilihan tidak tersedia")
```

Output:

```text
Menu bantuan
Pilih 1 untuk mulai.
```

### 7. Nilai yang Dicocokkan

`match-case` cocok untuk:

- pilihan menu berupa teks atau angka,
- kode kategori,
- nama perintah,
- pilihan yang jumlahnya terbatas.

Gunakan `if-elif` ketika:

- membandingkan rentang nilai tanpa guard,
- kondisi melibatkan banyak variabel,
- logika lebih mudah dibaca dengan perbandingan langsung.

### 8. Tidak Ada Fallthrough

Pada bahasa lain, `switch` sering membutuhkan `break`. Python tidak memerlukan itu: setelah satu case cocok, case lain tidak dijalankan.

```python
nilai = "A"

match nilai:
    case "A":
        print("Sangat baik")
    case "B":
        print("Baik")
```

Output:

```text
Sangat baik
```

### 9. Kesalahan Umum

| Kesalahan | Contoh | Akibat | Perbaikan |
|---|---|---|---|
| Lupa titik dua | `case 1` | `SyntaxError` | `case 1:` |
| Lupa wildcard | Tidak ada `case _` | Nilai tak dikenal tidak ditangani | Tambahkan `case _:` |
| Salah indentasi | `case` tidak sejajar `match` | `IndentationError` | Samakan indentasi `case` |
| Tipe data berbeda | input `"1"` dicocokkan dengan `case 1` | Tidak cocok | Ubah dengan `int()` |
| Guard salah urutan | Rentang besar diperiksa dulu | Hasil keliru | Periksa kondisi paling spesifik dulu |
| Mengira perlu `break` | Menulis `break` di case | `SyntaxError` | Hapus `break` |

### 10. Tips

- Gunakan `match-case` untuk menu dan kode kategori.
- Selalu sediakan `case _` agar input salah tetap ditangani.
- Samakan tipe data: `int` dengan `int`, `str` dengan `str`.
- Untuk rentang angka, gunakan guard atau `if-elif`.
- Uji setiap pilihan, termasuk pilihan yang tidak ada.

### 11. Contoh Implementasi

Beberapa contoh penerapan materi modul ini dalam kasus kecil.

**1. Menu sederhana dengan wildcard**

```python
pilihan = input("Pilihan (1/2/3): ")

match pilihan:
    case "1":
        print("Menampilkan profil")
    case "2":
        print("Mengubah password")
    case "3":
        print("Keluar")
    case _:
        print("Pilihan tidak tersedia")
```

Contoh interaksi:

```text
Pilihan (1/2/3): 2
Mengubah password
```

**2. Huruf vokal dengan OR pattern**

```python
huruf = input("Masukkan huruf: ").lower()

match huruf:
    case "a" | "i" | "u" | "e" | "o":
        print("Huruf vokal")
    case _:
        print("Bukan huruf vokal")
```

Contoh interaksi:

```text
Masukkan huruf: A
Huruf vokal
```

**3. Kategori umur dengan guard**

```python
umur = int(input("Umur: "))

match umur:
    case u if u < 0:
        print("Tidak valid")
    case u if u < 13:
        print("Anak")
    case u if u < 18:
        print("Remaja")
    case u if u < 60:
        print("Dewasa")
    case _:
        print("Lansia")
```

Contoh interaksi:

```text
Umur: 15
Remaja
```

---

## Tugas Praktikum

Simpan setiap tugas sebagai file terpisah, misalnya `tugas4_1.py`.

### Tugas 4.1 — Menu Sederhana

Buat menu dengan `match-case`:

```text
1. Lihat profil
2. Ubah password
3. Keluar
Pilihan:
```

Contoh interaksi:

```text
Pilihan: 2
Password berhasil diubah.
```

Jika pilihan tidak ada:

```text
Pilihan: 9
Pilihan tidak tersedia.
```

**Ketentuan:** gunakan `case _` untuk pilihan yang tidak dikenal.

### Tugas 4.2 — Nama Hari

Minta angka 1–7, lalu tampilkan nama hari.

Contoh interaksi:

```text
Masukkan angka hari: 3
Rabu
```

Jika angka di luar 1–7:

```text
Masukkan angka hari: 9
Hari tidak valid
```

**Ketentuan:** gunakan `match-case` dengan `case _`.

### Tugas 4.3 — Huruf Vokal

Minta satu huruf, lalu tentukan apakah huruf tersebut vokal atau konsonan.

Contoh interaksi:

```text
Masukkan huruf: a
a adalah huruf vokal.
```

```text
Masukkan huruf: k
k adalah huruf konsonan.
```

**Ketentuan:**

- Gunakan `lower()` agar huruf besar dan kecil dianggap sama.
- Gunakan OR pattern `|` untuk vokal.
- Jika input bukan satu huruf alfabet, tampilkan `Input bukan huruf.`

### Tugas 4.4 — Kalkulator Menu

Buat kalkulator dengan dua bilangan dan satu operator.

Contoh interaksi:

```text
Bilangan pertama: 10
Bilangan kedua: 4
Operator (+, -, *, /): *
Hasil: 40.0
```

```text
Bilangan pertama: 10
Bilangan kedua: 4
Operator (+, -, *, /): /
Hasil: 2.50
```

**Ketentuan:**

- Gunakan `match-case` untuk memilih operator.
- Tangani pembagian dengan nol.
- Tampilkan `Operator tidak valid` untuk operator lain.
- Tampilkan hasil pembagian dengan dua angka di belakang koma.

### Tugas 4.5 — Kategori Usia

Minta umur, lalu tampilkan kategori:

| Rentang umur | Kategori |
|---|---|
| < 0 | Tidak valid |
| 0–12 | Anak |
| 13–17 | Remaja |
| 18–59 | Dewasa |
| ≥ 60 | Lansia |

Contoh interaksi:

```text
Masukkan umur: 15
Kategori: Remaja
```

**Ketentuan:** gunakan `match-case` dengan guard `if`.

### Tugas 4.6 — Tantangan: ATM Satu Transaksi

Buat simulasi ATM dengan saldo awal `Rp500,000`. Tampilkan menu:

```text
1. Cek saldo
2. Tarik tunai
3. Setor tunai
4. Keluar
Pilihan:
```

Aturan:

- Pilihan 1 menampilkan saldo.
- Pilihan 2 meminta nominal penarikan. Nominal harus kelipatan Rp50,000 dan tidak boleh melebihi saldo.
- Pilihan 3 meminta nominal setoran. Nominal harus lebih dari 0.
- Pilihan 4 menampilkan `Terima kasih.`
- Pilihan lain menampilkan `Pilihan tidak valid.`

Contoh interaksi:

```text
Pilihan: 2
Nominal penarikan: 200000
Penarikan berhasil. Saldo: Rp300,000
```

```text
Pilihan: 2
Nominal penarikan: 125000
Nominal harus kelipatan Rp50,000.
```

**Ketentuan:**

- Gunakan `match-case` untuk menu.
- Gunakan `if-else` di dalam case untuk validasi.
- Tidak perlu membuat menu berulang; perulangan akan dipelajari di Modul 5 dan 6.

---

## Rangkuman

- `match-case` adalah padanan `switch-case` pada Python 3.10+.
- `case` memeriksa nilai tertentu; `case _` menangani nilai lain.
- Tanda `|` menggabungkan beberapa pola dalam satu case.
- Guard `if` menambahkan kondisi pada case.
- Python tidak memerlukan `break` di akhir case.
- Gunakan `if-elif` untuk rentang nilai yang lebih alami dibaca sebagai perbandingan.

## Istilah Penting

| Istilah | Arti |
|---|---|
| `match` | Nilai yang akan diperiksa |
| `case` | Kemungkinan pola yang dicocokkan |
| Wildcard | Pola `_` yang cocok dengan nilai apa pun |
| OR pattern | Beberapa pola digabung dengan `|` |
| Guard | Kondisi `if` tambahan pada case |
| Fallthrough | Perilaku menjalankan case berikutnya; tidak terjadi di Python |

## Checklist Sebelum Lanjut

- [ ] Saya dapat menulis `match-case` dengan benar.
- [ ] Saya dapat menggunakan `case _`.
- [ ] Saya dapat menggunakan OR pattern `|`.
- [ ] Saya dapat menggunakan guard `if` pada case.
- [ ] Saya dapat memilih antara `match-case` dan `if-elif`.
- [ ] Saya sudah mengerjakan seluruh tugas.

## Langkah Selanjutnya

Lanjutkan ke [Modul 5 — Perulangan `for`](modul-05-perulangan-for.md).
