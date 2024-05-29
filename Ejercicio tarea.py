"""
Cree un programa en python que solicite e ingrese en una lista numeros de punto flotante 
hasta que se ingrese un 0 se deben reportar todas las entradas en orden con su respectivo indice
y reportar el resultado de multiplicar todas las entradas de la lista.

"""

lista=[]

multiplicacion =1

pregunta= -1

while(pregunta != 0):
    pregunta= float(input("Ingrese numeros en punto flotante(Con decimales): \n"))
    if pregunta != 0:
        lista.append(pregunta)

for numero in lista:
    indice= lista.index(numero)
    print("El número en el índice", indice, "es:", numero)

#tambien se hace con:
#for index,num in enumerate(lista):
       # print("El número en el índice", index, "es:", num)

for repeticion in lista:
    multiplicacion *= repeticion

print("El resultado de los inputs multiplicados es:" ,multiplicacion)

    


