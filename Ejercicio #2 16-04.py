lista=[]

condicion= 0

#Lo que no ocupo que pase va dentro del while para que cuando pase termine el ciclo

while (condicion != "x"):
    pregunta= input("Digite cualquier palabra que no sea la letra x: \n")
    if pregunta != "x":
        lista.append(pregunta)
    condicion=pregunta

print(lista)



