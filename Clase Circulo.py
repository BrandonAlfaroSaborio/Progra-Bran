class Circulo:
   
    PI = 3.141592653589793

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        """Calcula el área del círculo usando la fórmula A = πr^2."""
        return Circulo.PI * (self.radio ** 2)

    def calcular_perimetro(self):
        """Calcula el perímetro del círculo usando la fórmula P = 2πr."""
        return 2 * Circulo.PI * self.radio

if __name__ == "__main__":
    radio = 5
    circulo = Circulo(radio)
    
    area = circulo.calcular_area()
    perimetro = circulo.calcular_perimetro()
    
    print(f"Radio del círculo: {radio}")
    print(f"Área del círculo: {area}")
    print(f"Perímetro del círculo: {perimetro}")
