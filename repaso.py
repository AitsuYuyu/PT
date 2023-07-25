# campus = {

# "Sputnik": {"activity": "classes", "students access": True, "schedule": "6 am to 10 pm", "capacity": 35},

# "Artemis": {"activity": "classes", "students access": True, "schedule": "6 am to 10 pm", "capacity": 30},

# "Apollo": {"activity": "classes", "students access": True, "schedule": "6 am to 10 pm", "capacity": 30},

# "Houston": {"activity": "teachers room", "students access": False, "schedule": "when teachers need", "capacity": 6},

# "Review": {"activity": "skills review", "students access": True, "schedule": "24/7", "capacity": 100}

# }
# Crea un menú (10 puntos) que se repita hasta que el usuario ingrese la opción de salida (a tu elección) y utilice una función para cada opción válida. 
# Las funcionalidades son:
# Mostrar a cuales espacios tienen acceso los campers (10 puntos)
# Mostrar como camper donde puedo estar, si NO es horario de clases (10 puntos) 
# Mostrar donde no puedo sentarme a estudiar nunca como camper (10 puntos)
# Mostrar el promedio de la capacidad de los espacios destinados a clase (10 puntos)
# Usar correctamente las excepciones (10 puntos) en este ejercicio.


    
import os
def opciones(num, dic):
    if num == 1:
        opcion1(dic)
    elif num == 2:
        opcion2(dic)
    elif num == 3:
        opcion3(dic)
    elif num == 4:
        opcion4(dic)
    elif num == 0:
        print("fin del programa!")
        os.system("clear")

# def opcion1 (campus):
#     for j in campus:
#         for info in campus[j]:

#             if info == "students access" and campus[j][info] == True:
#                 print(j)
                

def opcion1(campus):
    for clave, valor in campus.items():
        for info in valor:
            if info == "students access" and valor[info] == True:
                print(clave)

def opcion2(diccionario_campus):
    for clave, valor in diccionario_campus.items():
        for info in valor:
            if info == "schedule" and valor[info] == "24/7":
                print(clave)
                
def opcion3(set_camper):
    for clave, valor in set_camper.items():
        for info in valor:
            if info == "students access" and valor[info] == False:
                print(clave)
def opcion4(ca_camper):
    suma=0
    cont = 0
    for clave, valor in ca_camper.items():
        if valor["activity"] == "classes":
            cont = cont + 1  
            for clave1, valor1 in valor.items():
                if clave1 == "capacity":
                    suma = suma + valor1
                    

    print(suma/cont)
            
def menu():
    menu = ["1.Mostrar a cuales espacios tienen acceso los campers",
        "2.Mostrar como camper donde puedo estar, si NO es horario de clases",
        "3.Mostrar donde no puedo sentarme a estudiar nunca como camper ",
        "4.Mostrar el promedio de la capacidad de los espacios destinados a clase",
        "0.terminar programa"
        ]
    for i in menu:
        print(i)

campus = {

"Sputnik": {"activity": "classes", "students access": True, "schedule": "6 am to 10 pm", "capacity": 35},

"Artemis": {"activity": "classes", "students access": True, "schedule": "6 am to 10 pm", "capacity": 30},

"Apollo": {"activity": "classes", "students access": True, "schedule": "6 am to 10 pm", "capacity": 30},

"Houston": {"activity": "teachers room", "students access": False, "schedule": "when teachers need", "capacity": 6},

"Review": {"activity": "skills review", "students access": True, "schedule": "24/7", "capacity": 100},

"Espacio1": {"activity": "skills review", "students access": False, "schedule": "24/7", "capacity": 100}

}

try: 
    print("****************************************************")
    print("bienvenido a campusland!")
    menu()
    num = int(input("que seccion desea ver?:\n"))
    opciones(num,campus)

except Exception:
    # print(Exception)
    pass



