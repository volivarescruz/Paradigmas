from Figura import Figura

class Triangulo(Figura):
    def __init__(self, color: str, base: float, height: float, side1: float, side2: float):
        super().__init__(color)
        self.base = base
        self.height = height
        self.side1 = side1
        self.side2 = side2
    
    def perimetro(self) -> float:
        return self.base + self.side1 + self.side2
    
    def area(self) -> float:
        return 0.5 * self.base * self.height
