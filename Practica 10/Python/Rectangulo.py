from Figura import Figura

class Rectangulo(Figura):
    def __init__(self, color: str, width: float, height: float):
        super().__init__(color)
        self.width = width
        self.height = height
    
    def perimetro(self) -> float:
        return 2 * (self.width + self.height)
    
    def area(self) -> float:
        return self.width * self.height
