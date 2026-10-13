

# Errores personalizados
class numerosNegativos(Exception):
    def __init__(self, mensaje="Los numeros no pueden ser negativos" ):
        super().__init__(mensaje)
        self.mensaje = mensaje

class ErrorDivisa(Exception):
    pass

try:

    euros = float(input("Introduce la cantidad en euros: "))

    if euros <= 0:
        raise numerosNegativos


    divisa = input("Introduce la divisa (USD, GBP o JPY): ").upper()


    if divisa not in ["USD", "GBP", "JPY"]:
        raise ErrorDivisa("La divisa introducida no es valida.")


    if divisa == "USD":
        resultado = euros * 1.10
    elif divisa == "GBP":
        resultado = euros * 0.85
    else:
        resultado = euros * 160


    print(f"{euros} euros son {resultado:.2f} {divisa}.")

except ValueError:
    print("Error: debes introducir una cantidad numerica valida.")

except ErrorDivisa as e:
    print(f"Error: {e}")
except numerosNegativos as e:
    print (e)