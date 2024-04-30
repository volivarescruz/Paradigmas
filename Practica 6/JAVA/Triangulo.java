/*Olivares Cruz Victor Manuel Elaboraciòn en JAVA*/

public class Triangulo {
    private String color;
    private double alto;
    private double base;

    public Triangulo(String color, double alto, double base) {
        this.color = color;
        this.alto = alto;
        this.base = base;
    }

    // Getters y Setters
    public double getArea() {
        return (alto*base)/2;
    }
    
    public double getPerimetro() {
        return (alto*2)+base;
    }
    
    public String getColor() {
        return color;
    }

}
