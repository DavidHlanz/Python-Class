BarraNoDia= int(input("Cuantas barras no se han vendido hoy: "))
PrecioInicial= 3.49
Descuento = 0.6
BarraDescuento= PrecioInicial * Descuento
DescuentoPorcentaje = int(Descuento  * 100)
print(f"El precio habitual de la barra es de {PrecioInicial}€")
print(f"El descuento que se hace es del {DescuentoPorcentaje}% ")
print(f"El coste final de la barra que no es de hoy: {BarraDescuento:.2f}€")