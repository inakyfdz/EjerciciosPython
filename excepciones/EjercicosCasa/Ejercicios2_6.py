
try:

    numero = int(input("Introduce un número entero: "))


    if numero % 2 == 0:
        print(f"El número {numero} es PAR.")
    else:
        print(f"El número {numero} es IMPAR.")

except ValueError:
    print("Error: Eso no es un número entero válido.")
except KeyboardInterrupt:
    print("Se ha cancelado por el usuario")