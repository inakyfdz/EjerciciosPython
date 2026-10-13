class ErrorCajero(Exception):
    pass


try:

    saldo = float(input("Introduce el saldo inicial: "))


    if saldo <= 0:
        raise ErrorCajero("El saldo debe ser mayor que cero.")


    cantidad = float(input("Introduce la cantidad a retirar: "))


    if cantidad <= 0:
        raise ErrorCajero("La cantidad a retirar debe ser mayor que cero.")


    if cantidad > saldo:
        raise ErrorCajero("No hay suficiente saldo para realizar la retirada.")


    saldo -= cantidad


    print("Retirada realizada correctamente.")
    print(f"Saldo restante: {saldo:.2f} euros.")

except ValueError:
    print("Error: debes introducir una cantidad numerica valida.")

except ErrorCajero as error:
    print(f"Error: {error}")