print("=== Misi dari Guru Kakashi ===")
nim = input("Masukkan nimmu : " )

stamina = int(nim[-3:])
chakra = 0

print("=== Misi ke 1 : Tes Konsentrasi ===")
while chakra < 200 and stamina > 0:
    chakra += 5
    stamina -= 3

print("\n--- Hasil Misi ke 1 ---")
print("Chakra terkumpul:", chakra)
print("Sisa stamina:", stamina)

if chakra >= 200:
    print("Naruto berhasil menyempurnakan Rasengannya! ")
else:
    print("Naruto kehabisan stamina sebelum mencapai 200 chakra... ")


print("\n=== Misi Ke 2 : Infiltrasi ===")
tinggi_menara = int(nim[-2:])
gulungan = 0

for tinggi in range(3, tinggi_menara + 1, 3):
    gulungan += 1

print("\n--- Hasil Misi Ke 2 ---")
print(f"Tinggi menara: {tinggi_menara} meter")
print(f"Jumlah gulungan informasi yang ditemukan: {gulungan}")


print("\n=== Misi Ke 3 : Penyelidikan ===")
jumlah_koridor = int(nim[-2])

data_intel = 0
perangkap = 0

for koridor in range(1, jumlah_koridor + 1):
    print(f"\nKoridor {koridor}:")
    for ruangan in range(1, 4):  
        if ruangan % 2 == 1:
            print(f"  Ruangan {ruangan} : Data Intelijen")
            data_intel += 1
        else:
            print(f"  Ruangan {ruangan} : Perangkap Peledak (dijinakkan)")
            perangkap += 1

print("\n--- Hasil Misi Ke 3 ---")
print(f"Total Data Intelijen yang dikumpulkan: {data_intel}")
print(f"Total Perangkap Peledak yang dijinakkan: {perangkap}")

print("\n=== Naruto menyelesaikan semua misi ! ===")