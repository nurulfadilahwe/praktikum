a = int(input("masukan a : "))
b = int(input("masukan b : "))
c = int(input("masukan c : "))

if (a==b==c) :
    print("segitiga sama sisi")
elif (a==b or b==c or a==c) :
    print("segitiga sama kaki")
