/*Olivares Cruz Victor Manuel Elaboraciòn en JAVA*/

public class Cuadrado {
    private String color;
    private double lado;

    public Cuadrado(String color, double lado) {
        this.color = color;
        this.lado = lado;

    }

    // Getters y Setters
    public double getArea() {
        return lado*lado;
    }
    
    public double getPerimetro() {
        return lado*4;
    }
    
    public String getColor() {
        return color;
    }

}
