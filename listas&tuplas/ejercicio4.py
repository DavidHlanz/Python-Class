lista = []
i = 5
x = 0

while i >= x:
    numero = int(input("Numero de la loteria: "))
    lista.append(numero)
    x += 1

lista.sort() 
print(lista)