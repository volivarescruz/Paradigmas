package Java;

public class Circulo extends Figura {
    private double radius;

    public Circulo(String color, double radius) {
        super(color);
        this.radius = radius;
    }

    @Override
    public double perimetro() {
        return 2 * Math.PI * radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }
}

