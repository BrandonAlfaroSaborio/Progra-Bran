import random

numero = 0 


def numero_random():
    global numero
    numero = random.randint(0,100)

numero_random()

print(numero)