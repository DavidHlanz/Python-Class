capital=float(input("Cuanto dinero vas a meter: "))
interes=float(input("Tasa de interés: ")) / 100
tiempo=float(input("Tiempo en años: "))

simple = capital * interes * tiempo

print(f"El interés simple es: {simple}")