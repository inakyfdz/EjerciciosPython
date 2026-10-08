import math

# Ejercicios rogramación en Python (UT1)

# 1. Calcular la suma de dos números
def ejercicio1():
    numero1 = input("dime el primer numero: ")
    numero2 = input("dime el segundo numero: ")
    suma = float(numero1) + float(numero2)
    print(suma)
    print(f"La suma es {suma}") #Esto es el modo F string (más rapido para los que son numero y texto

# 2. Calcular el area de un círculo
def ejercicio2():
    radio = input("dime el radio de un circulo: ")
    print("El area del circulo es: ", (math.pi * float(radio) ** 2))

# 3. Convertir grados Celsius a Fahrenheit
def ejercicio3():
    celsius = float(input("Dime el valor en Celsius: "))
    totalFahrenheit = (9 * celsius / 5) + 32
    print(str(celsius) + "ºC son " + str(totalFahrenheit) + "ºF")

# 4. Calcular el doble y el triple de un número
def ejercicio4():
    numero3 = int(input("dime un numero: "))
    doble = numero3 * 2
    triple = numero3 * 3
    print(str(numero3) + " su doble es " + str(doble))
    print(str(numero3) + " su triple es " + str(triple))

# 5. Calcular la media de tres números
def ejercicio5():
    numero5 = int(input("dime un numero: "))
    numero6 = int(input("dime un numero: "))
    numero7 = int(input("dime un numero: "))
    print("la media es de " + str((numero5 + numero6 + numero7) / 3))

# 6. Multiplicar dos números
def ejercicio6():
    numero8 = int(input("dime un numero: "))
    numero9 = int(input("dime un numero: "))
    print(numero8 * numero9)

# 7. Concatenar dos cadenas de texto
def ejercicio7():
    texto1 = input("dime un texto: ")
    texto2 = input("dime un texto: ")
    print(texto1 + " " + texto2)

# 8. Mostrar un número repetido varias veces
def ejercicio8():
    numer10 = int(input("dime un numero: "))
    for n in range(5):
        print(numer10)

# 9. Calcular el área de un rectángulo
def ejercicio9():
    base = int(input("dime el largo de la base: "))
    altura = int(input("dime la altura: "))
    area = base * altura
    print("El area del rectangulo es: ", area)

# 10. Calcular el perímetro de un rectángulo
def ejercicio10():
    base = int(input("dime el largo de la base: "))
    altura = int(input("dime la altura: "))
    perimetro = 2 * (base + altura)
    print("el perimetro del rectangulo es: ", perimetro)


#llamar a los ejercicios
ejercicio = int(input("dime el numero de ejercicio: "))

match ejercicio:
    case 1: ejercicio1()
    case 2: ejercicio2()
    case 3: ejercicio3()
    case 4: ejercicio4()
    case 5: ejercicio5()
    case 6: ejercicio6()
    case 7: ejercicio7()
    case 8: ejercicio8()
    case 9: ejercicio9()
    case 10: ejercicio10()
    case _:
        print("Error: El número debe estar entre 1 y 10")
