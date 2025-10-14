nombre = input("Introduce el nombre del producto: ")
precio = float(input("Introduce el precio unitario: "))
unidades = int(input("Introduce el número de unidades: "))

total = precio * unidades


print(f"{nombre}: {precio:04.2f} euros {unidades:02d} unidades y el total: {total:05.2f} euros ")