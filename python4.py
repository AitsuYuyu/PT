edad = int(input("ingrese la edad"))

if edad <4:
    print("valor a pagar: ", 0)
elif edad >=4 and edad <= 18:
    print("valor a pagar: ", 5000)
elif edad >18:
    print("valor a pagar: ", 10000)
else:
    print("ingrese la edad!")



