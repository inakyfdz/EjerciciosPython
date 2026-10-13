
        #Errores personalizados
    #Numeros negaticos con mensaje inicial preprogramado
class numerosNegativos(Exception):
    def __init__(self, mensaje="Los numeros no pueden ser negativos" ):
        super().__init__(mensaje)
        self.mensaje = mensaje



try:
    #variables
    numero = int(input("Dime un numero: "))
    esPrimo = True
    #si es menor de 0 salta error
    if numero < 0:
        raise numerosNegativos()
    if (numero <= 3) : esPrimo = True #Si el numero es igual o menor a 1 es imposible que sea primo
    else:
        for i in range(2, (numero//2)+1):
            if numero % i == 0:
                esPrimo = False
            break

    if(esPrimo):
        print("El numero es primo")
    else:
        print("El numero no es primo")
except ValueError:
    print("No se pueden ser palabras")
except numerosNegativos as e:
    print(e)
except Exception as e:
    print(type(e).__name__)