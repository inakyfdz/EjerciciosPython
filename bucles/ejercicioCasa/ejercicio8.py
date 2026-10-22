try:
    num = int(input("Introduce un número : "))
    if num < 2:
        raise ValueError
except ValueError:
    print("Error: debes introducir un número entero mayor o igual que 2.")
else:
    primos = []
    for numero in range(2, num + 1):
        es_primo = True
        divisor = 2
        while divisor * divisor <= numero:
            if numero % divisor == 0:
                es_primo = False
                break
            divisor += 1
        if es_primo:
            primos.append(numero)
    print(f"Primos hasta {num}:", primos)
