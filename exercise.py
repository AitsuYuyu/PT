lista =["matematicas:","fisica:","quimica:","historia:","lengua:"]
nota = int(input("ingrese las notas de las materias:\n "+ str(lista[0])))

while nota >50 and nota <=-1:
    print("ERROR! ingrese una nota valida!")
    intento = float(input("reintentelo:"))
nota2 = int(input("ingrese la nota de la materia:\n "+str(lista[1])))
intento = float(input("reintentelo:"))
if nota >50 and nota <=-1:
    print("ERROR! ingrese una nota valida!")
    print(intento)
nota3 = int(input("ingrese la nota de la materia:\n"+str(lista[2])))
intento = float(input("reintentelo:"))
if nota >50 and nota <=-1:
    print("ERROR! ingrese una nota valida!")
    print(intento)
nota4 = int(input("ingrese la nota de la materia:\n"+str(lista[3])))
intento = float(input("reintentelo:"))
if nota >50 and nota <=-1:
    print("ERROR! ingrese una nota valida!")
    print(intento)
nota5 = int(input("ingrese la nota de la materia:\n"+ str(lista[4])))
intento = float(input("reintentelo:"))
if nota >50 and nota <=-1:
    print("ERROR! ingrese una nota valida!")
print(intento)

cuenta = [0]
for i in lista:
    print(f"la nota de su{lista[i]} es: {nota[0]}")
