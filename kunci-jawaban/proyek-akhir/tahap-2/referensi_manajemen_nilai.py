def hitung_nilai_akhir(tugas, uts, uas):
    return 0.3 * tugas + 0.3 * uts + 0.4 * uas


def konversi_huruf(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 75:
        return "B"
    elif nilai >= 65:
        return "C"
    elif nilai >= 55:
        return "D"
    else:
        return "E"


def input_angka(prompt, minimum=0.0, maksimum=100.0):
    while True:
        try:
            nilai = float(input(prompt))
        except ValueError:
            print("Masukkan angka yang valid.")
            continue

        if minimum <= nilai <= maksimum:
            return nilai

        print(f"Nilai harus berada antara {minimum:.0f} dan {maksimum:.0f}.")


def cari_indeks(data, nim):
    for i, mahasiswa in enumerate(data):
        if mahasiswa["nim"] == nim:
            return i
    return -1


def tampilkan_menu():
    print("\n=== MANAJEMEN NILAI MAHASISWA ===")
    print("1. Tambah mahasiswa")
    print("2. Tampilkan semua mahasiswa")
    print("3. Cari mahasiswa")
    print("4. Ubah data mahasiswa")
    print("5. Hapus mahasiswa")
    print("6. Statistik")
    print("0. Keluar")


def tampilkan_satu(mahasiswa):
    akhir = hitung_nilai_akhir(
        mahasiswa["tugas"],
        mahasiswa["uts"],
        mahasiswa["uas"]
    )
    print(f"NIM        : {mahasiswa['nim']}")
    print(f"Nama       : {mahasiswa['nama']}")
    print(f"Nilai tugas: {mahasiswa['tugas']:.2f}")
    print(f"Nilai UTS  : {mahasiswa['uts']:.2f}")
    print(f"Nilai UAS  : {mahasiswa['uas']:.2f}")
    print(f"Nilai akhir: {akhir:.2f}")
    print(f"Huruf      : {konversi_huruf(akhir)}")


def tampilkan_semua(data):
    if not data:
        print("Belum ada data mahasiswa.")
        return

    print(
        f"{'NIM':<10} {'Nama':<15} {'Tugas':>7} "
        f"{'UTS':>7} {'UAS':>7} {'Akhir':>8} {'Huruf':>6}"
    )
    print("-" * 66)

    for mahasiswa in data:
        akhir = hitung_nilai_akhir(
            mahasiswa["tugas"],
            mahasiswa["uts"],
            mahasiswa["uas"]
        )
        print(
            f"{mahasiswa['nim']:<10} {mahasiswa['nama']:<15} "
            f"{mahasiswa['tugas']:>7.2f} {mahasiswa['uts']:>7.2f} "
            f"{mahasiswa['uas']:>7.2f} {akhir:>8.2f} "
            f"{konversi_huruf(akhir):>6}"
        )


def tambah_mahasiswa(data):
    nim = input("NIM: ").strip()

    if not nim:
        print("NIM tidak boleh kosong.")
        return

    if cari_indeks(data, nim) != -1:
        print("NIM sudah terdaftar.")
        return

    nama = input("Nama: ").strip()

    if not nama:
        print("Nama tidak boleh kosong.")
        return

    tugas = input_angka("Nilai tugas: ")
    uts = input_angka("Nilai UTS: ")
    uas = input_angka("Nilai UAS: ")

    data.append({
        "nim": nim,
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas
    })
    print(f"Data {nama} berhasil ditambahkan.")


def cari_mahasiswa(data):
    nim = input("NIM yang dicari: ").strip()
    indeks = cari_indeks(data, nim)

    if indeks == -1:
        print("Mahasiswa tidak ditemukan.")
    else:
        tampilkan_satu(data[indeks])


def ubah_mahasiswa(data):
    nim = input("NIM yang akan diubah: ").strip()
    indeks = cari_indeks(data, nim)

    if indeks == -1:
        print("Mahasiswa tidak ditemukan.")
        return

    mahasiswa = data[indeks]
    nama = input(f"Nama [{mahasiswa['nama']}]: ").strip()

    if nama:
        mahasiswa["nama"] = nama

    mahasiswa["tugas"] = input_angka(f"Nilai tugas [{mahasiswa['tugas']:.2f}]: ")
    mahasiswa["uts"] = input_angka(f"Nilai UTS [{mahasiswa['uts']:.2f}]: ")
    mahasiswa["uas"] = input_angka(f"Nilai UAS [{mahasiswa['uas']:.2f}]: ")
    print("Data berhasil diperbarui.")


def hapus_mahasiswa(data):
    nim = input("NIM yang akan dihapus: ").strip()
    indeks = cari_indeks(data, nim)

    if indeks == -1:
        print("Mahasiswa tidak ditemukan.")
        return

    mahasiswa = data[indeks]
    konfirmasi = input(f"Hapus data {mahasiswa['nama']}? (y/n): ").strip().lower()

    if konfirmasi == "y":
        del data[indeks]
        print("Data berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")


def tampilkan_statistik(data):
    if not data:
        print("Belum ada data mahasiswa.")
        return

    jumlah = len(data)
    total_akhir = 0
    jumlah_lulus = 0
    tertinggi = data[0]
    terendah = data[0]
    nilai_tertinggi = hitung_nilai_akhir(
        tertinggi["tugas"],
        tertinggi["uts"],
        tertinggi["uas"]
    )
    nilai_terendah = nilai_tertinggi

    for mahasiswa in data:
        akhir = hitung_nilai_akhir(
            mahasiswa["tugas"],
            mahasiswa["uts"],
            mahasiswa["uas"]
        )
        total_akhir += akhir

        if akhir >= 60:
            jumlah_lulus += 1

        if akhir > nilai_tertinggi:
            nilai_tertinggi = akhir
            tertinggi = mahasiswa

        if akhir < nilai_terendah:
            nilai_terendah = akhir
            terendah = mahasiswa

    rata_rata = total_akhir / jumlah

    print(f"Jumlah mahasiswa: {jumlah}")
    print(f"Rata-rata nilai akhir: {rata_rata:.2f}")
    print(f"Nilai tertinggi: {tertinggi['nama']} ({nilai_tertinggi:.2f})")
    print(f"Nilai terendah: {terendah['nama']} ({nilai_terendah:.2f})")
    print(f"Jumlah lulus: {jumlah_lulus}")


def main():
    data = []

    while True:
        tampilkan_menu()
        pilihan = input("Pilihan: ").strip()

        if pilihan == "1":
            tambah_mahasiswa(data)
        elif pilihan == "2":
            tampilkan_semua(data)
        elif pilihan == "3":
            cari_mahasiswa(data)
        elif pilihan == "4":
            ubah_mahasiswa(data)
        elif pilihan == "5":
            hapus_mahasiswa(data)
        elif pilihan == "6":
            tampilkan_statistik(data)
        elif pilihan == "0":
            print("Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
