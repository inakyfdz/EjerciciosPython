

        # 1. Variables globales
nombre = "Sin nombre"
edad = 0




        # 2. Simulación
eleccion = 0

try:
    while True:  #

        print('Que quieres seleccionar:'
              ' 1. Ver perfil'
              ' 2. Editar perfil'
              ' 3. Salir')
        eleccion = int(input())

        match eleccion:
            case 1:
                mostrarPerfil()
            case 2:
                editarPerfil()
            case 3:
                print('Saliendo')
            case _:
                print('numero invalido')


        if not (eleccion != 3):
            break

except ValueError:
    print('Eso no era un numero')
except Exception as e:
    print(type(e).__name__)


        # 3. Funciones
    def mostrarPerfil():
        print(f"\nNombre: {nombre}")
        print(f"Edad: {edad}\n")


    def editarPerfil():
        global nombre, edad
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
