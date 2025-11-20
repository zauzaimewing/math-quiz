# function == kumpulan urutan coding yg sesuai

#def nama()
# isi dari function

#dipangil fungsinya

def tampilkan():
    print("raynel kaya eeq")

tampilkan()

def menu():
    print("aplikasi penghitung luas bangun datar")
    print("1.luas persegi panjang")
    print("2.luas persegi")
    print("3.luas segitiga")
    print("4.luas lingkaran")

def persegi_panjang():
    P = int(input("panjangnya apa woi"))
    L = int(input("lebarnya apa bajingannnnnnnnnnnnnnnnnnn"))
    rumus = P * L
    print("luasnya ituuuuuu",rumus)

 def persegi():
    S = int(input(" sisi"))
    Rumus = S * S
    print("luasnya ituuuuuu",Rumus)


menu()
cois = int(input("= "))
if cois == 1:
    persegi_panjang()

menu()
cois = int(input("= "))
if cois == 2:
    persegi()