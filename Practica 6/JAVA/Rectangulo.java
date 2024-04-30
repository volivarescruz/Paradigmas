/*Olivares Cruz Victor Manuel Elaboraciòn en JAVA*/

public class Rectangulo {
    private String color;
    private double alto;
    private double ancho;

    public Rectangulo(String color, double alto, double ancho) {
        this.color = color;
        this.alto = alto;
        this.ancho = ancho;
    }

    // Getters y Setters
    public double getArea() {
        return alto*ancho;
    }
    
    public double getPerimetro() {
        return (alto*2)+(ancho*2);
    }
    
    public String getColor() {
        return color;
    }

}
