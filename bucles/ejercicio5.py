CantidadInvertir = int(input("Cuanto dinero a invertir: "))
Interes = int(input("Que interes anual %: "))
Años = int(input("A cuantos años: "))
defecto = 0


while Años > defecto:
    capital = CantidadInvertir * Interes * Años
    print(f"Año {Años}: {capital} €")
    Años -= 1
