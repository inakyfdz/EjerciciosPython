try:
    lista1 = [1, 4, 7, 9, 12, 4, 20, 32, 30, 100 ,10, 5]
    lista2 = [4, 5, 9, 9, 20, 30]

    comunes = []
    for a in lista1:
        for b in lista2:
            if a == b and a not in comunes:
                comunes.append(a)

    if comunes:
        print("Números comunes:", comunes)
    else:
        print("No hay números en común.")

except Exception as e:
    print(type(e).__name__)