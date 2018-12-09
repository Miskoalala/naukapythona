
produkty = ["mleko","ser","chleb","kielbasa"]
cena = [ 10,6, 3,20]
suma = 0

for c in cena:
    suma = suma + c

if suma > 15:
    print("20% off, >15zl")
    suma = suma - (suma * 20)/100
if len(produkty) > 3:
    print("000 Udane zakupy")
    suma = suma - (suma * 15)/1000

print("Do zaplaty:{0}".format(suma))
