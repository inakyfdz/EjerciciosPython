#Ejercicio 2

try:
    numero1 = int(input("Dime un numero: "))
    numero2 = int(input("Dime un numero: "))

    if numero2<numero1 :
        print(f'El primer numero es mayor {numero1}')
    elif numero2 > numero1:
        print(f'El primer numero es mayor {numero2}')
    else :
        print("Son dos numero iguales")

except ValueError as e:
    print(f'Ha sido un error de valor por {e}')
except Exception as e:
    print(type(e).__name__)