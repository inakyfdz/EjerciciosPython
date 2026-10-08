#Ejercicio 1

try:
    edad = int(input("Dime tu edad ") )
    if edad <0 :
        raise ValueError(" edad no puede ser menor a 0")
    else :
        if edad < 18 :
            print("Eres menor de edad")
        else:
            print("Eres mayor de edada" )

except ValueError as e:
    print(f'Ha sido un error de valor por {e}')
except Exception as e:
    print(type(e).__name__)