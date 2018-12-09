koszyk = [{"name": "mleko", "cena": 10},
          {"name": "ser", "cena": 12},
          {"name": "chleb", "cena": 8}]
print(koszyk[0]["cena"])
print(koszyk[1]["cena"])
print(koszyk[2]["cena"])
print(koszyk[0]["name"])
suma = 0
bylo_mleko = False
byl_ser = False
for poz in koszyk:
    suma = suma + poz["cena"]
    print(suma)

for poz in koszyk:
    suma = suma + poz["cena"]
    nazwa_prod = poz["name"]
    if nazwa_prod == "mleko":
        bylo_mleko = True
    if nazwa_prod =="ser":
        byl_ser = True
print("Znizka!!!!")
