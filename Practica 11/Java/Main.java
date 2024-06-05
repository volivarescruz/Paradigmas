package Java;

interface Figure {
    String getColor();
    double perimeter();
    double area();
}

class Triangle implements Figure {
    private String color;
    private double a, b, c;

    public Triangle(String color, double a, double b, double c) {
        this.color = color;
        this.a = a;
        this.b = b;
        this.c = c;
    }

    @Override
    public String getColor() {
        return color;
    }

    @Override
    public double perimeter() {
        return a + b + c;
    }

    @Override
    public double area() {
        double s = perimeter() / 2;
        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }
}

class Circle implements Figure {
    private String color;
    private double radius;

    public Circle(String color, double radius) {
        this.color = color;
        this.radius = radius;
    }

    @Override
    public String getColor() {
        return color;
    }

    @Override
    public double perimeter() {
        return 2 * Math.PI * radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}

class Rectangle implements Figure {
    private String color;
    private double width, height;

    public Rectangle(String color, double width, double height) {
        this.color = color;
        this.width = width;
        this.height = height;
    }

    @Override
    public String getColor() {
        return color;
    }

    @Override
    public double perimeter() {
        return 2 * (width + height);
    }

    @Override
    public double area() {
        return width * height;
    }
}

class Hexagon implements Figure {
    private String color;
    private double sideLength;

    public Hexagon(String color, double sideLength) {
        this.color = color;
        this.sideLength = sideLength;
    }

    @Override
    public String getColor() {
        return color;
    }

    @Override
    public double perimeter() {
        return 6 * sideLength;
    }

    @Override
    public double area() {
        return (3 * Math.sqrt(3) * sideLength * sideLength) / 2;
    }
}

public class Main {
    public static void main(String[] args) {
        Figure[] shapes = {
            new Triangle("Red", 3, 4, 5),
            new Circle("Blue", 2.5),
            new Rectangle("Green", 4, 6),
            new Hexagon("Yellow", 2)
        };

        for (Figure shape : shapes) {
            System.out.println("Shape: " + shape.getClass().getSimpleName() +
                               ", Color: " + shape.getColor() +
                               ", Perimeter: " + shape.perimeter() +
                               ", Area: " + shape.area());
        }
    }
}
