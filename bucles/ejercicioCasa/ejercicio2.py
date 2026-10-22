try:
    numero1 = int(input("Ingrese el primer numero: "))
    for numero2 in range(0, 11):
        print (f'{numero1} x {numero2} = {numero1 * numero2}')

except ValueError  as e:
    print("Error por valor")
except Exception as e:
    print(type(e).__name__)