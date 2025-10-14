Edad = int(input("¿Cual es tu edad? "))
Ingresos = int(input("¿Cual son tus ingresos mensuales? "))

if Edad > 16 and Ingresos > 1000 :
    print("Si tienes que tributar")
else:
    print("No tienes que tributar")