from Figura import Figura
import math

class Circulo(Figura):
    def __init__(self, color: str, radius: float):
        super().__init__(color)
        self.radius = radius
    
    def perimetro(self) -> float:
        return 2 * math.pi * self.radius
    
    def area(self) -> float:
        return math.pi * self.radius**2
