class Hexagono:
    def __init__(self, color, lado, apotema):
        self.color = color
        self.lado = lado
        self.apotema = apotema


    # Getters y Setters
    def getArea(self):
        return ((self.lado*6)*self.apotema)/2
        
    def getPerimetro(self):
        return self.lado*6
        
    def getColor(self):
        return self.color
        