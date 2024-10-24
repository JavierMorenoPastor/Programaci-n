saldo = float(input("Escribe tu saldo bancario: "))

while saldo <=0:
    print("El saldo no puede ser 0")
    saldo = input("Ingresa un saldo válido: ")
    break
  
print("Elige la opción que quieras realizar: ")
print("1-Ingresar dinero")
print("2-Retirar dinero")
print("3-Mostrar saldo")
print("4-Salir")

while True:
    numero = int(input("Elige una opción: "))

    if numero == 1:
        suma = float(input("¿Cuanto dinero deseas ingresar?: "))
        saldo = suma + saldo
        print("su saldo es de: " , saldo)
        while saldo <= 0:
            print("No puedes ingresar cantidades negativas")
            ingreso = float(input("ingresa la cantidad de nuevo: "))
            break
        print("Elige la opción que quieras realizar: ")
        print("1-Ingresar dinero")
        print("2-Retirar dinero")
        print("3-Mostrar saldo")
        print("4-Salir")

        

    elif numero == 2:
        resta = float(input("¿Cuanto dinero deseas retirar?: "))
        saldo =saldo - resta
        print("su saldo es de: " , saldo)
        while saldo <= 0:
            print("No puedes retirar dinero si tu saldo es menor o igual a 0, por favor ingrese dinero antes")
            resta = float(input("¿Cuanto dinero deseas retirar?: "))
            break
        print("Elige la opción que quieras realizar: ")
        print("1-Ingresar dinero")
        print("2-Retirar dinero")
        print("3-Mostrar saldo")
        print("4-Salir")


    elif numero == 3:
        print("Su saldo bancario es: ", saldo ,"€" )
        print("Elige la opción que quieras realizar: ")
        print("1-Ingresar dinero")
        print("2-Retirar dinero")
        print("3-Mostrar saldo")
        print("4-Salir")


    elif numero == 4:
        print("Apagando...")
        break

    else:
        print("Ingresa un número válido")
        print("Elige la opción que quieras realizar: ")
        print("1-Ingresar dinero")
        print("2-Retirar dinero")
        print("3-Mostrar saldo")
        print("4-Salir")


    

