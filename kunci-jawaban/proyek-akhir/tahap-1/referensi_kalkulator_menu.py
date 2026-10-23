while True:
    print("\n=== KALKULATOR MENU ===")
    print("1. Operasi aritmatika")
    print("2. Luas bangun")
    print("3. Konversi suhu")
    print("4. Tabel perkalian")
    print("5. Faktorial")
    print("6. Deret angka")
    print("0. Keluar")

    pilihan = input("Pilihan: ")

    match pilihan:
        case "1":
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
                    print("Operator tidak valid.")

        case "2":
            print("\n1. Persegi")
            print("2. Persegi panjang")
            print("3. Lingkaran")
            print("4. Segitiga")
            bangun = input("Pilihan bangun: ")

            match bangun:
                case "1":
                    sisi = float(input("Sisi: "))
                    print(f"Luas persegi: {sisi * sisi:.2f}")
                case "2":
                    panjang = float(input("Panjang: "))
                    lebar = float(input("Lebar: "))
                    print(f"Luas persegi panjang: {panjang * lebar:.2f}")
                case "3":
                    jari_jari = float(input("Jari-jari: "))
                    luas = 3.14159 * jari_jari * jari_jari
                    print(f"Luas lingkaran: {luas:.2f}")
                case "4":
                    alas = float(input("Alas: "))
                    tinggi = float(input("Tinggi: "))
                    print(f"Luas segitiga: {0.5 * alas * tinggi:.2f}")
                case _:
                    print("Pilihan bangun tidak valid.")

        case "3":
            print("\n1. Celsius ke Fahrenheit")
            print("2. Fahrenheit ke Celsius")
            print("3. Celsius ke Kelvin")
            konversi = input("Pilihan konversi: ")

            match konversi:
                case "1":
                    celsius = float(input("Suhu Celsius: "))
                    fahrenheit = (celsius * 9 / 5) + 32
                    print(f"Suhu Fahrenheit: {fahrenheit:.2f}")
                case "2":
                    fahrenheit = float(input("Suhu Fahrenheit: "))
                    celsius = (fahrenheit - 32) * 5 / 9
                    print(f"Suhu Celsius: {celsius:.2f}")
                case "3":
                    celsius = float(input("Suhu Celsius: "))
                    kelvin = celsius + 273.15
                    print(f"Suhu Kelvin: {kelvin:.2f}")
                case _:
                    print("Pilihan konversi tidak valid.")

        case "4":
            n = int(input("Masukkan n: "))

            if n < 0:
                print("n tidak boleh negatif.")
            else:
                for i in range(1, 11):
                    print(f"{n} x {i} = {n * i}")

        case "5":
            n = int(input("Masukkan n: "))

            if n < 0:
                print("n tidak boleh negatif.")
            else:
                faktorial = 1

                for i in range(1, n + 1):
                    faktorial *= i

                print(f"{n}! = {faktorial}")

        case "6":
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
                print("Jumlah:", total)
                print(f"Rata-rata: {total / n:.2f}")

        case "0":
            print("Terima kasih.")
            break

        case _:
            print("Pilihan tidak valid.")
