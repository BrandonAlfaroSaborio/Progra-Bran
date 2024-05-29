'''
Suponga que cuenta con una lista de numeros . Escriba una funcion 
que cree y retorne una sublista con los indices de los numeros que
estan por debajo del parametro recibido.

'''

lista=[1,4,3,7,8,9,10]

numero = 10

def sub_lista(numero, lista):
    numero_retorno=[]
    for indice in range(0,len(lista)):             #repeticion representa el indice 
        if lista[indice] < numero:
            numero_retorno.append(indice)
             
    return numero_retorno

print("los indices de los numeros que estan por debajo del parametro recibido son: \n",sub_lista(numero, lista))
