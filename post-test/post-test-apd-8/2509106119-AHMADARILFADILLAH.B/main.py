import os
from autentikasi import login, register
from data_mobil import clear

def main():
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
            login()
        elif menu == "2":
            register()
        elif menu == "3":
            clear()
            print("Terima kasih telah menggunakan program ini!")
            input("Tekan Enter untuk keluar...")
            break
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter...")

if __name__ == "__main__":
    main()
 