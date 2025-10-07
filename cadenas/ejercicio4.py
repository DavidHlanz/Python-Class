telefono = input("Escribe tu número de telefono en este formato +34-xxxxxxxxxx-xx: ")
divide = telefono.split("-")
numero  = divide[1]

print(f"Tu número sin prefijo ni extension es {numero}")