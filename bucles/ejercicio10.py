entero = int(input("Numero entero "))
for i in range(1,entero+1):
    if entero % i == 0 and i != entero and i !=1:
        print(f"{entero} no es primo")
        exit(0)
print(f"{entero} es primo")