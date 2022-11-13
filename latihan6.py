#peerkalian
bilangan = int(input("masukan bilangan : "))
for i in range(1, 11):
    hasil = bilangan * i
    print(bilangan, "x", i, "=", hasil)

#bilangan ganjil genap
print("")
list1 = 1,2,3,4,5,6,7,8,9
genap = 0
ganjil = 0
print(("list angka, ", list1))
for item in list1:
    if item % 2 == 0:
        genap += 1
print("jumlah bilangan genap :", genap)
for item in list1:
    if item % 2 != 0:
        ganjil += 1
print("jumlah bilangan ganjil :", ganjil)