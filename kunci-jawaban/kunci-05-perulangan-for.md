# Kunci Jawaban Modul 5 — Perulangan `for`

## Tugas 5.1 — Deret Angka

```python
n = int(input("Masukkan n: "))

if n <= 0:
    print("n harus bilangan positif.")
else:
    total = 0

    print("Deret:", end=" ")
    for i in range(1, n + 1):
        print(i, end=" ")
        total += i
    print()

    rata_rata = total / n

    print("Jumlah:", total)
    print(f"Rata-rata: {rata_rata:.2f}")
```

Contoh output:

```text
Masukkan n: 5
Deret: 1 2 3 4 5
Jumlah: 15
Rata-rata: 3.00
```

## Tugas 5.2 — Faktorial

```python
n = int(input("Masukkan n: "))

if n < 1:
    print("n harus minimal 1.")
else:
    faktorial = 1
    proses = ""

    for i in range(1, n + 1):
        faktorial *= i

        if i == 1:
            proses = str(i)
        else:
            proses += " x " + str(i)

    print(f"{n}! = {faktorial}")
    print(proses + f" = {faktorial}")
```

Contoh output:

```text
Masukkan n: 5
5! = 120
1 x 2 x 3 x 4 x 5 = 120
```

**Penjelasan:** `faktorial *= i` sama dengan `faktorial = faktorial * i`. Variabel `proses` menyimpan urutan angka agar dapat ditampilkan.

## Tugas 5.3 — Tabel Perkalian

```python
n = int(input("Masukkan n: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

Contoh output:

```text
Masukkan n: 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30
```

## Tugas 5.4 — Bilangan Prima

```python
n = int(input("Masukkan bilangan: "))

if n < 2:
    prima = False
else:
    prima = True
    for pembagi in range(2, n):
        if n % pembagi == 0:
            prima = False
            break

if prima:
    print(f"{n} adalah bilangan prima.")
else:
    print(f"{n} bukan bilangan prima.")
```

Contoh output:

```text
Masukkan bilangan: 29
29 adalah bilangan prima.
```

```text
Masukkan bilangan: 30
30 bukan bilangan prima.
```

**Penjelasan:** bilangan prima hanya habis dibagi 1 dan dirinya sendiri. Loop memeriksa pembagi dari 2 sampai `n - 1`. Jika ditemukan pembagi, `prima` menjadi `False` dan loop dihentikan dengan `break`.

## Tugas 5.5 — Pola Bintang

```python
tinggi = int(input("Masukkan tinggi: "))

for i in range(1, tinggi + 1):
    print("*" * i)

for i in range(tinggi, 0, -1):
    print("*" * i)
```

Contoh output untuk tinggi 5:

```text
*
**
***
****
*****
*****
****
***
**
*
```

**Penjelasan:** loop pertama mencetak dari 1 hingga `tinggi`. Loop kedua mencetak dari `tinggi` turun ke 1.

## Tugas 5.6 — Deret Fibonacci

```python
n = int(input("Masukkan n: "))

if n < 1:
    print("n harus minimal 1.")
else:
    a = 0
    b = 1
    total = 0

    print("Deret:", end=" ")
    for i in range(n):
        print(a, end=" ")
        total += a

        berikutnya = a + b
        a = b
        b = berikutnya

    print()
    print("Jumlah:", total)
```

Contoh output:

```text
Masukkan n: 7
Deret: 0 1 1 2 3 5 8
Jumlah: 20
```

**Penjelasan:**

- `a` dan `b` menyimpan dua angka Fibonacci terakhir.
- Setiap putaran mencetak `a`, menambahkannya ke `total`, lalu menghitung angka berikutnya.
- `berikutnya = a + b`, lalu `a = b` dan `b = berikutnya` memindahkan deret satu langkah.
- `end=" "` membuat angka tercetak dalam satu baris.
