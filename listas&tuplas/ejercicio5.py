numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros.reverse()

resultado = ""

for n in numeros:
    if n == 1:
        resultado = resultado + str(n)
    else:
        resultado = resultado + str(n) + ", "
        
print(resultado)