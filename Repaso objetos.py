class Pajaro:
    def __init__(self,color, especie, subespecie, envergadura, forma_del_pico, cantidad_plumas):
        self.color= color
        self.especie= especie
        self.subespecie= subespecie
        self.envergadura= envergadura
        self.forma_del_pico= forma_del_pico
        self.cantidad_plumas= cantidad_plumas 

    def crecimiento(self, nueava_envergadura, nueva_cantidad_plumas, nuevo_color):
        self.nueva_envergadura = nueava_envergadura
        self.nueva_cantidad_plumas= nueva_cantidad_plumas
        self.nuevo_color= nuevo_color

#Convierte a strings 
    def descripcion(self):
	    print("Color: %s\nForma Pico: %s\nEspecie: %s\nSubespecie: %s\nEnvergadura: %f\nCantidad Plumas: %i" % (self.color, self.forma_del_pico, self.especie, self.subespecie, self.envergadura, self.cantidad_plumas))

#Self NUNCA se envia como parametro
pajarito1=Pajaro("blanco", "traupis episcopus", "viudita", 10.2,"puntiagudo", 89)
pajarito2=Pajaro("negro", "zanate", "idk", 19.2, "redondo",199)

pajarito1.descripcion()
print("------------------------")
pajarito2.descripcion()
pajarito1.crecimiento(10.6, 90, "azulejo")
print("------POST CRECIMIENTO P1------")
pajarito1.descripcion()

