# Kunci Jawaban Modul 6 — Perulangan `while`

## Tugas 6.1 — Hitung Mundur

```python
n = int(input("Masukkan n: "))

if n <= 0:
    print("n harus bilangan positif.")
else:
    while n >= 1:
        print(n)
        n -= 1

    print("Selesai!")
```

Contoh output:

```text
Masukkan n: 5
5
4
3
2
1
Selesai!
```

**Penjelasan:** `n -= 1` membuat nilai `n` menurun setiap putaran, sehingga kondisi `n >= 1` akhirnya menjadi `False`.

## Tugas 6.2 — Jumlahkan Angka sampai 0

```python
total = 0
banyak_angka = 0

angka = int(input("Masukkan angka (0 untuk selesai): "))

while angka != 0:
    total += angka
    banyak_angka += 1
    angka = int(input("Masukkan angka (0 untuk selesai): "))

if banyak_angka == 0:
    print("Tidak ada data.")
else:
    rata_rata = total / banyak_angka
    print(f"Total: {total}")
    print(f"Banyak angka: {banyak_angka}")
    print(f"Rata-rata: {rata_rata:.2f}")
```

Contoh output:

```text
Masukkan angka (0 untuk selesai): 10
Masukkan angka (0 untuk selesai): 20
Masukkan angka (0 untuk selesai): 30
Masukkan angka (0 untuk selesai): 0
Total: 60
Banyak angka: 3
Rata-rata: 20.00
```

**Penjelasan:** `0` adalah sentinel. Karena kondisi diperiksa sebelum isi loop, angka `0` tidak ikut dijumlahkan.

## Tugas 6.3 — Validasi Nilai

```python
percobaan = 1
nilai = int(input(f"Percobaan {percobaan}: "))

while nilai < 0 or nilai > 100:
    print("Nilai tidak valid.")
    percobaan += 1
    nilai = int(input(f"Percobaan {percobaan}: "))

print(f"Nilai {nilai} disimpan setelah {percobaan} percobaan.")
```

Contoh output:

```text
Percobaan 1: 120
Nilai tidak valid.
Percobaan 2: -5
Nilai tidak valid.
Percobaan 3: 80
Nilai 80 disimpan setelah 3 percobaan.
```

**Penjelasan:** input baru diminta di dalam loop. Tanpa input ulang, nilai tidak pernah berubah dan loop berjalan terus.

## Tugas 6.4 — Tebak Angka

```python
angka_rahasia = 42
percobaan = 0
maksimal = 5

while percobaan < maksimal:
    percobaan += 1
    tebakan = int(input(f"Percobaan {percobaan}: "))

    if tebakan == angka_rahasia:
        print("Selamat, tebakan Anda benar!")
        break
    elif tebakan < angka_rahasia:
        print("Terlalu kecil.")
    else:
        print("Terlalu besar.")
else:
    print(f"Percobaan habis. Angka rahasianya {angka_rahasia}.")
```

Contoh output:

```text
Percobaan 1: 20
Terlalu kecil.
Percobaan 2: 60
Terlalu besar.
Percobaan 3: 42
Selamat, tebakan Anda benar!
```

**Penjelasan:** `while ... else` menjalankan blok `else` hanya jika loop selesai tanpa `break`. Jika pemain berhasil menebak, pesan "Percobaan habis" tidak muncul.

## Tugas 6.5 — Simpan Uang sampai Target

```python
target = float(input("Target tabungan: "))

if target <= 0:
    print("Target harus lebih dari 0.")
else:
    total = 0

    while total < target:
        setoran = float(input("Setoran: "))

        if setoran <= 0:
            print("Setoran harus lebih dari 0.")
            continue

        total += setoran

        if total >= target:
            print(f"Target tercapai. Total tabungan: Rp{total:,.0f}")
        else:
            print(f"Total sementara: Rp{total:,.0f}")
```

Contoh output:

```text
Target tabungan: 100000
Setoran: 30000
Total sementara: Rp30,000
Setoran: 50000
Total sementara: Rp80,000
Setoran: 25000
Target tercapai. Total tabungan: Rp105,000
```

**Penjelasan:** `continue` melewati setoran yang tidak valid tanpa menambah total. Loop berhenti ketika `total >= target`.

## Tugas 6.6 — Menu Kalkulator Berulang

```python
while True:
    print("\n=== KALKULATOR ===")
    print("1. Tambah")
    print("2. Kurang")
    print("3. Kali")
    print("4. Bagi")
    print("0. Keluar")

    pilihan = input("Pilihan: ")

    match pilihan:
        case "1":
            angka1 = float(input("Bilangan pertama: "))
            angka2 = float(input("Bilangan kedua: "))
            print(f"Hasil: {angka1 + angka2}")
        case "2":
            angka1 = float(input("Bilangan pertama: "))
            angka2 = float(input("Bilangan kedua: "))
            print(f"Hasil: {angka1 - angka2}")
        case "3":
            angka1 = float(input("Bilangan pertama: "))
            angka2 = float(input("Bilangan kedua: "))
            print(f"Hasil: {angka1 * angka2}")
        case "4":
            angka1 = float(input("Bilangan pertama: "))
            angka2 = float(input("Bilangan kedua: "))

            if angka2 == 0:
                print("Pembagian dengan nol tidak diperbolehkan.")
            else:
                print(f"Hasil: {angka1 / angka2}")
        case "0":
            print("Terima kasih.")
            break
        case _:
            print("Pilihan tidak valid.")
```

Contoh output:

```text
Pilihan: 1
Bilangan pertama: 10
Bilangan kedua: 5
Hasil: 15.0

Pilihan: 4
Bilangan pertama: 10
Bilangan kedua: 0
Pembagian dengan nol tidak diperbolehkan.

Pilihan: 0
Terima kasih.
```

**Penjelasan:**

- `while True` membuat menu tampil terus.
- `break` pada pilihan `0` adalah satu-satunya jalan keluar.
- `match-case` memilih operasi berdasarkan input.
- Pemeriksaan pembagi nol dilakukan sebelum pembagian.
