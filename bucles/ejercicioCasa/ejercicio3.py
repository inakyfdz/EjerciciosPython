try:
    numero = int(input("Introduce un número entero positivo: "))
    if numero < 0:
        raise ValueError ("Error: debes introducir un número entero positivo.")
    else:
        numeros = []
        for i in range(numero, -1, -1):
            numeros.append(str(i))
        print(", ".join(numeros))
except ValueError as e:
    print(e)
except Exception as e:
    print(type(e).__name__)


