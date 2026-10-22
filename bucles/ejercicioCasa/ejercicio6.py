import random

secreto = random.randint(1, 100)
intentos = 0

while True:
    try:
        intento = int(input("Adivina el número (1-100): "))


        intentos += 1
        if intento < secreto:
            print("El número es mayor.")
        elif intento > secreto:
            print("El número es menor.")
        else:
            print(f" Lo has adivinado en {intentos} intentos.")
            break
    except ValueError:
        print("Error: introduce un número entero.")
        continue