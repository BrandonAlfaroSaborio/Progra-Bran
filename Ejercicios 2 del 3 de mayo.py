'''
Escriba una funcion que reciba como paramatro una lista
y retorne la lista sin duplicados

'''


lista= [1,2,3,4,5,5,6,6,7,8,9]

def sin_duplicados (lista):
    lista_no_duplicados=[]
    for repeticion in lista:
        if repeticion not in lista_no_duplicados:
            lista_no_duplicados.append(repeticion)
    return lista_no_duplicados

print(sin_duplicados(lista))
        
   