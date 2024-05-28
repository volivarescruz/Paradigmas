from Triangulo import Triangulo
from Circulo import Circulo
from Rectangulo import Rectangulo
from Hexagono import Hexagono

def main():
    figures = [
        Triangulo("Rojo", 3, 4, 3, 4),
        Circulo("Azul", 5),
        Rectangulo("Verde", 4, 6),
        Hexagono("Amarillo", 2)
    ]

    for Figura in figures:
        print(f"Color: {Figura.getColor()}, Perímetro: {Figura.perimetro()}, Área: {Figura.area()}")

if __name__ == "__main__":
    main()
