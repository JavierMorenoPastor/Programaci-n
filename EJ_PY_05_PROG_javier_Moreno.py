#Ejercicio 1
'''
#creo la lista
lista = list(range(10))
print(lista)


#defino la función que sumará 5 a cada número de la lista~
def sumar_5(numero):
    return numero + 5

#le aplico la suma a la lista mediante el comando map()
print("El resultado de la suma da: ")
suma_final = list(map(sumar_5, lista))
print(suma_final)
'''

#Ejercicio 2

Lista_Frases = ("rojo, azul, verde")

def mayusculas(Lista_Frases):
    return Lista_Frases.title()

Lista_Frases_Mayusculas = list(map(mayusculas, Lista_Frases))
print(Lista_Frases_Mayusculas)