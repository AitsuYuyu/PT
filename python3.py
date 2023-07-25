saldo = 2400
puntuacion =float(input("ingrese la puntuacion del empleado"))

if puntuacion == 0.0:
    print("es inaceptable su puntuacion")
    print("saldo es: ", saldo)
elif puntuacion == 0.4:
    print("es aceptable su puntuacion")
    saldo += saldo*puntuacion
    print("saldo es: ",saldo)
elif puntuacion >=0.6:
    print("es meritorio su puntaje")
    saldo += saldo*puntuacion
    print("saldo es: ",saldo)
else:
    print("es invalido su puntaje!")



