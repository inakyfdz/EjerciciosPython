import math


class ErrorEcuacion(Exception):
    pass


try:

    a = float(input("Introduce el valor de a: "))
    b = float(input("Introduce el valor de b: "))
    c = float(input("Introduce el valor de c: "))


    if a == 0:
        raise ErrorEcuacion("El coeficiente a no puede ser cero.")


    discriminante = b**2 - 4 * a * c


    if discriminante < 0:
        raise ErrorEcuacion("La ecuacion no tiene raices reales.")


    x1 = (-b + math.sqrt(discriminante)) / (2 * a)
    x2 = (-b - math.sqrt(discriminante)) / (2 * a)


    print(f"La primera raiz es: {x1}")
    print(f"La segunda raiz es: {x2}")

except ValueError:
    print("Error: debes introducir valores numericos.")

except ErrorEcuacion as error:
    print(f"Error: {error}")