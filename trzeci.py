suma_gorna = 200
suma_dolna = 100
suma = 8
if 100 < suma and suma< 200:
    print('Promocja 30%')
    suma = suma - (suma *30)/100
elif suma >=200:
    print("PRomocja 50%")
    suma = suma - (suma/2)
else:
    print("bez promocji")
