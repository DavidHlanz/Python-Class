numero = int(input("Escribe numero entero: "))
for i in range(1, numero +1, 2):
    print()
    for j in range(i, 0, -2):
        print(j, end=" ")
        