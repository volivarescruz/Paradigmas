class Trapecio:
    def __init__(self, color, Bmayor, Bmenor, altura, lado):
        self.color = color
        self.Bmayor = Bmayor
        self.Bmenor = Bmenor
        self.altura = altura
        self.lado = lado


    # Getters y Setters
    def getArea(self):
        return ((self.Bmayor+self.Bmenor)/2)*self.altura
        
    def getPerimetro(self):
        return (self.Bmayor+self.Bmenor)+2*self.lado
        
    def getColor(self):
        return self.color
        