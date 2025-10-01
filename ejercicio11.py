interes= 0.04
deposito= float(input("Cantidad a añadir en la cuenta de ahorro: "))

PrimerAño= deposito * (1 + interes)
SegundoAño= PrimerAño * (1 + interes)
TercerAño = SegundoAño  * (1 + interes)



print(f"El primer año {round(PrimerAño, 2)}")
print(f"El segundo año {round(SegundoAño, 2)}")
print(f"El tercer año {round(TercerAño, 2)}")
