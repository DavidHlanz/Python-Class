payaso=int(112)
muñeca=int(75)
PayasosVendidos=int(input("¿Cuántos payasos vendidos?"))
MuñecasVendidas=int(input("¿Cuántas muñecas vendidas"))

VentaFinal=int(payaso*PayasosVendidos) + int(muñeca*MuñecasVendidas)

print(f"Hay un peso total del paquete de {VentaFinal} gramos")