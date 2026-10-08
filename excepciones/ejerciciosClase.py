

class numerosNegativos(Exception):
    def __init__(self, mensaje="Los numeros no pueden ser negativos" ):
        super().__init__(mensaje)
        self.mensaje = mensaje

try:
            #variables
    horasMaximasTrabajadasAntesExtra = int(input("Dime cuanto puedes trabajar antes de pagar horas extras?: "))#el de 40 horas

    horasTrabajadas = int(input("Cuanto has trabajo: "))
    pagoPorHora = float(input("Cuanto te pagan por hora: "))

    pagoPorHorasExtra = 0
    pagoNomal = 0
    pagoExtra = 0
    sueldoTotal = 0

            #operaciones
#comprobacion numeros negativos
    if horasMaximasTrabajadasAntesExtra <0 or horasTrabajadas <0 or pagoPorHora <0:
        raise numerosNegativos() #si ponemos un mensaje en el parentesis sacara este mensaje y no el pre programado
#horas trabajadas
    else :

        if horasTrabajadas >= horasMaximasTrabajadasAntesExtra : #miramos si las horas trabajadas no son negativas

            pagoPorHorasExtra = pagoPorHora * 1.5 #Cuanto pagan las horas extra

            print(f'El pago por hora extra es {pagoPorHorasExtra}')
                #calculamos pagos
            pagoNomal = pagoPorHora * horasMaximasTrabajadasAntesExtra
            pagoExtra = pagoPorHora * (horasTrabajadas -horasMaximasTrabajadasAntesExtra)
                #total del pago
            sueldoTotal = pagoExtra + pagoNomal
        else:
                #calculamos pagos
            pagoNomal = pagoPorHora * horasTrabajadas
            sueldoTotal = pagoNomal

        print(f'Tu pago total es: {sueldoTotal} por hora extra: {pagoExtra} y por pago normal es: {pagoNomal}')


except ValueError as e: #excepciones por valor (poner un String por ejemplo dara a error)
    print(f'que raro no has puesto ningun numero has puesto {e}')

except numerosNegativos as e:
    print(e) #va a sacar el mensaje

except Exception as e: print(type(e).__name__) #el resto de excepciones van aqui junto al nombre de la excepcion
# si es un Value Error saldra en la consola ValueError
