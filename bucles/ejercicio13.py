print("Eco, usa 'salir' para acabar")
entrada = ""
while entrada.lower() != "salir":
    entrada = input("Tu: ")
    if entrada.lower() == "salir":
        print("Finalizado")
    else:
        print(f"Eco: {entrada}")