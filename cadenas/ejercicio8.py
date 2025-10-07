euros = input("Dinero con decimales: ")
divide = euros.replace(".", ",").split(",")[0]
suelto = euros.replace(".", ",").split(",")[1]
print(f"Euros " + divide)
print(f"Centimos " + suelto)