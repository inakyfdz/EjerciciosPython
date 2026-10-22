
try:
    comidas = ["Paella", "Lasaña", "Hamburguesa", "Ensalada"]
    bebidas = ["Agua", "Refresco", "Cerveza", "Zumo"]
    contador = 0
    for comida in comidas:
        for bebida in bebidas:
            print(f"{comida} y {bebida}")
            contador += 1
    print (f'Hay {contador} combinaciones')

except Exception as e:
    print(type(e).__name__)