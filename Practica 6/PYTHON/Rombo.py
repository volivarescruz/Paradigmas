class Rombo:
    def __init__(self, color, lado, Diametro):
        self.color = color
        self.lado = lado
        self.Diametro = Diametro


    # Getters y Setters
    def getArea(self):
        return ((self.Diametro/2)*self.Diametro)/2
        
    def getPerimetro(self):
        return self.lado*4
        
    def getColor(self):
        return self.color
        