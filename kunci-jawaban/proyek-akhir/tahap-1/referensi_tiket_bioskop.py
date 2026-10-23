total_pendapatan = 0

while True:
    print("\n=== TIKET BIOSKOP ===")
    print("1. Pesan tiket")
    print("2. Lihat total pendapatan")
    print("0. Keluar")

    pilihan = input("Pilihan: ")

    match pilihan:
        case "1":
            print("\nDaftar film:")
            print("A. Petualangan Angka - Rp35,000")
            print("B. Logika Malam - Rp45,000")
            print("C. Kode Rahasia - Rp55,000")

            kode = input("Pilih film (A/B/C): ").upper()

            match kode:
                case "A":
                    judul = "Petualangan Angka"
                    harga = 35000
                case "B":
                    judul = "Logika Malam"
                    harga = 45000
                case "C":
                    judul = "Kode Rahasia"
                    harga = 55000
                case _:
                    print("Kode film tidak valid.")
                    continue

            jumlah = int(input("Jumlah tiket (1-10): "))

            if jumlah < 1 or jumlah > 10:
                print("Jumlah tiket harus antara 1 dan 10.")
                continue

            total = 0

            for i in range(1, jumlah + 1):
                umur = int(input(f"Umur penonton {i}: "))

                while umur < 0 or umur > 120:
                    print("Usia harus antara 0 dan 120.")
                    umur = int(input(f"Umur penonton {i}: "))

                if umur < 13:
                    kategori = "Anak"
                    harga_tiket = harga * 0.70
                elif umur >= 60:
                    kategori = "Senior"
                    harga_tiket = harga * 0.80
                else:
                    kategori = "Dewasa"
                    harga_tiket = harga

                total += harga_tiket
                print(f"Tiket {i}: {kategori} - Rp{harga_tiket:,.0f}")

            print(f"\nTotal sebelum diskon: Rp{total:,.0f}")

            member = input("Member (y/n): ").lower()

            while member != "y" and member != "n":
                print("Masukkan y atau n.")
                member = input("Member (y/n): ").lower()

            if member == "y":
                diskon = total * 0.10
            else:
                diskon = 0

            total_bayar = total - diskon

            print(f"Diskon member 10%: Rp{diskon:,.0f}")
            print(f"Total bayar: Rp{total_bayar:,.0f}")

            bayar = float(input("Bayar: "))

            while bayar < total_bayar:
                print(f"Pembayaran kurang. Total: Rp{total_bayar:,.0f}")
                bayar = float(input("Bayar: "))

            kembalian = bayar - total_bayar
            total_pendapatan += total_bayar

            print("\nRingkasan:")
            print(f"Film: {judul}")
            print(f"Jumlah tiket: {jumlah}")
            print(f"Total sebelum diskon: Rp{total:,.0f}")
            print(f"Diskon member: Rp{diskon:,.0f}")
            print(f"Total bayar: Rp{total_bayar:,.0f}")
            print(f"Bayar: Rp{bayar:,.0f}")
            print(f"Kembalian: Rp{kembalian:,.0f}")

        case "2":
            print(f"Total pendapatan: Rp{total_pendapatan:,.0f}")

        case "0":
            print("Terima kasih.")
            break

        case _:
            print("Pilihan tidak valid.")
