package Java;

public class Main {
    public static void main(String[] args) {
        Figura[] figures = {
            new Triangulo("Rojo", 3, 4, 3, 4),
            new Circulo("Azul", 5),
            new Rectangulo("Verde", 4, 6),
            new Hexagono("Amarillo", 2)
        };

        for (Figura figure : figures) {
            System.out.println("Color: " + figure.getColor() + ", Perímetro: " + figure.perimetro() + ", Área: " + figure.area());
        }
    }
}
