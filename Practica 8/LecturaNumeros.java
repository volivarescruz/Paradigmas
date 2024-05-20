import java.io.*;

public class LecturaNumeros extends BufferedReader {
    
    // Constructor que prepara el objeto para lectura desde el teclado
    public LecturaNumeros() {
        super(new InputStreamReader(System.in));
    }
    
    // Constructor que recibe un Reader
    public LecturaNumeros(Reader r) {
        super(r);
    }
    
    // Método para leer un entero
    public int readInt() throws IOException {
        String line = readLine();
        return Integer.parseInt(line);
    }
    
    // Método para leer un entero con un mensaje
    public int readInt(String mensaje) throws IOException {
        System.out.print(mensaje);
        String line = readLine();
        return Integer.parseInt(line);
    }
    
    // Método para leer un Integer
    public Integer readInteger() throws IOException {
        String line = readLine();
        return Integer.valueOf(line);
    }
    
    // Método para leer un double
    public double readDouble() throws IOException {
        String line = readLine();
        return Double.parseDouble(line);
    }
    
    // Método para leer un double con un mensaje
    public double readDouble(String mensaje) throws IOException {
        System.out.print(mensaje);
        String line = readLine();
        return Double.parseDouble(line);
    }
}
