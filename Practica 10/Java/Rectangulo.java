package Java;

public class Rectangulo extends Figura {
    private double width, height;

    public Rectangulo(String color, double width, double height) {
        super(color);
        this.width = width;
        this.height = height;
    }

    @Override
    public double perimetro() {
        return 2 * (width + height);
    }

    @Override
    public double area() {
        return width * height;
    }
}