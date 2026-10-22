

for numero in range(81, 200):
    if numero % 7 != 0:
        continue
    print(f"El primer múltiplo de 7 mayor que 80 y menor que 200 es: {numero}")
    break
