import os
from data_mobil import clear
from sewa import sewa_mobil, kembalikan_mobil
from data_mobil import lihat_mobil, tambah_mobil, update_mobil, hapus_mobil

users = {
    "admin": {"password": "admin123", "role": "admin"}
}

def login():
    clear()
    print("=== LOGIN ===")
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

    if username in users and users[username]["password"] == password:
        print(f"Login berhasil sebagai {users[username]['role'].upper()}")
        input("Tekan Enter untuk lanjut...")
        if users[username]["role"] == "admin":
            menu_admin()
        else:
            menu_user(username)
    else:
        print("Username atau password salah!")
        input("Tekan Enter...")


def register():
    clear()
    print("=== REGISTER AKUN BARU ===")
    username = input("Masukkan username baru: ").strip()
    if username in users:
        print("Username sudah terdaftar!")
    else:
        password = input("Masukkan password: ").strip()
        users[username] = {"password": password, "role": "user"}
        print("Registrasi berhasil! Silakan login.")
    input("Tekan Enter...")


def menu_admin():
    while True:
        clear()
        print("=" * 50)
        print("MENU ADMIN RENTAL MOBIL".center(50))
        print("=" * 50)
        print("1. Lihat daftar mobil")
        print("2. Tambah mobil")
        print("3. Update mobil")
        print("4. Hapus mobil")
        print("5. Logout")

        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            lihat_mobil()
        elif pilih == "2":
            tambah_mobil()
        elif pilih == "3":
            update_mobil()
        elif pilih == "4":
            hapus_mobil()
        elif pilih == "5":
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter...")


def menu_user(username):
    while True:
        clear()
        print("=" * 50)
        print(f"MENU PENGGUNA ({username})".center(50))
        print("=" * 50)
        print("1. Lihat daftar mobil")
        print("2. Sewa mobil")
        print("3. Kembalikan mobil")
        print("4. Logout")

        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            lihat_mobil()
        elif pilih == "2":
            sewa_mobil(username)
        elif pilih == "3":
            kembalikan_mobil(username)
        elif pilih == "4":
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter...")
