import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try {
            LecturaNumeros ln = new LecturaNumeros();

            // Leer y desplegar 2 enteros
            int num1 = ln.readInt("Introduce el primer número entero: ");
            int num2 = ln.readInt("Introduce el segundo número entero: ");
            System.out.println("Primer número entero: " + num1);
            System.out.println("Segundo número entero: " + num2);

            // Leer y desplegar 1 Integer
            System.out.print("Introduce el tercer número entero (Integer): ");
            Integer num3 = ln.readInteger();
            System.out.println("Número entero (Integer): " + num3);

            // Leer y desplegar 1 double
            double num4 = ln.readDouble("Introduce el primer número double: ");
            System.out.println("Primer número double: " + num4);

            // Leer y desplegar 1 Double
            double num5 = ln.readDouble("Introduce el segundo número double: ");
            Double num5Double = num5;  // Boxing para convertir de double a Double
            System.out.println("Segundo número double (Double): " + num5Double);

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
