
class numerosNegativos(Exception):
    def __init__(self, mensaje="Los numeros no pueden ser negativos" ):
        super().__init__(mensaje)
        self.mensaje = mensaje



while True:
    try:
        nota = float(input("¿Qué nota has sacado? "))
        if nota < 0 : raise numerosNegativos
        match nota:
            case x if x < 5:
                print("Suspenso")
            case x if 7 > x >= 5:
                print("Aprobado")
            case x if 9 > x >= 7:
                print("Notable")
            case x if 10 >= x >= 9:
                print("Sobresaliente")
            case _:
                print("Valor invalido")
    except numerosNegativos as e:
        print(e)

    except ValueError:
        print("Esto no es un error")
    except Exception as e:
        print(type(e).__name__)


        ###no es mi ejercicio pero este esta modificado:
        #try:
            #edad = int(input("Introduce la edad: "))

            #if edad < 0:
                #raise ValueError("La edad no puede ser negativa")


        #except ValueError as e:

            #print(
                #"Error: Debes introducir un número entero válido." if "invalid literal" in str(e) or not str(e) else e
            #)


        #else:
            #if edad >= 18:
                #print("Es mayor de edad")
            #else:
                #print("Es menor de edad")