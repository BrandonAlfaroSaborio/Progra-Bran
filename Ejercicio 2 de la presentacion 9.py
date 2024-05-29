'''
Cree una funcion que reciba una lista de numeros en punto flotante positivos
y retorne una lista con la raiz cuadrada de los mismos (utilice la funcion math.sqrt())

'''
import math

numeros=[]

for iteracion in range(0,5):
    pregunta=float(input("Digite un nemero en punto flotante: \n"))
    numeros.append(pregunta)


def raiz(lista):
    raices= []
    for num in lista:
        if num >= 0:
            raiz = math.sqrt(num)
            raices.append(raiz)
        
    return raices

"""
numeros_flotante=[14.5, 128.4, 400.76]
print(raiz(numeros_flotante))
"""

print(raiz(numeros))