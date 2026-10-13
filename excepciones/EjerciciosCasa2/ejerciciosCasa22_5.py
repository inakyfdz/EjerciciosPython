

class ErrorCalculadora(Exception):
    pass


class ErrorDivisionCero(Exception):
    pass


try:

    num1 = float(input("Introduce el primer numero: "))
    num2 = float(input("Introduce el segundo numero: "))


    operacion = input("Introduce la operacion (+, -, *, /): ")


    if operacion == "+":
        resultado = num1 + num2

    elif operacion == "-":
        resultado = num1 - num2

    elif operacion == "*":
        resultado = num1 * num2

    elif operacion == "/":

        if num2 == 0:
            raise ErrorDivisionCero("No se puede dividir entre cero.")

        resultado = num1 / num2

    else:

        raise ErrorCalculadora("La operacion introducida no es valida.")


    print(f"Resultado: {resultado}")

except ValueError:
    print("Error: debes introducir valores numericos validos.")

except ErrorDivisionCero as error:
    print(f"Error: {error}")

except ErrorCalculadora as error:
    print(f"Error: {error}")