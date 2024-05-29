suma=0
while(101>suma):
    pregunta=int(input("escriba un numero entre 1-10: \n"))
    if(pregunta < 11 and pregunta > 0):
        suma += pregunta
    
    else: 
        print("numero invalido")

print(suma)