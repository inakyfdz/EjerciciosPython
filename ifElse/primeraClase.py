
a = int(input("Dime un numero: "))
b = int(input("Dime otro numero: "))
aPar = False
bPar = False
if a == b:
    print("El numero es igual")
else:
    if a > b:
        print(f"{a} > {b}")
    else:
        print(f"{b} > {a}")
    if a % 2 == 0:
        print(f"{a} es par")
        aPar = True
    else:
        print(f"{a} es impar")
    if b % 2 == 0:
        print(f"{b} es par")
        bPar = True
    else:
        print(f"{b} es impar")

if aPar and bPar:
    print(f"Los numeros {a} y {b} son pares")
elif aPar and not bPar:
    print( f"El numero {a} es par y el numero {b} es impar")
else :
    print("Que raro no es ni par ni par ninguno de los dos numeros")