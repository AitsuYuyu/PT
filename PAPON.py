def repetirfrase(frase, veces):
    for _ in range(veces):
        print(frase)

while True:
    try:
        cantidad = int(input("Ingrese la cantidad de veces que quiere repetir la frase: "))
        repetirfrase("Claudia la más papona", cantidad)
        break
    except ValueError:
        print("Por favor, ingrese un número válido.")
        