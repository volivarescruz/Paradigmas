using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Calculadora Funcional");
        while (true)
        {
            Console.WriteLine("Elija una operación:");
            Console.WriteLine("1. Suma");
            Console.WriteLine("2. Resta");
            Console.WriteLine("3. Multiplicación");
            Console.WriteLine("4. División");
            Console.WriteLine("5. Exponenciación");
            Console.WriteLine("6. Raíz Cuadrada");
            Console.WriteLine("7. Valor Absoluto");
            Console.WriteLine("8. Máximo");
            Console.WriteLine("9. Mínimo");
            Console.WriteLine("10. Redondeo");
            Console.WriteLine("0. Salir");

            int opcion = Convert.ToInt32(Console.ReadLine());

            if (opcion == 0)
            {
                break;
            }

            Func<double, double, double> operacionBinaria = null;
            Func<double, double> operacionUnaria = null;

            switch (opcion)
            {
                case 1:
                    operacionBinaria = Suma;
                    break;
                case 2:
                    operacionBinaria = Resta;
                    break;
                case 3:
                    operacionBinaria = Multiplicacion;
                    break;
                case 4:
                    operacionBinaria = Division;
                    break;
                case 5:
                    operacionBinaria = Exponenciacion;
                    break;
                case 6:
                    operacionUnaria = RaizCuadrada;
                    break;
                case 7:
                    operacionUnaria = ValorAbsoluto;
                    break;
                case 8:
                    operacionBinaria = Maximo;
                    break;
                case 9:
                    operacionBinaria = Minimo;
                    break;
                case 10:
                    operacionUnaria = Redondeo;
                    break;
                default:
                    Console.WriteLine("Opción no válida.");
                    continue;
            }

            Console.Write("\nIngrese el primer número: ");
            double num1 = Convert.ToDouble(Console.ReadLine());

            if (operacionBinaria != null)
            {
                Console.Write("\nIngrese el segundo número: ");
                double num2 = Convert.ToDouble(Console.ReadLine());
                Console.Clear();
                Console.WriteLine("Números ingresados: {0}, {1}", num1, num2);
                Console.WriteLine($"El resultado es: {operacionBinaria(num1, num2)}");
            }
            else if (operacionUnaria != null)
            {
                Console.Clear();
                Console.WriteLine("Números ingresados: {0}", num1);
                Console.WriteLine($"El resultado es: {operacionUnaria(num1)}");
            }
        }
    }

    static double Suma(double a, double b) => a + b;
    static double Resta(double a, double b) => a - b;
    static double Multiplicacion(double a, double b) => a * b;
    static double Division(double a, double b) => b != 0 ? a / b : throw new DivideByZeroException();
    static double Exponenciacion(double a, double b) => Math.Pow(a, b);
    static double RaizCuadrada(double a) => Math.Sqrt(a);
    static double ValorAbsoluto(double a) => Math.Abs(a);
    static double Maximo(double a, double b) => Math.Max(a, b);
    static double Minimo(double a, double b) => Math.Min(a, b);
    static double Redondeo(double a) => Math.Round(a);
}
