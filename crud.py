import os
def mostrar_cobros_pendientes(cobros):
    total_cobrado = sum(cobros.values())  
    total_pendiente = 0  
    print("==================================")
    print("Facturas pendientes de cobro:")
    for factura, importe in cobros.items():
        print(f"Factura {factura}: ${importe:.2f}")
        total_pendiente += importe 

    print(f"\nTotal cobrado hasta el momento: ${total_cobrado:.2f}")#round(factura, 2) apartir de 1 en adelante si tiene ceros va a mostrar un cero.
    print(f"Total pendiente de cobro: ${total_pendiente:.2f}\n")
    print("==================================")

cobros = {} 
def main():
    while True:
        print("==================================")
        print("¿Qué desea hacer?")
        print("1. Añadir una nueva factura")
        print("2. Pagar una factura existente")
        print("3. Terminar")
        print("==================================")
        opcion = int(input("Ingrese el número de opción: ")) 
        os.system("clear")
        if opcion == 1:  
            numero_factura = int(input("Ingrese el número de factura: "))
            if numero_factura in cobros:
                print("Ya existe una factura con este número de factura.")
            else:
                costo_factura = float(input("Ingrese el costo de la factura: "))
                cobros[numero_factura] = costo_factura
                mostrar_cobros_pendientes(cobros)
        elif opcion == 2:
            os.system("clear")
            if not cobros:
                print("No hay facturas pendientes de cobro.")
            else:
                numero_factura = input("Ingrese el número de factura a pagar: ")
                if numero_factura in cobros:
                    monto_pagado = cobros.pop(numero_factura)  
                    print(f"Factura {numero_factura} pagada: ${monto_pagado:.2f}")
                else:
                    print("El número de factura no existe en la lista de pendientes.")
                    mostrar_cobros_pendientes(cobros)  
        elif opcion == 3:  
            print("Terminando el programa...")
            break 

        else:  # Opción inválida
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()  
