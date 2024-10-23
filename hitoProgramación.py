def area_cuadrado(lado):
    return lado * 2

def perimetro_cuadrado(lado):
    return lado * 4

def area_rectangulo(base, altura):
    return base * altura

def perimetro_rectangulo(base, altura):
    return 2*base + 2*altura

def cuadrado_asteriscos(lado):
    for i in range(lado):
        print(" * " * lado)

def rectangulo_asteriscos(base, altura):
    for i in range(altura):
        print(" * " * base)
   


print(" ***EJECUCIÓN INICIADA***")
print("MENU")
print("1-Cuadrado")
print("2-Rectángulo")
print("3-Salir")

numero = int(input("dime una opción: " ))
if numero == 1:
     lado = int(input("Dime el lado del cuadrado: "))
     print(cuadrado_asteriscos(lado))

     areacuadrado = area_cuadrado(lado)
     perimetrocuadrado = perimetro_cuadrado(lado)
     
     print("El área es", areacuadrado)
     print("El perímetro es", perimetrocuadrado)
    
elif numero == 2:
     base = int(input("Dime la base del rectángulo: "))
     altura = int(input("Dime la altura del rectángulo: "))
     print(rectangulo_asteriscos(base, altura))

     arearectangulo = area_rectangulo(base, altura)
     perimetrorectangulo = perimetro_rectangulo(base, altura)
     print("El área es", arearectangulo)
     print("El perímetro es", perimetrorectangulo)



elif numero == 3:
     print("Apagando...")
else: 
    print("Error, introduce un número válido")
