nama = input("Masukkan nama kamu: ")
jumlah_bata = int(input("Masukkan jumlah batu bata: "))
jumlah_semen = int(input("Masukkan jumlah karung semen: "))

harga_bata = 100
harga_semen = 100000

total_awal = (jumlah_bata * harga_bata) + (jumlah_semen * harga_semen)

diskon_persen = 0
keterangan_diskon = "Tidak Ada Diskon"

if jumlah_bata >= 2000 and jumlah_semen >= 16:
    diskon_persen = 30
    keterangan_diskon = "Paket Ultra Mantap (30%)"
elif jumlah_bata >= 500 and jumlah_semen >= 5:
    diskon_persen = 15
    keterangan_diskon = "Paket Hemat (15%)"

jumlah_diskon = total_awal * (diskon_persen / 100)
total_akhir = total_awal - jumlah_diskon

print("="*50)
print("        ESTIMASI BIAYA BAHAN BANGUNAN")
print("="*50)
print(f"Nama kamu : {nama}")
print("-"*50)
print(f"| {'Barang':10} | {'Jumlah':6} | {'Harga Satuan':12} |")
print("-"*50)
print(f"| {'Batu Bata':10} | {jumlah_bata:6} | Rp{harga_bata:10,} |")
print(f"| {'Semen':10} | {jumlah_semen:6} | Rp{harga_semen:10,} |")
print("-"*50)
print(f"Total Biaya Awal     : Rp{total_awal:,.0f}")
print(f"Diskon yang Didapat  : {keterangan_diskon}")
print(f"Jumlah Diskon        : Rp{jumlah_diskon:,.0f}")
print("-"*50)
print(f"TOTAL BIAYA AKHIR    : Rp{total_akhir:,.0f}")
print("="*50)