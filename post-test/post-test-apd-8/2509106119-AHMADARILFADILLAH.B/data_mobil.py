import os
from prettytable import PrettyTable

mobil_list = {
    "KT1234AA": {"nama": "Toyota Alphard", "harga": 1500000, "status": "Tersedia"},
    "DA5678BB": {"nama": "BMW i8", "harga": 2500000, "status": "Tersedia"},
    "KH8765CC": {"nama": "Mercedes Benz S-Class", "harga": 2800000, "status": "Tersedia"},
    "KB4321DD": {"nama": "Range Rover Evoque", "harga": 2000000, "status": "Tersedia"},
    "KU9999EE": {"nama": "Porsche Cayenne", "harga": 3000000, "status": "Tersedia"}
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def lihat_mobil():
    clear()
    print("=== DAFTAR MOBIL ===\n")
    table = PrettyTable()
    table.field_names = ["Plat", "Nama Mobil", "Harga Sewa (Rp)", "Status"]
    for plat, data in mobil_list.items():
        table.add_row([plat, data["nama"], f"{data['harga']:,}", data["status"]])
    print(table)
    input("\nTekan Enter untuk kembali...")


def tambah_mobil():
    clear()
    print("=== TAMBAH MOBIL BARU ===")
    plat = input("Plat mobil (misal KT8888XX): ").upper().strip()
    if plat in mobil_list:
        print("Plat sudah terdaftar!")
    else:
        nama = input("Nama mobil: ").strip()
        harga = input("Harga sewa per hari: ").strip()
        if not harga.isdigit():
            print("Harga harus berupa angka!")
        else:
            mobil_list[plat] = {"nama": nama, "harga": int(harga), "status": "Tersedia"}
            print("Mobil berhasil ditambahkan!")
    input("Tekan Enter untuk kembali...")


def update_mobil():
    clear()
    print("=== UPDATE DATA MOBIL ===")
    lihat_mobil()
    plat_update = input("\nMasukkan plat mobil yang ingin diupdate: ").upper().strip()

    if plat_update not in mobil_list:
        print("Plat tidak ditemukan!")
    else:
        nama_baru = input("Nama baru (kosong = tidak ubah): ").strip()
        harga_baru = input("Harga baru (kosong = tidak ubah): ").strip()
        status_baru = input("Status baru (Tersedia/Disewa): ").strip()

        if nama_baru:
            mobil_list[plat_update]["nama"] = nama_baru
        if harga_baru and harga_baru.isdigit():
            mobil_list[plat_update]["harga"] = int(harga_baru)
        if status_baru in ["Tersedia", "Disewa"]:
            mobil_list[plat_update]["status"] = status_baru

        print("Data mobil berhasil diperbarui!")
    input("Tekan Enter untuk kembali...")


def hapus_mobil():
    clear()
    print("=== HAPUS MOBIL ===")
    lihat_mobil()
    plat_hapus = input("\nMasukkan plat mobil yang ingin dihapus: ").upper().strip()
    if plat_hapus in mobil_list:
        konfirmasi = input(f"Yakin ingin menghapus {plat_hapus}? (y/n): ").lower()
        if konfirmasi == "y":
            del mobil_list[plat_hapus]
            print("Mobil berhasil dihapus!")
        else:
            print("Dibatalkan.")
    else:
        print("Plat tidak ditemukan!")
    input("Tekan Enter untuk kembali...")
