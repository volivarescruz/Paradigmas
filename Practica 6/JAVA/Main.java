import java.util.Scanner;

/*Olivares Cruz Victor Manuel Elaboraciòn en JAVA*/
public class Main
{
	public static void main(String[] args) {

	    System.out.println("Menú:");
            System.out.println("1. Círculo");
            System.out.println("2. Rectángulo");
            System.out.println("3. Triangulo");
            System.out.println("4. Cuadrado");
            System.out.print("Elige una opción: ");
        int diaSemana = new Scanner(System.in).nextInt();
        
        switch (diaSemana) {
            case 1:
                    System.out.print("Ingresa el radio del círculo: ");
            		double radio = new Scanner(System.in).nextDouble();
            		System.out.print("Ingresa el color del círculo: ");
            		String color = new Scanner(System.in).nextLine();
            		 
            		 
            		Circulo p1 = new Circulo(color, radio);
            		
                    System.out.println("\nÁrea: " + p1.getArea());
                    System.out.println("Perimetro: " + p1.getPerimetro());
                    System.out.println("Color: " + p1.getColor());
                break;
            case 2:
                    System.out.print("Ingresa el alto del Rectángulo: ");
            		double alto = new Scanner(System.in).nextDouble();
            		System.out.print("Ingresa el ancho del Rectángulo: ");
            		double ancho = new Scanner(System.in).nextDouble();
            		System.out.print("Ingresa el color del Rectángulo: ");
            		String color2 = new Scanner(System.in).nextLine();
            		 
            		 
            		Rectangulo p2 = new Rectangulo(color2, alto, ancho);
            		
                    System.out.println("\nÁrea: " + p2.getArea());
                    System.out.println("Perimetro: " + p2.getPerimetro());
                    System.out.println("Color: " + p2.getColor());
                break;
            case 3:
                    System.out.print("Ingresa el alto del Triangulo: ");
            		double alto2 = new Scanner(System.in).nextDouble();
            		System.out.print("Ingresa la base del Triangulo: ");
            		double base = new Scanner(System.in).nextDouble();
            		System.out.print("Ingresa el color del Triangulo: ");
            		String color3 = new Scanner(System.in).nextLine();
            		 
            		 
            		Triangulo p3 = new Triangulo(color3, alto2, base);
            		
                    System.out.println("\nÁrea: " + p3.getArea());
                    System.out.println("Perimetro: " + p3.getPerimetro());
                    System.out.println("Color: " + p3.getColor());
                break;
            case 4:
                    System.out.print("Ingresa el lado del Cuadrado: ");
            		double lado = new Scanner(System.in).nextDouble();
            		System.out.print("Ingresa el color del Triangulo: ");
            		String color4 = new Scanner(System.in).nextLine();
            		 
            		 
            		Cuadrado p4 = new Cuadrado(color4, lado);
            		
                    System.out.println("\nÁrea: " + p4.getArea());
                    System.out.println("Perimetro: " + p4.getPerimetro());
                    System.out.println("Color: " + p4.getColor());
                break;
            default:
                System.out.println("Número inválido. Debes ingresar un número del 1 al 4.");
        }
        

	    
	   
	}
}

 
 