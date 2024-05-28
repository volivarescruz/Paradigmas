from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, color: str):
        self.color = color
    
    def getColor(self) -> str:
        return self.color
    
    @abstractmethod
    def perimetro(self) -> float:
        pass
    
    @abstractmethod
    def area(self) -> float:
        pass
