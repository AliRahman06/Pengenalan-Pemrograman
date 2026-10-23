# Kunci Jawaban Modul 4 — Switch Case dengan `match-case`

## Tugas 4.1 — Menu Sederhana

```python
pilihan = input("Pilihan: ")

match pilihan:
    case "1":
        print("Menampilkan profil pengguna.")
    case "2":
        print("Password berhasil diubah.")
    case "3":
        print("Keluar dari program.")
    case _:
        print("Pilihan tidak tersedia.")
```

Contoh output:

```text
Pilihan: 2
Password berhasil diubah.
```

```text
Pilihan: 9
Pilihan tidak tersedia.
```

**Penjelasan:** `case _` menangani semua pilihan selain `"1"`, `"2"`, dan `"3"`.

## Tugas 4.2 — Nama Hari

```python
hari = int(input("Masukkan angka hari: "))

match hari:
    case 1:
        print("Senin")
    case 2:
        print("Selasa")
    case 3:
        print("Rabu")
    case 4:
        print("Kamis")
    case 5:
        print("Jumat")
    case 6:
        print("Sabtu")
    case 7:
        print("Minggu")
    case _:
        print("Hari tidak valid")
```

Contoh output:

```text
Masukkan angka hari: 3
Rabu
```

```text
Masukkan angka hari: 9
Hari tidak valid
```

**Penjelasan:** input diubah dengan `int()` agar cocok dengan pola angka pada `case`.

## Tugas 4.3 — Huruf Vokal

```python
huruf = input("Masukkan huruf: ").lower()

match huruf:
    case "a" | "i" | "u" | "e" | "o":
        print(f"{huruf} adalah huruf vokal.")
    case _:
        if len(huruf) == 1 and huruf.isalpha():
            print(f"{huruf} adalah huruf konsonan.")
        else:
            print("Input bukan huruf.")
```

Contoh output:

```text
Masukkan huruf: a
a adalah huruf vokal.
```

```text
Masukkan huruf: k
k adalah huruf konsonan.
```

**Penjelasan:** `lower()` menyeragamkan huruf besar dan kecil. `len(huruf) == 1 and huruf.isalpha()` memastikan input benar-benar satu huruf alfabet.

## Tugas 4.4 — Kalkulator Menu

```python
angka1 = float(input("Bilangan pertama: "))
angka2 = float(input("Bilangan kedua: "))
operator = input("Operator (+, -, *, /): ")

match operator:
    case "+":
        print(f"Hasil: {angka1 + angka2}")
    case "-":
        print(f"Hasil: {angka1 - angka2}")
    case "*":
        print(f"Hasil: {angka1 * angka2}")
    case "/":
        if angka2 == 0:
            print("Pembagian dengan nol tidak diperbolehkan.")
        else:
            print(f"Hasil: {angka1 / angka2:.2f}")
    case _:
        print("Operator tidak valid")
```

Contoh output:

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

**Penjelasan:** `case _` menangani operator di luar `+`, `-`, `*`, dan `/`. Pemeriksaan pembagi nol dilakukan sebelum pembagian.

## Tugas 4.5 — Kategori Usia

```python
umur = int(input("Masukkan umur: "))

match umur:
    case u if u < 0:
        print("Kategori: Tidak valid")
    case u if u < 13:
        print("Kategori: Anak")
    case u if u < 18:
        print("Kategori: Remaja")
    case u if u < 60:
        print("Kategori: Dewasa")
    case _:
        print("Kategori: Lansia")
```

Contoh output:

```text
Masukkan umur: 15
Kategori: Remaja
```

**Penjelasan:** guard diperiksa berurutan. Jika `u < 0` tidak terpenuhi, Python memeriksa `u < 13`, lalu `u < 18`, dan seterusnya. Karena itu, urutan dari rentang terkecil ke terbesar penting.

## Tugas 4.6 — ATM Satu Transaksi

```python
saldo = 500000
pilihan = input("Pilihan: ")

match pilihan:
    case "1":
        print(f"Saldo: Rp{saldo:,.0f}")
    case "2":
        nominal = int(input("Nominal penarikan: "))

        if nominal <= 0:
            print("Nominal harus lebih dari 0.")
        elif nominal % 50000 != 0:
            print("Nominal harus kelipatan Rp50,000.")
        elif nominal > saldo:
            print("Saldo tidak mencukupi.")
        else:
            saldo -= nominal
            print(f"Penarikan berhasil. Saldo: Rp{saldo:,.0f}")
    case "3":
        nominal = int(input("Nominal setoran: "))

        if nominal <= 0:
            print("Nominal harus lebih dari 0.")
        else:
            saldo += nominal
            print(f"Setoran berhasil. Saldo: Rp{saldo:,.0f}")
    case "4":
        print("Terima kasih.")
    case _:
        print("Pilihan tidak valid.")
```

Contoh output:

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

**Penjelasan:**

- `nominal % 50000 != 0` mendeteksi nominal yang bukan kelipatan Rp50,000.
- `nominal > saldo` mencegah saldo menjadi negatif.
- Setelah penarikan atau setoran, program menampilkan saldo terbaru.
- Menu belum berulang karena `while` baru dipelajari pada Modul 6.
