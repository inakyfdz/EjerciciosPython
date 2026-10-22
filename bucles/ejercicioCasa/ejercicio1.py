try:

    salir = False
    opcion = 0
    while not salir:
        print("Elije una opcion:")
        print("1.Sumar")
        print("2.Restar")
        print("3.Multiplicar")
        print("4.Dividir")
        print("5.Salir")
        opcion = int(input())
        if opcion != 5:
            numero1 = int(input("Ingrese el primer numero: "))
            numero2 = int(input("Ingrese el segundo numero: "))
        resultado = 0
        match opcion:
            case 1:
                resultado = numero1 + numero2
            case 2:
                resultado = numero1 - numero2
            case 3:
                resultado = numero1 * numero2
            case 4:
                resultado = numero1 / numero2
            case 5:
                resultado ="Adios"
                salir = True
            case _:
                resultado = "Opcion no valida"

        print(resultado)
except ValueError as e:
    print("Error de valor")
except Exception as e:
    print(type(e).__name__)