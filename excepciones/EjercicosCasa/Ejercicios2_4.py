
try:

    clave_ingresada = input("Introduce la clave de acceso: ")


    if clave_ingresada == "python123":
        print("Acceso concedido")
    else:
        print("Acceso denegado")

except KeyboardInterrupt: #fuerza el parar
    print("Programa interrumpido por el usuario.")
except ValueError as e:
    print("Error hay que poner un array")
except Exception as e:
    print(f"Ocurrió un error inesperado: {type(e).__name__}")