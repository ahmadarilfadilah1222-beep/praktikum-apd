import os
users = {
    "admin": {"password": "admin123", "role": "admin"}
}

mobil_list = {
    "KT1234AA": {"nama": "Toyota Alphard", "harga": 1500000, "status": "Tersedia"},
    "DA5678BB": {"nama": "BMW i8", "harga": 2500000, "status": "Tersedia"},
    "KH8765CC": {"nama": "Mercedes Benz S-Class", "harga": 2800000, "status": "Tersedia"},
    "KB4321DD": {"nama": "Range Rover Evoque", "harga": 2000000, "status": "Tersedia"},
    "KU9999EE": {"nama": "Porsche Cayenne", "harga": 3000000, "status": "Tersedia"}
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()
    print("=" * 50)
    print("SISTEM RENTAL MOBIL MAHAL".center(50))
    print("=" * 50)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu = input("Pilih menu (1/2/3): ").strip()

    if menu == "1":
        clear()
        print("=== LOGIN ===")
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()

        if username in users and users[username]["password"] == password:
            role = users[username]["role"]
            print(f"Login berhasil sebagai {role.upper()}")
            input("Tekan Enter untuk lanjut...")

            if role == "admin":
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
                        clear()
                        print("=== DAFTAR MOBIL ===")
                        print(f"{'Plat':<10}{'Nama Mobil':<25}{'Harga':<12}{'Status'}")
                        print("-" * 55)
                        for plat, data in mobil_list.items():
                            print(f"{plat:<10}{data['nama']:<25}Rp{data['harga']:<10}{data['status']}")
                        input("\nTekan Enter untuk kembali...")

                    elif pilih == "2":
                        clear()
                        print("=== TAMBAH MOBIL BARU ===")
                        plat = input("Plat mobil (misal KT8888XX): ").upper().strip()
                        if plat in mobil_list:
                            print(" Plat sudah terdaftar!")
                            input("Tekan Enter...")
                            continue

                        nama = input("Nama mobil: ").strip()
                        harga = input("Harga sewa per hari: ").strip()

                        if not harga.isdigit():
                            print(" Harga harus angka!")
                        else:
                            mobil_list[plat] = {
                                "nama": nama,
                                "harga": int(harga),
                                "status": "Tersedia"
                            }
                            print(" Mobil berhasil ditambahkan!")
                        input("Tekan Enter...")

                    elif pilih == "3":
                        clear()
                        print("=== UPDATE DATA MOBIL ===")
                        for i, plat in enumerate(mobil_list.keys(), start=1):
                            data = mobil_list[plat]
                            print(f"{i}. {plat} - {data['nama']} - Rp{data['harga']} - {data['status']}")
                        plat_update = input("Masukkan plat mobil yang ingin diupdate: ").upper().strip()

                        if plat_update not in mobil_list:
                            print(" Plat tidak ditemukan!")
                            input("Tekan Enter...")
                            continue

                        nama_baru = input("Nama baru (kosong = tidak ubah): ").strip()
                        harga_baru = input("Harga baru (kosong = tidak ubah): ").strip()
                        status_baru = input("Status baru (Tersedia/Disewa): ").strip()

                        if nama_baru:
                            mobil_list[plat_update]["nama"] = nama_baru
                        if harga_baru.isdigit():
                            mobil_list[plat_update]["harga"] = int(harga_baru)
                        if status_baru in ["Tersedia", "Disewa"]:
                            mobil_list[plat_update]["status"] = status_baru

                        print(" Data mobil berhasil diperbarui!")
                        input("Tekan Enter...")

                    elif pilih == "4":
                        clear()
                        print("=== HAPUS MOBIL ===")
                        plat_hapus = input("Masukkan plat mobil yang ingin dihapus: ").upper().strip()
                        if plat_hapus in mobil_list:
                            del mobil_list[plat_hapus]
                            print(" Mobil berhasil dihapus!")
                        else:
                            print(" Plat tidak ditemukan!")
                        input("Tekan Enter...")

                    elif pilih == "5":
                        break
                    else:
                        print(" Pilihan tidak valid!")
                        input("Tekan Enter...")

            else:
                while True:
                    clear()
                    print("=" * 50)
                    print(f"MENU PENGGUNA ({username})".center(50))
                    print("=" * 50)
                    print("1. Lihat daftar mobil")
                    print("2. Sewa mobil")
                    print("3. Kembalikan mobil")
                    print("4. Logout")
                    pilih_user = input("Pilih menu: ").strip()

                    if pilih_user == "1":
                        clear()
                        print("=== DAFTAR MOBIL ===")
                        print(f"{'Plat':<10}{'Nama Mobil':<25}{'Harga':<12}{'Status'}")
                        print("-" * 55)
                        for plat, data in mobil_list.items():
                            print(f"{plat:<10}{data['nama']:<25}Rp{data['harga']:<10}{data['status']}")
                        input("\nTekan Enter...")

                    elif pilih_user == "2":
                        clear()
                        print("=== SEWA MOBIL ===")
                        for i, (plat, data) in enumerate(mobil_list.items(), start=1):
                            print(f"{i}. {plat} - {data['nama']} ({data['status']})")

                        plat_sewa = input("Masukkan plat mobil yang ingin disewa: ").upper().strip()
                        if plat_sewa in mobil_list:
                            if mobil_list[plat_sewa]["status"] == "Tersedia":
                                mobil_list[plat_sewa]["status"] = f"Disewa oleh {username}"
                                print(f" Mobil {mobil_list[plat_sewa]['nama']} berhasil disewa!")
                            else:
                                print(" Mobil sedang disewa!")
                        else:
                            print(" Plat tidak ditemukan!")
                        input("Tekan Enter...")

                    elif pilih_user == "3":
                        ditemukan = False
                        for data in mobil_list.values():
                            if data["status"] == f"Disewa oleh {username}":
                                data["status"] = "Tersedia"
                                print(f" Mobil {data['nama']} telah dikembalikan.")
                                ditemukan = True
                        if not ditemukan:
                            print(" Anda belum menyewa mobil.")
                        input("Tekan Enter...")

                    elif pilih_user == "4":
                        break
                    else:
                        print(" Pilihan tidak valid!")
                        input("Tekan Enter...")

        else:
            print(" Username atau password salah!")
            input("Tekan Enter...")

    elif menu == "2":
        clear()
        print("=== REGISTER AKUN BARU ===")
        username = input("Masukkan username baru: ").strip()
        if username in users:
            print(" Username sudah terdaftar!")
        else:
            password = input("Masukkan password: ").strip()
            users[username] = {"password": password, "role": "user"}
            print(" Registrasi berhasil! Silakan login.")
        input("Tekan Enter...")

    elif menu == "3":
        clear()
        print("Terima kasih telah menggunakan program ini!")
        input("Tekan Enter untuk keluar...")
        break

    else:
        print(" Pilihan tidak valid!")
        input("Tekan Enter...")
