edad = int(input("Edad?"))
if(edad < 4):
    print("Gratis!")
elif edad >=4 and edad <= 18:
    print("5€")
elif edad > 18:
    print("10€")
