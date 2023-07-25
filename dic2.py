#2. Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
# y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre>
# tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

dic ={
    "nombre": "",
    "edad": "",
    "direccion": "",
    "telefono": ""
}

dic["nombre"] = input("Ingrese su nombre: ")
dic["edad"] = input("Ingrese su edad: ")
dic["direccion"] = input("Ingrese su dirección: ")
dic["telefono"] = input("Ingrese su número de teléfono: ")

print(dic["nombre"] + " tiene " + dic["edad"] + " años, vive en " + dic["direccion"] + " y su número de teléfono es " + dic["telefono"])

