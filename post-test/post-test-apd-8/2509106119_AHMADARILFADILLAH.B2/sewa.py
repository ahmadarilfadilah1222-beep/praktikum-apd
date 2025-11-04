import os
from prettytable import PrettyTable
from data_mobil import mobil_list, clear, lihat_mobil

def sewa_mobil(username):
    clear()
    print("=== SEWA MOBIL ===\n")
    table = PrettyTable()
    table.field_names = ["Plat", "Nama Mobil", "Harga (Rp)", "Status"]
    for plat, data in mobil_list.items():
        table.add_row([plat, data["nama"], f"{data['harga']:,}", data["status"]])
    print(table)

    # Cegah user menyewa lebih dari satu
    for data in mobil_list.values():
        if data["status"] == f"Disewa oleh {username}":
            print("\nAnda sudah menyewa mobil! Kembalikan dulu sebelum menyewa lagi.")
            input("Tekan Enter...")
            return

    plat_sewa = input("\nMasukkan plat mobil yang ingin disewa: ").upper().strip()
    if plat_sewa in mobil_list:
        if mobil_list[plat_sewa]["status"] == "Tersedia":
            mobil_list[plat_sewa]["status"] = f"Disewa oleh {username}"
            print(f"Mobil {mobil_list[plat_sewa]['nama']} berhasil disewa!")
        else:
            print("Mobil sedang disewa!")
    else:
        print("Plat tidak ditemukan!")
    input("Tekan Enter...")


def kembalikan_mobil(username):
    clear()
    ditemukan = False
    for data in mobil_list.values():
        if data["status"] == f"Disewa oleh {username}":
            data["status"] = "Tersedia"
            print(f"Mobil {data['nama']} telah dikembalikan.")
            ditemukan = True
    if not ditemukan:
        print("Anda belum menyewa mobil.")
    input("Tekan Enter...")

