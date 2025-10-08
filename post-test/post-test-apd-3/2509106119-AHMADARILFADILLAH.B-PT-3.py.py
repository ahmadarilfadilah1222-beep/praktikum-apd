print("=== Penghitung Gaji Karyawan PT. BOM ===")

nama = input("Masukkan Nama Karyawan: ")
jabatan = input("Masukkan Jabatan Karyawan (peracik petasan/pengantar petasan): ").lower()
hari_kerja = int(input("Masukkan Jumlah Hari Kerja: "))
jam_kerja = int(input("Masukkan Jam Kerja per Hari: "))
lembur = int(input("Masukkan Jumlah Lembur: "))

if jabatan == "peracik petasan":
    if hari_kerja >= 24 and jam_kerja >= 8 and lembur >= 4:
        bayaran_perjam = 25000
        bayaran_lembur = 15000
    elif hari_kerja >= 18 and jam_kerja >= 6 and lembur >= 2:
        bayaran_perjam = 20000
        bayaran_lembur = 10000
    else:
        bayaran_perjam = 15000
        bayaran_lembur = 10000

elif jabatan == "pengantar petasan":
    if hari_kerja >= 20 and jam_kerja >= 7 and lembur >= 7:
        bayaran_perjam = 25000
        bayaran_lembur = 20000
    elif hari_kerja >= 16 and jam_kerja >= 5 and lembur >= 4:
        bayaran_perjam = 20000
        bayaran_lembur = 15000
    else:
        bayaran_perjam = 15000
        bayaran_lembur = 12000
else:
    print("Jabatan tidak dikenali!")

total_gaji = ((bayaran_perjam * jam_kerja) * hari_kerja) + (lembur * bayaran_lembur)

print("\n=== Laporan Gaji Karyawan ===")
print(f"Nama Karyawan     : {nama}")
print(f"Jabatan           : {jabatan}")
print(f"Hari Kerja        : {hari_kerja}")
print(f"Jam Kerja / Hari  : {jam_kerja}")
print(f"Jumlah Lembur     : {lembur}")
print(f"Bayaran per Jam   : Rp {bayaran_perjam}")
print(f"Bayaran per Lembur: Rp {bayaran_lembur}")
print(f"Total Gaji        : Rp {total_gaji}")