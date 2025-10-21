buah = {"apel", "jeruk", "mangga", "apel"}
print(buah)

angka_ganjil = {1, 3, 5, 7, 9}

for angka in angka_ganjil:
 print(angka)

Daftar_buku = {
"Buku1" : "Bumi Manusia",
"Buku2" : "Laut Bercerita"
}

print(Daftar_buku["Buku1"])
print(Daftar_buku)

Biodata = {
"Nama" : "Ananda Daffa Harahap",
"NIM" : 2409106050,
"KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
"Mahasiswa_Aktif" : True,
"Social Media" : {"Instagram" : "daffahrhap"}
}
print(f"nama saya adalah {Biodata["Nama"]}")
print(f"Instagram : {Biodata['Social Media']['Instagram']}")
print(f"nama saya adalah {Biodata.get["Nama"]}")
print({Biodata.get("Nama")})

Nilai = {
"Matematika": 80,
"B. Indonesia": 90,
"B. Inggris": 81,
"Kimia": 78,
"Fisika": 80
}
# Tanpa menggunakan items()
for i in Nilai:
  print(i)

print("") # pemisah

# Menggunakan items()
for i, j in Nilai.items():
  print(f"Nilai {i} anda adalah {j}")

Film = {
"Avenger Endgame" : "Action",
"Sherlock Holmes" : "Mystery",
"The Conjuring" : "Horror"
}
#Sebelum Diubah
print(Film)
Film["Sherlock Holmes"] = "Action"
Film.update({"The Conjuring" : "Tragedy"})
print(Film) 

data = {
"Nama" : "Daffa",
"Umur" : 19,
"Jurusan" : "Informatika"
}
#Sebelum Dihapus
print(data)
del data["Nama"]
#Setelah diubah
print(data)
#memanggil data yang telah dihapus
print(data.get("Jurusan"))


cache = data.pop("Nama")
#Setelah dihapus
print(data)
#memanggil data yang telah dihapus pada dictionary
print(data.get("Nama"))
#memanggil data yang telah dihapus pada variabel cache
print(cache)


#Sebelum Dihapus
print(data)
data.clear()
#Setelah dihapus
print(data)




buku = {
"Buku1" : "Bumi Manusia",
"Buku2" : "Laut Bercerita"
}
pinjam = buku.copy()
print(pinjam)



key = "apel", "jeruk", "mangga"
value = 1, 2, 3
buah = dict.fromkeys(key, value)
print(buah) 