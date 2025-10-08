umur = int(input("Masukkan umur Anda: "))

if umur < 13:
   kategori = "Anak-anak"
elif umur < 18:
   kategori = "Remaja"
elif umur < 60:
   kategori = "Dewasa"
else:
   kategori = "Lansia"

print("Umur:", umur, "Kategori:", kategori)





