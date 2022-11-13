#luas persegi
panjang_sisi = int(input("masukan panjang_sisi"))
luas = panjang_sisi * panjang_sisi
print("luas =", luas)

#luas persegi panjang
panjang_pp = int(input("masukan panjang_pp:"))
lebar_pp = int (input("masukan lebar_pp:"))
luas = panjang_pp * lebar_pp
print("luas =", luas)

#luas segitiga
aa = 1/2 
alas_segitiga = int(input("masukan alas_segitiga"))
tinggi_segitiga = int(input("masukan tinggi_segitiga"))
luas =  aa * (alas_segitiga * tinggi_segitiga)
print("luas =", luas)

#luas lingkaran
bb = 22/7
jari_lingkaran = int(input("masukan jari lingkaran"))
luas = bb * jari_lingkaran * jari_lingkaran
print("luas =", luas)

#luas jajargenjang
alas = int(input("masukan alas"))
tinggi = int(input("masukan tinggi"))
luas = alas * tinggi
print("luas =", luas)

#luas trapesium
cc = 1/2
alas_a = int(input("masukan alas_a"))
alas_b = int(input("masukan alas_b"))
tinggi = int(input("masukan tinggi"))
luas = cc * (alas_a + alas_b) * tinggi
print("luas =", luas)