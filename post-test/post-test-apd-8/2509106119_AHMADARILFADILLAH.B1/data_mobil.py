import json, os
from prettytable import PrettyTable

MOBIL_FILE = "mobil.json"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_mobil():
    if os.path.exists(MOBIL_FILE):
        with open(MOBIL_FILE, "r") as f:
            return json.load(f)
    else:
        mobil_list = {
            "KT1234AA": {"nama": "Toyota Alphard", "harga": 1500000, "status": "Tersedia"},
            "DA5678BB": {"nama": "BMW i8", "harga": 2500000, "status": "Tersedia"},
        }
        with open(MOBIL_FILE, "w") as f:
            json.dump(mobil_list, f, indent=4)
        return mobil_list

def save_mobil(mobil_list):
    with open(MOBIL_FILE, "w") as f:
        json.dump(mobil_list, f, indent=4)

def lihat_mobil():
    clear()
    mobil_list = load_mobil()
    tabel = PrettyTable(["Plat", "Nama Mobil", "Harga (Rp)", "Status"])
    for plat, data in mobil_list.items():
        tabel.add_row([plat, data["nama"], f"{data['harga']:,}", data["status"]])
    print(tabel)
    input("Tekan Enter...")

def tambah_mobil():
    clear()
    mobil_list = load_mobil()
    plat = input("Masukkan plat nomor mobil: ").upper()
    if plat in mobil_list:
        print("Plat nomor sudah terdaftar!")
    else:
        nama = input("Masukkan nama mobil: ")
        harga = int(input("Masukkan harga sewa per hari: "))
        mobil_list[plat] = {"nama": nama, "harga": harga, "status": "Tersedia"}
        save_mobil(mobil_list)
        print("Mobil berhasil ditambahkan!")
    input("Tekan Enter...")

def update_mobil():
    clear()
    mobil_list = load_mobil()
    plat = input("Masukkan plat nomor mobil yang ingin diupdate: ").upper()
    if plat in mobil_list:
        nama = input(f"Nama baru ({mobil_list[plat]['nama']}): ") or mobil_list[plat]['nama']
        harga_baru = input(f"Harga baru ({mobil_list[plat]['harga']}): ")
        if harga_baru and harga_baru.isdigit():
            harga_baru = int(harga_baru)
        else:
            harga_baru = mobil_list[plat]['harga']
        mobil_list[plat] = {"nama": nama, "harga": harga_baru, "status": mobil_list[plat]['status']}
        save_mobil(mobil_list)
        print("Data mobil berhasil diperbarui!")
    else:
        print("Plat tidak ditemukan!")
    input("Tekan Enter...")

def hapus_mobil():
    clear()
    mobil_list = load_mobil()
    plat = input("Masukkan plat nomor mobil yang ingin dihapus: ").upper()
    if plat in mobil_list:
        konfirmasi = input(f"Yakin ingin menghapus {plat}? (y/n): ").lower()
        if konfirmasi == "y":
            del mobil_list[plat]
            save_mobil(mobil_list)
            print("Mobil berhasil dihapus!")
        else:
            print("Dibatalkan.")
    else:
        print("Plat tidak ditemukan!")
    input("Tekan Enter...")

