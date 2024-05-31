class Pajaro:
    def __init__(self,color, especie, subespecie, envergadura, forma_del_pico, cantidad_plumas):
        self.color= color
        self.especie= especie
        self.subespecie= subespecie
        self.envergadura= envergadura
        self.forma_del_pico= forma_del_pico
        self.cantidad_plumas= cantidad_plumas 

    def crecimineto(self, nueava_envergadura, nueva_cantidad_plumas, nuevo_color):
        self.nueva_envergadura = nueava_envergadura
        self.nueva_cantidad_plumas= nueva_cantidad_plumas
        self.nuevo_color= nuevo_color

    def descripcion (self):
        print("Color")

#Self NUNCA se envia como parametro
pajarito1=Pajaro("blanco", "traupis episcopus", "viudita", 10.2,"puntiagudo", 89)
pajarito2=Pajaro("negro", "zanate", "idk", 19.2, "redondo",199)

pajarito1.descripcion()
pajarito2.descripcion()
pajarito1.crecimineto(10.6,90, "azulejo")
pajarito1.descripcion()
