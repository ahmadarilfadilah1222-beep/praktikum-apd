# membuat fungsi
def salam():
    print ("Halo, Aril")
def kali():
    X = 5*5
    print(X)
# memanggil fungsi
salam()
salam()
salam()
kali()
kali()
kali()

# membuat fungsi dengan parameter
def luas_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    print ("luas persegi panjang adalah ", luas)
# Pemanggilan Fungsi luas_persegi_panjang
luas_persegi_panjang(4, 5)


# Contoh Program mengembalikan hasil fungsi
def luas_persegi(sisi):
   luas = sisi * sisi
   return luas

# pemanggilan fungsi luas persegi
print ("Luas persegi :", luas_persegi(8))

# rumus: sisi x sisi
def luas_persegi(sisi):
    luas = sisi * sisi
    return luas
# rumus: sisi x sisi x sisi
def volume_persegi(sisi):
    volume = luas_persegi(sisi) * sisi
    print ("Volume Persegi = ", volume)

# pemanggilan Fungsi
luas_persegi(4)
volume_persegi(6)

# membuat variabel lokal dan global
# variabel global
Nama = "Aril"
Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
#variabel lokal
def info():
    Nama = "Informatika"
    Mata_Kuliah = "Logika Informatika"
    # mengakses variabel lokal
    print("Prodi:", Nama)
    print("Mata Kuliah:", Mata_Kuliah)
    # mengakses variabel global
    print("Prodi:", Nama)
    print("Mata Kuliah:", Mata_Kuliah)
# memanggil fungsi
info()

def faktorial(n):
    # Basis (Base Case): Kondisi berhenti
    if n == 1 or n == 0:
     return 1
    # Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
    else:
     print(n)
     return n * faktorial(n - 1)
    # Memanggil fungsi
hasil = faktorial(5)
print(f"Hasil dari 5! adalah: {hasil}")


# Variabel global untuk menyimpan data Film
film = []
# Fungsi untuk menampilkan semua data
def show_data():
    if len(film) <= 0:
     print("Belum Ada data")
    else:
     print("ID | Judul Film")
    for indeks in range(len(film)):
      print(indeks, "|", film[indeks])



# Fungsi untuk menampilkan semua data
def show_data():
    if len(film) <= 0:
       print("Belum Ada data")
    else:
       print("ID | Judul Film")
    for indeks in range(len(film)):
       print(indeks, "|", film[indeks])

# Fungsi untuk menambah data
def insert_data():
    film_baru = input("Judul Film: ")
    film.append(film_baru)
print("Film berhasil ditambahkan!")

# Fungsi untuk mengedit data
def edit_data():
    show_data()
    indeks = int(input("Inputkan ID film: "))
    if indeks >= len(film) or indeks < 0:
      print("ID salah")
    else:
      judul_baru = input("Judul baru: ")
      film[indeks] = judul_baru
print("Film berhasil diupdate!")

# Fungsi untuk menghapus data
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID film: "))
    if indeks >= len(film) or indeks < 0:
      print("ID salah")
    else:
     film.remove(film[indeks])
print("Film berhasil dihapus!")



# fungsi untuk menampilkan menu
def show_menu():
    print ("\n")
print ("----------- MENU---------- ")
print ("[1] Show Data")
print ("[2] Insert Data")
print ("[3] Edit Data")
print ("[4] Delete Data")
print ("[5] Exit")
menu = input("PILIH MENU> ")
print ("\n")
if menu == "1":
   show_data()
elif menu == "2":
   insert_data()
elif menu == "3":
   edit_data()
elif menu == "4":
   delete_data()
elif menu == "5":
   exit()
else:
   print ("Salah pilih!")


# Fungsi untuk menampilkan semua data
Film = []
def show_data():
    if len(film) <= 0:
       print("Belum Ada data")
    else:
       print("ID | Judul Film")
for indeks in range(len(film)):
    print(indeks, "|", film[indeks])

# Fungsi untuk menambah data
def insert_data():
    film_baru = input("Judul Film: ")
    film.append(film_baru)
print("Film berhasil ditambahkan!")

# Fungsi untuk mengedit data
def edit_data():
    show_data()
indeks = int(input("Inputkan ID film: "))
if indeks >= len(film) or indeks < 0:
    print("ID salah")


else:
  judul_baru = input("Judul baru: ")
film[indeks] = judul_baru
print("Film berhasil diupdate!")

# Fungsi untuk menghapus data
def delete_data():
    show_data()
indeks = int(input("Inputkan ID film: "))
if indeks >= len(film) or indeks < 0:
   print("ID salah")
else:
   film.remove(film[indeks])
print("Film berhasil dihapus!")

# fungsi untuk menampilkan menu
def show_menu():
    print ("\n")
print ("----------- MENU---------- ")
print ("[1] Show Data")
print ("[2] Insert Data")
print ("[3] Edit Data")
print ("[4] Delete Data")
print ("[5] Exit")
menu = input("PILIH MENU> ")
print ("\n")

if menu == "1":
   show_data()
elif menu == "2":
     insert_data()
elif menu == "3" :
     edit_data()
elif menu == "4":
    delete_data()
elif menu == "5":
    exit()
else:
    print ("salah pilih")
while (True):
   show_menu()
