fecha = input("Introduce una fecha con el formato dd/mm/aaaa: ")
dividir = fecha.split("/")

print(f"Dia: " + dividir[0])
print(f"Mes: " + dividir[1])
print(f"Año: " + dividir[2])