/*Olivares Cruz Victor Manuel Elaboraciòn en JAVA*/

public class Circulo {
    private String color;
    private double radio;

    public Circulo(String color, double radio) {
        this.color = color;
        this.radio = radio;
    }

    // Getters y Setters
    public double getArea() {
        return 3.1416*(radio*radio);
    }
    
    public double getPerimetro() {
        return 3.1416*(radio*2);
    }
    
    public String getColor() {
        return color;
    }

}
