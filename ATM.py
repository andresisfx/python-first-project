


def main():
    saldo = 0

    while True:
        print("1. Consultar saldo")
        print("2. Retirar dinero")
        print("3. Depositar dinero")
        print("4. Salir")
        opcion = input("Ingrese el número de la opción que desea realizar: ")
        

        if opcion == '1':
            print(f"Saldo actual es: {saldo} pesos")
            break
        elif opcion == '2':
            cantidad = float(input("Ingrese la cantidad que desea retirar: "))
            saldo-=cantidad
            print(f"usted retiró {cantidad} su saldo actual es {saldo}")
            break
        elif opcion == '3':
            cantidad = float(input("Ingrese la cantidad que desea depositar: "))
            saldo+=cantidad
            print(f"usted depositó {cantidad} su saldo actual es {saldo}")
            
        elif opcion == '4':
            print("Gracias por utilizar el cajero automático. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")
        


if __name__ == "__main__":
    main()




