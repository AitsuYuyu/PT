#1. Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
dic ={ "euro":"€",
    'dollar':"$",
    'yen': "¥"
}

divisa =(input("ingrese una palabra:\n "))
if divisa in dic:
    print("el valor esta en la lista")
else: 
    print("el valor no esta en la lista")
