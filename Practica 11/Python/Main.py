from abc import ABC, abstractmethod
from math import sqrt, pi

class Figure(ABC):
    @abstractmethod
    def get_color(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Triangle(Figure):
    def __init__(self, color, a, b, c):
        self.color = color
        self.a = a
        self.b = b
        self.c = c

    def get_color(self):
        return self.color

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

class Circle(Figure):
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius

    def get_color(self):
        return self.color

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * self.radius ** 2

class Rectangle(Figure):
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

    def get_color(self):
        return self.color

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

class Hexagon(Figure):
    def __init__(self, color, side_length):
        self.color = color
        self.side_length = side_length

    def get_color(self):
        return self.color

    def perimeter(self):
        return 6 * self.side_length

    def area(self):
        return (3 * sqrt(3) * self.side_length ** 2) / 2

# Demonstration of polymorphism
shapes = [
    Triangle("Red", 3, 4, 5),
    Circle("Blue", 2.5),
    Rectangle("Green", 4, 6),
    Hexagon("Yellow", 2)
]

for shape in shapes:
    print(f"Shape: {shape.__class__.__name__}, Color: {shape.get_color()}, Perimeter: {shape.perimeter()}, Area: {shape.area()}")
