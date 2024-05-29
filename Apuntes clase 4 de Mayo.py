"""
Cree un funcion que reciba como parametro una lista de numeros,
e imprima los valores de esa lista que son divisibles entre 5

"""
lista=[]

for repeticion in range( 0,5):
    pregunta= int(input("Digite un numero entero:\n"))
    lista.append(pregunta)
    if pregunta == str():
        print("Esto definitivamente no es un numero entero")

print("Los numeros divisibles entre 5 que ud ingreso son:")

def numeros_divisibles (lista):
    for num in lista:
        if num % 5 ==0:
            print(num)

numeros_divisibles(lista)
