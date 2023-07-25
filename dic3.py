#3. Escribir un programa que guarde en un diccionario los precios de las verduras de la tabla, pregunte al usuario por una 
# verdura, un número de kilos y muestre por pantalla el precio a pagar.
# # Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
# Verdura               Precio (Kg)
# Brócoli                2500 COP
# Pimentón           1250 COP
# Arveja                 3500 COP


venta= {
    'brocoli': 2500,
    'pimenton': 1250,
    'arveja': 3500
}

verduras= input("que verdura desea comprar?:\n")

if verduras in venta:
    print(f"el precio de la verdura es: {venta[verduras]} COP")
    peso = int(input("cuantos kg desea comprar?:\n"))

    if peso in venta:
        print(f"el precio de la verdura es: {venta[verduras]} COP")
    pago_total = peso*venta[verduras]
    print(f"el total a pagar es: {pago_total} COP")
else:
    print("no tenemos esa verdura")
