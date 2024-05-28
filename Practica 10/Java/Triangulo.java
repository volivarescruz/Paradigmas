package Java;

public class Triangulo extends Figura {
    private double base, height, side1, side2;

    public Triangulo(String color, double base, double height, double side1, double side2) {
        super(color);
        this.base = base;
        this.height = height;
        this.side1 = side1;
        this.side2 = side2;
    }

    @Override
    public double perimetro() {
        return base + side1 + side2;
    }

    @Override
    public double area() {
        return 0.5 * base * height;
    }
}