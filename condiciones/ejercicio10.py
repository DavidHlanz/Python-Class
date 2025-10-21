tipo = input("¿Quieres una pizza vegetariana? (sí/no): ")

if tipo == "si":
    ingredientev = input("Elige un ingrediente (pimiento o tofu): ")
    print("Elegiste vegetariana con: " + ingredientev)
else:
    ingrediente = input("Elige un ingrediente (peperoni, jamón o salmón): ").lower()
    print("Elegiste no vegetariana con: " + ingrediente)


