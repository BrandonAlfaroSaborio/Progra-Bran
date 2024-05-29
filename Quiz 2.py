
lista=[]

pregunta=int(input("escriba un numero entre 1-10:\n"))
suma=0

if (pregunta  > 0 and pregunta < 11):
      while pregunta !=0:
        if (pregunta  > 0 and pregunta < 11):
            lista.append(pregunta)
            pregunta=int(input("escriba un numero entre 1-10:\n"))
            if (pregunta >11):
                 print("Numero no valido")

for repeticion in range (0, len(lista)):
    suma+=lista[repeticion]

print(suma)