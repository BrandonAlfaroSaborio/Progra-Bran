
class Persona():
    def __init__(self, nombre, cedula, edad, correo):
        self.nombre = nombre
        self.cedula=cedula
        self.edad = edad
        self.correo= correo 
    
personas = []
while True:
    nombre = input("Ingrese el nombre: ")
    cedula = input("Ingrese la cédula: ")
    edad = input("Ingrese la edad: ")
    correo = input("Ingrese el correo electrónico: ")

    persona = Persona(nombre, cedula, edad, correo)
    personas.append(persona)

    pregunta = input("¿Desea ingresar otra persona?: \n")
    if pregunta != 'si':
        break
    
for imprimir in personas:
    print("Cédula:", imprimir.cedula + ",", "Nombre:", imprimir.nombre + ",", "Edad:", str(imprimir.edad) + ",", "Correo:", imprimir.correo)

