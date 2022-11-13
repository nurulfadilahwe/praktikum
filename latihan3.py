#List_kosong
list_kosong = []
print(list_kosong)

#list_buah
list_buah = ['pisang', 'nanas', 'melon','durian']
print(list_buah[0])
print(list_buah[1])
print(list_buah[2])
print(list_buah[3])

print('------------')

print(list_buah[-1])
print(list_buah[-2])
print(list_buah[-3])
print(list_buah[-4])

print('------------')

#List_nilai
list_nilai = [80, 70, 90, 60]
print(list_nilai)

#List_jawaban
list_jawaban = [150, 33.33, 'Presiden Sukarno', False]
print(list_jawaban)

print('##############')

#list buah
list_buah = ['jeruk', 'naga', 'pepaya', 'mangga']
print(list_buah)

#append
list_buah.append('sirsak')
print(list_buah)

#insert
list_buah.insert(0, 'jambu')
print(list_buah)

list_buah.insert(3, 'manggis')
print(list_buah)

list_angka = [1, 2, 3, 4, 5]
print(list_angka)

#remove
list_angka.remove(5)
print(list_angka)

print('atau menggunakan')

#pop
list_angka = [1, 2, 3, 4, 5]
print(list_angka)
angka_yang_terhapus = list_angka.pop()
print('angka yang terhapus', 'angka_yang_terhapus')
print(list_angka)

#operator
list_buah1 = ['mangga', 'jeruk', 'jambu']
list_buah2 = ['mangga', 'jeruk', 'jambu']
list_baru = list_buah1 + list_buah2
print(list_baru)
