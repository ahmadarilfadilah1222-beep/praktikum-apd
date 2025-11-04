import os
from autentikasi import login, register
from data_mobil import clear, lihat_mobil, tambah_mobil, update_mobil, hapus_mobil
from sewa import sewa_mobil, kembalikan_mobil

def menu_admin():
    while True:
        clear()
        print("="*50)
        print("MENU ADMIN RENTAL MOBIL".center(50))
        print("="*50)
        print("1. Lihat Daftar Mobil")
        print("2. Tambah Mobil")
        print("3. Update Mobil")
        print("4. Hapus Mobil")
        print("5. Logout")
        pilihan = input("Pilih menu: ")
        if pilihan == "1": lihat_mobil()
        elif pilihan == "2": tambah_mobil()
        elif pilihan == "3": update_mobil()
        elif pilihan == "4": hapus_mobil()
        elif pilihan == "5": break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter...")

def menu_user(username):
    while True:
        clear()
        print("="*50)
        print(f"MENU USER - {username}".center(50))
        print("="*50)
        print("1. Lihat Mobil")
        print("2. Sewa Mobil")
        print("3. Kembalikan Mobil")
        print("4. Logout")
        pilihan = input("Pilih menu: ")
        if pilihan == "1": lihat_mobil()
        elif pilihan == "2": sewa_mobil(username)
        elif pilihan == "3": kembalikan_mobil(username)
        elif pilihan == "4": break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter...")

def main():
    while True:
        clear()
        print("="*50)
        print("SISTEM RENTAL MOBIL MAHAL".center(50))
        print("="*50)
        print("1. Login")
        print("2. Register")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            username, role = login()
            if role == "admin":
                menu_admin()
            elif role == "user":
                menu_user(username)
        elif pilihan == "2":
            register()
        elif pilihan == "3":
            print("Terima kasih telah menggunakan sistem ini!")
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter...")

if __name__ == "__main__":
    main()
