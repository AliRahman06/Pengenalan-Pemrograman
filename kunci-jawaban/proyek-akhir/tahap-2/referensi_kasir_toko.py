def tampilkan_menu():
    print("\n=== KASIR TOKO ===")
    print("1. Lihat produk")
    print("2. Transaksi baru")
    print("0. Keluar")


def tampilkan_produk(produk):
    print(f"{'Kode':<6} {'Nama':<15} {'Harga':>12} {'Stok':>6}")
    print("-" * 43)

    for item in produk:
        harga = "Rp" + format(item["harga"], ",.0f")
        print(
            f"{item['kode']:<6} {item['nama']:<15} "
            f"{harga:>12} {item['stok']:>6}"
        )


def cari_produk(produk, kode):
    for item in produk:
        if item["kode"].casefold() == kode.casefold():
            return item
    return None


def input_jumlah(prompt):
    while True:
        try:
            jumlah = int(input(prompt))
        except ValueError:
            print("Masukkan bilangan bulat.")
            continue

        if jumlah > 0:
            return jumlah

        print("Jumlah harus lebih dari 0.")


def input_uang(prompt):
    while True:
        try:
            uang = float(input(prompt))
        except ValueError:
            print("Masukkan angka yang valid.")
            continue

        if uang >= 0:
            return uang

        print("Nominal tidak boleh negatif.")


def hitung_subtotal(keranjang):
    total = 0

    for entry in keranjang:
        total += entry["produk"]["harga"] * entry["jumlah"]

    return total


def hitung_diskon(subtotal):
    if subtotal >= 200000:
        return 0.15
    elif subtotal >= 100000:
        return 0.10
    elif subtotal >= 50000:
        return 0.05
    else:
        return 0.0


def hitung_total(subtotal, diskon_persen):
    diskon = subtotal * diskon_persen
    pajak = (subtotal - diskon) * 0.11
    total = subtotal - diskon + pajak
    return diskon, pajak, total


def cetak_struk(
    keranjang,
    subtotal,
    diskon_persen,
    diskon,
    pajak,
    total,
    bayar,
    kembalian
):
    print("=" * 30)
    print("STRUK PEMBELIAN")
    print("=" * 30)

    for entry in keranjang:
        produk = entry["produk"]
        jumlah = entry["jumlah"]
        baris_total = produk["harga"] * jumlah
        print(produk["nama"])
        print(
            f"  {jumlah} x Rp{produk['harga']:,.0f} "
            f"= Rp{baris_total:,.0f}"
        )

    label_diskon = f"Diskon {diskon_persen * 100:.0f}%"

    print("-" * 30)
    print(f"{'Subtotal':<14}: Rp{subtotal:,.0f}")
    print(f"{label_diskon:<14}: Rp{diskon:,.0f}")
    print(f"{'Pajak 11%':<14}: Rp{pajak:,.0f}")
    print(f"{'Total':<14}: Rp{total:,.0f}")
    print(f"{'Bayar':<14}: Rp{bayar:,.0f}")
    print(f"{'Kembalian':<14}: Rp{kembalian:,.0f}")
    print("=" * 30)
    print("Terima kasih.")


def transaksi(produk):
    keranjang = []

    while True:
        kode = input("Kode produk (kosong untuk selesai): ").strip()

        if not kode:
            break

        item = cari_produk(produk, kode)

        if item is None:
            print("Produk tidak ditemukan.")
            continue

        jumlah = input_jumlah("Jumlah: ")
        jumlah_di_keranjang = 0

        for entry in keranjang:
            if entry["produk"]["kode"] == item["kode"]:
                jumlah_di_keranjang += entry["jumlah"]

        if jumlah_di_keranjang + jumlah > item["stok"]:
            print(
                f"Stok tidak mencukupi. Stok tersedia: {item['stok']}, "
                f"sudah di keranjang: {jumlah_di_keranjang}."
            )
            continue

        keranjang.append({"produk": item, "jumlah": jumlah})
        print(f"{item['nama']} x{jumlah} ditambahkan.")

    if not keranjang:
        print("Transaksi dibatalkan: keranjang kosong.")
        return

    subtotal = hitung_subtotal(keranjang)
    diskon_persen = hitung_diskon(subtotal)
    diskon, pajak, total = hitung_total(subtotal, diskon_persen)

    print(f"Subtotal: Rp{subtotal:,.0f}")
    print(f"Diskon {diskon_persen * 100:.0f}%: Rp{diskon:,.0f}")
    print(f"Pajak 11%: Rp{pajak:,.0f}")
    print(f"Total: Rp{total:,.0f}")

    bayar = input_uang("Bayar: ")

    while bayar < total:
        print(f"Pembayaran kurang. Total yang harus dibayar: Rp{total:,.0f}.")
        bayar = input_uang("Bayar: ")

    kembalian = bayar - total

    for entry in keranjang:
        entry["produk"]["stok"] -= entry["jumlah"]

    cetak_struk(
        keranjang,
        subtotal,
        diskon_persen,
        diskon,
        pajak,
        total,
        bayar,
        kembalian
    )


def main():
    produk = [
        {"kode": "P001", "nama": "Pena", "harga": 3000, "stok": 10},
        {"kode": "P002", "nama": "Buku", "harga": 5000, "stok": 5},
        {"kode": "P003", "nama": "Penggaris", "harga": 4000, "stok": 8}
    ]

    while True:
        tampilkan_menu()
        pilihan = input("Pilihan: ").strip()

        if pilihan == "1":
            tampilkan_produk(produk)
        elif pilihan == "2":
            transaksi(produk)
        elif pilihan == "0":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
