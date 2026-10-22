enVenta = True
stock = 25


def sacarMenu():
    print("\nBienvenido al teatro, hoy tenemos Homer vs Peter Griffin")
    print("1. Comprar entradas.")
    print("2. Mostrar entradas disponibles.")
    print("3. Salir.")
    return int(input("Elije una opcion valida: "))


def realizarCompra():
    global stock
    while True:
        numeroEntradasPedidas = int(input("¿Cuántas entradas necesitas?: "))

        if numeroEntradasPedidas <= 0:
            print("Por favor, introduce una cantidad válida.")
            continue

        if numeroEntradasPedidas > stock:
            print(f"No hay tantas entradas disponibles (Stock actual: {stock}).")
            opcion = int(input("¿Deseas cambiar la cantidad? (1 para Sí, 0 para No): "))
            if opcion == 0:
                break
        else:
            stock -= numeroEntradasPedidas
            print(f"¡Compra realizada con éxito! Has comprado {numeroEntradasPedidas} entradas.")
            break


# Bucle principal del programa
while enVenta:
    try:
        eleccion = sacarMenu()

        match eleccion:
            case 1:
                realizarCompra()
            case 2:
                print(f"\nEntradas disponibles: {stock}")
            case 3:
                print("¡Adiós!")
                enVenta = False
            case _:
                print("Elección no válida. Elige un número del 1 al 3.")

    except ValueError:
        print("Error: Por favor, introduce un número entero válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {type(e).__name__}")
