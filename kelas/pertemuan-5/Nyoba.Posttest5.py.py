import os
import time

# ===== DATA AKUN (NESTED LIST) =====
users = [
    ["admin", "admin123", "admin"]
]

# ===== DATA MOBIL MAHAL (NESTED LIST) =====
mobil_list = [
    ["KT1234AA", "Toyota Alphard", 1500000, "Tersedia"],       # Kalimantan Timur
    ["DA5678BB", "BMW i8", 2500000, "Tersedia"],               # Kalimantan Selatan
    ["KH8765CC", "Mercedes Benz S-Class", 2800000, "Tersedia"],# Kalimantan Tengah
    ["KB4321DD", "Range Rover Evoque", 2000000, "Tersedia"],   # Kalimantan Barat
    ["KU9999EE", "Porsche Cayenne", 3000000, "Tersedia"]       # Kalimantan Utara
]

# ===== PROGRAM UTAMA =====
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*50)
    print("SISTEM MANAJEMEN RENTAL MOBIL MAHAL".center(50))
    print("="*50)
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    menu_awal = input("Pilih menu: ").strip()

    # ========== LOGIN ==========
    if menu_awal == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        login_berhasil = False
        role = ""

        for u in users:
            if u[0] == username and u[1] == password:
                login_berhasil = True
                role = u[2]
                break

        if not login_berhasil:
            print("❌ Username atau password salah!")
            input("Tekan Enter untuk kembali...")
            continue

        print(f"✅ Login berhasil sebagai {role.upper()}")
        input("Tekan Enter untuk masuk ke menu...")

        # ========== MENU ADMIN ==========
        if role == "admin":
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("="*50)
                print("MENU ADMIN RENTAL MOBIL MAHAL".center(50))
                print("="*50)
                print("1. Lihat daftar mobil")
                print("2. Tambah mobil")
                print("3. Update mobil")
                print("4. Hapus mobil")
                print("5. Logout")
                pilih_admin = input("Pilih menu: ").strip()

                # ===== READ =====
                if pilih_admin == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DAFTAR MOBIL ===")
                    print(f"{'Plat':<10}{'Nama Mobil':<25}{'Harga':<12}{'Status'}")
                    print("-"*55)
                    for m in mobil_list:
                        print(f"{m[0]:<10}{m[1]:<25}Rp{m[2]:<10}{m[3]}")
                    input("\nTekan Enter untuk kembali...")

                # ===== CREATE =====
                elif pilih_admin == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== TAMBAH MOBIL BARU ===")
                    plat = input("Plat mobil (misal KT8888XX): ").upper().strip()
                    nama = input("Nama mobil: ").strip()
                    harga = input("Harga sewa per hari: ").strip()

                    if not harga.isdigit():
                        print("⚠ Harga harus berupa angka!")
                    else:
                        mobil_list.append([plat, nama, int(harga), "Tersedia"])
                        print("✅ Mobil berhasil ditambahkan!")
                    input("Tekan Enter...")

                # ===== UPDATE =====
                elif pilih_admin == "3":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== UPDATE DATA MOBIL ===")
                    for i, m in enumerate(mobil_list):
                        print(f"{i+1}. {m[0]} - {m[1]} - Rp{m[2]} - {m[3]}")
                    nomor = input("Pilih nomor mobil yang ingin diupdate: ").strip()

                    if not nomor.isdigit() or int(nomor) < 1 or int(nomor) > len(mobil_list):
                        print("⚠ Nomor tidak valid!")
                        input("Tekan Enter...")
                        continue

                    idx = int(nomor) - 1
                    nama_baru = input("Nama baru (kosong jika tidak diubah): ").strip()
                    harga_baru = input("Harga baru (kosong jika tidak diubah): ").strip()
                    status_baru = input("Status baru (Tersedia/Disewa): ").strip()

                    if nama_baru:
                        mobil_list[idx][1] = nama_baru
                    if harga_baru.isdigit():
                        mobil_list[idx][2] = int(harga_baru)
                    if status_baru in ["Tersedia", "Disewa"]:
                        mobil_list[idx][3] = status_baru

                    print("✅ Data mobil berhasil diperbarui!")
                    input("Tekan Enter...")

                # ===== DELETE =====
                elif pilih_admin == "4":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== HAPUS MOBIL ===")
                    for i, m in enumerate(mobil_list):
                        print(f"{i+1}. {m[0]} - {m[1]}")
                    hapus = input("Pilih nomor mobil yang ingin dihapus: ").strip()

                    if not hapus.isdigit() or int(hapus) < 1 or int(hapus) > len(mobil_list):
                        print("⚠ Nomor tidak valid!")
                        input("Tekan Enter...")
                        continue

                    del mobil_list[int(hapus) - 1]
                    print("✅ Mobil berhasil dihapus!")
                    input("Tekan Enter...")

                elif pilih_admin == "5":
                    break
                else:
                    print("⚠ Pilihan tidak valid!")
                    input("Tekan Enter...")

        # ========== MENU USER ==========
        else:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("="*50)
                print(f"MENU PENGGUNA ({username})".center(50))
                print("="*50)
                print("1. Lihat daftar mobil")
                print("2. Sewa mobil")
                print("3. Kembalikan mobil")
                print("4. Logout")
                pilih_user = input("Pilih menu: ").strip()

                # ===== READ =====
                if pilih_user == "1":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== DAFTAR MOBIL MAHAL ===")
                    print(f"{'Plat':<10}{'Nama Mobil':<25}{'Harga':<12}{'Status'}")
                    print("-"*55)
                    for m in mobil_list:
                        print(f"{m[0]:<10}{m[1]:<25}Rp{m[2]:<10}{m[3]}")
                    input("\nTekan Enter untuk kembali...")

                # ===== SEWA MOBIL =====
                elif pilih_user == "2":
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("=== SEWA MOBIL ===")
                    for i, m in enumerate(mobil_list):
                        print(f"{i+1}. {m[1]} ({m[3]})")
                    index = input("Pilih nomor mobil: ").strip()

                    if index.isdigit():
                        idx = int(index) - 1
                        if 0 <= idx < len(mobil_list):
                            if mobil_list[idx][3] == "Tersedia":
                                mobil_list[idx][3] = f"Disewa oleh {username}"
                                print(f" Mobil {mobil_list[idx][1]} berhasil disewa!")
                            else:
                                print(" Mobil sedang disewa!")
                        else:
                            print(" Nomor tidak valid!")
                    else:
                        print(" Masukkan angka!")
                    input("Tekan Enter...")

                # ===== KEMBALIKAN MOBIL =====
                elif pilih_user == "3":
                    ditemukan = False
                    for m in mobil_list:
                        if m[3] == f"Disewa oleh {username}":
                            m[3] = "Tersedia"
                            print(f" Mobil {m[1]} telah dikembalikan.")
                            ditemukan = True
                    if not ditemukan:
                        print(" Anda belum menyewa mobil.")
                    input("Tekan Enter...")

                elif pilih_user == "4":
                    break
                else:
                    print(" Pilihan tidak valid!")
                    input("Tekan Enter...")

    # ========== REGISTER ==========
    elif menu_awal == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("=== REGISTER AKUN BARU ===")
        username = input("Masukkan username: ").strip()
        password = input("Masukkan password: ").strip()

        sudah_ada = False
        for u in users:
            if u[0] == username:
                sudah_ada = True
                break

        if sudah_ada:
            print(" Username sudah digunakan!")
        else:
            users.append([username, password, "user"])
            print(" Registrasi berhasil!")
        input("Tekan Enter untuk kembali...")

    # ========== KELUAR ==========
    elif menu_awal == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Terima kasih telah menggunakan program ini!")
        time.sleep(1)
        break

    else:
        print(" Pilihan tidak valid!")
        input("Tekan Enter...")