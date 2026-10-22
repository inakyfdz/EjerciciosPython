

try:
    notas = [4.5, 7, 9.25, 5, 3, 8, 6.5, 10, 2.75, 5.5]
    print("Notas:", notas)
    aprobados = 0
    for nota in notas:
        if nota >= 5:
            aprobados += 1

    media = sum(notas) / len(notas)

    print(f"Alumnos aprobados: {aprobados} de {len(notas)}")
    print(f"Nota media: {media:.2f}")
    print(f"Nota más alta: {max(notas)}")
    print(f"Nota más baja: {min(notas)}")
except ZeroDivisionError:
    print("Error: no hay notas ")
except TypeError:
    print("Error: Hay notas usando letras.")
