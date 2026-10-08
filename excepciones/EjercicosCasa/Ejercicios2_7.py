
try:

    edad = int(input("Introduce tu edad: "))

    if edad < 0:
        print("Error: La edad no puede ser un número negativo.")

    elif edad >= 18:
        print("Puedes conducir un coche.")
    elif edad >= 16:
        print("Puedes conducir una moto de gran cilindrada.")
    elif edad >= 14:
        print("Puedes conducir una moto de poca cilindrada.")
    else:
        print("No puedes conducir ningún vehículo.")

except ValueError:
    print("Error: Debes introducir un número entero para la edad.")
except KeyboardInterrupt:
    print("Programa interrumpido.")
