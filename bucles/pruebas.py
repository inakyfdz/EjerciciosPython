
def conWhile(numeroInicio):
    while numeroInicio >= 0:
        if numeroInicio == 0:
            print(numeroInicio)
        else:
            print(numeroInicio, end=",")
        numeroInicio -= 1

def conFor(numeroInicio):
    for i in range(numeroInicio, -1, -1):
        if i == 0:
            print(i)
        else:
            print(i, end=",")

try :
    numeroInicio = int(input("Dime un numero: "))
    conWhile(numeroInicio)
    conFor(numeroInicio)
except ValueError:
    print("Tiene que ser un numero")

except Exception as e:
    print(type(e).__name__)








