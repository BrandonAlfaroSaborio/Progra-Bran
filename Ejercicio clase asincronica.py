"""
-Se cuenta con una "lista" de datos que esta guardada en la posicion de memoria 0xE0, la cantidad
de datos que tiene la lista se encuentra en la posicion 0xDF

-Cree un programa que recorra toda la lista y sume el total de valores de cada entrada de la lista

-El resultado de la suma de todos los valores de la lista debe de multiplicarlo por el valor guardado
en la posicion 0xD0

-Si este valor es igual al valor 40 (en decimal) debe de guardar el resultado en la misma posicion 0xD0, 
si no es igual a 40 debe de guardarlo en la posicion 0xD2

"""

lista=[10.0, 9.5, 10.5, 10.0]
suma=0
valor_guardado= 2

for recorrido in lista:
    suma += recorrido

print("La suma de los valores de cada entrada de la lista es: \n",suma)

suma *= valor_guardado
print("La multiplicacion del resultado de la suma por el valor guardado es: \n",suma)
