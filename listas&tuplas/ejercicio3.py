asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []



for i in asignaturas:
    nota = input(f"Que has sacado en {i} ")
    notas.append(nota)

for i in range(len(notas)):
    print(f"Ha sacado {notas[i]} en {asignaturas[i]}")