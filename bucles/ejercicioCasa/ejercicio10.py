

def leer_numero(mensaje, tipo):
    while True:
        try:
            valor = tipo(input(mensaje))

            if valor < 0:
                print("Error: el valor no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("Error: introduce un valor numérico válido.")
            continue


capital = leer_numero("Cantidad a invertir (€): ", float)
interes = leer_numero("Interés anual (%): ", float)
años = leer_numero("Número de años: ", int)

for años in range(1, años + 1):
    capital = capital * (1 + interes / 100)
    print(f"Año {años}: {capital:.2f} €") ##bloquea los digitos a 2