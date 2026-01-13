asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

repetir = []

for materia in asignaturas:
    nota = float(input("Nota de " + materia + "? "))
    
    if nota < 5:
        repetir.append(materia)

if len(repetir) > 0:
    print("Tienes que repetir estas asignaturas:")
    for materia in repetir:
        print(materia)
else:
    print("Has aprobado todo.")