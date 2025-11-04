#angka = int("10")
#print(angka)

for i, v in enumerate(['a','b']):
    print(i, v) # 0 a , 1 b

len([10, 20, 30]) # 3

list(map(str, [1,2,3])) # ['1', '2', '3']

sorted([3, 1, 2]) # [1, 2, 3]

list(zip([1,2],['a','b'])) # [(1,'a'), (2,'b')]

x = 42
def fungsi():
 x = 10
 y = 20
 z = 30
print(globals()['x']) # mendapatkan isi dari variabel x (global)
print(locals()['x']) # mendapatkan isi dari variabel x (lokal)
print(locals()) # {'x': 10, 'y': 20, 'z': 30}
fungsi()

import math
from math import sqrt
import math as m
import math
print(math.sqrt(16))
print(math.factorial(4))

import random
print(random.randint(1, 5)) # menghasilkan angka random dari 1 - 4
pilih_acak = ["pisang", "rambutan", "manggis"]
acak = "apcb"
print(random.choice(pilih_acak)) # memilih 1 element secara acak pada list
print(random.choice(acak)) # memilih 1 karakter acak pada string
# memasukkan satu persatu nilai dari kumpulan_angka
# ke dalam variabel hasil dengan isinya 4 karakter hasil randomize
kumpulan_angka = "1234567890"
hasil = ""
for i in range(4):
   hasil += random.choice(kumpulan_angka)
print(hasil)
acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
random.shuffle(acak_kartu) # kocok kartu, output berupa urutan list yang berubah
print(acak_kartu)

