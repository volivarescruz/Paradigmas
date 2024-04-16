/*Olivares Cruz Victor Manuel Elaboraciòn en JAVA*/
public class Main
{
	public static void main(String[] args) {
		Persona p1 = new Persona("Victor Olivares", 19, "Masculino", "Calle Mon", "1234567890", "CDMX",
                "Ingeniero", "Soltero", "Mexicana", "victormanuelolivarescruz@example.com");
        System.out.println("Nombre: " + p1.getNombre());
        System.out.println("Edad: " + p1.getEdad());
        System.out.println("Género: " + p1.getGenero());
        System.out.println("Dirección: " + p1.getDireccion());
        System.out.println("Teléfono: " + p1.getTelefono());
        System.out.println("Ciudad: " + p1.getCiudad());
        System.out.println("Profesión: " + p1.getProfesion());
        System.out.println("Estado Civil: " + p1.getEstadoCivil());
        System.out.println("Nacionalidad: " + p1.getNacionalidad());
        System.out.println("Email: " + p1.getEmail());
	}
}

 
 