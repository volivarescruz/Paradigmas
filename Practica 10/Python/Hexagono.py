from Figura import Figura
import math

class Hexagono(Figura):
    def __init__(self, color: str, side: float):
        super().__init__(color)
        self.side = side
    
    def perimetro(self) -> float:
        return 6 * self.side
    
    def area(self) -> float:
        return (3 * math.sqrt(3) * self.side**2) / 2
