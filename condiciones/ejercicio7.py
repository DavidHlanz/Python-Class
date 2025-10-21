renta = int(input("Cual es tu renta? "))
if (renta < 10000):
    print("Tu renta es 5%")
elif renta >10000 and renta <= 20000:
    print("Tu renta es 15%")
elif renta >20000 and renta <= 35000:
    print("Tu renta es 20%")
elif renta >35000 and renta <= 60000:
    print("Tu renta es 30%")
elif renta > 60000:
    print("Tu renta es 45%")



