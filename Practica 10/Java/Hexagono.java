package Java;

public class Hexagono extends Figura {
    private double side;

    public Hexagono(String color, double side) {
        super(color);
        this.side = side;
    }

    @Override
    public double perimetro() {
        return 6 * side;
    }

    @Override
    public double area() {
        return (3 * Math.sqrt(3) * side * side) / 2;
    }
}
