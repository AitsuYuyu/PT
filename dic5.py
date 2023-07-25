#5. Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar 
# el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe
# mostrar por pantalla la lista de la compra y el coste total
print("********************************\n")
print("bienvenidos a la panaderia samsam")
dic={

    'pan':83,
    'tostadas':23,
    'especialidadSam':400
}
articulo = (input("que desea comprar?: \n"))
precio = int(input("el precio del articulo es: \n "))


dic["articulo"] = precio
print(f'el precio total es: {dic["articulo"]},precio')

