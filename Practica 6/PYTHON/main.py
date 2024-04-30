from Hexagono import Hexagono
from Rombo import Rombo
from Trapecio import Trapecio

# Ejemplo de uso
p1 = Hexagono("rosa", 6, 5)
print("Area:", p1.getArea())
print("Perimetro:", p1.getPerimetro())
print("Color:", p1.getColor())

p2 = Rombo("rosa", 5, 8)
print("\nArea:", p2.getArea())
print("Perimetro:", p2.getPerimetro())
print("Color:", p2.getColor())

p3 = Trapecio("rosa", 8, 6, 4, 5)
print("\nArea:", p3.getArea())
print("Perimetro:", p3.getPerimetro())
print("Color:", p3.getColor())


