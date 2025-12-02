frase = input("Prueba una frase: ").lower()
letra = input("Elige una letra: ").lower()

for i in range(len(frase)):
    numero = frase.count(letra)
print(f"*{letra}* fue repetida {numero} veces")
