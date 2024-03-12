using System;
using System.Collections.Generic;
using System.Linq;
using System.Diagnostics;

public class Program
{
    public static void Main(string[] args)
    {
        Console.Write("Lista 1: ");
        List<int> listaGenerada = ListaRandom(10);
        Console.Write("Lista 2: ");
        List<int> listaGenerada2 = ListaRandom(10);
        Console.WriteLine("\nEl minimo de la lista 1 es: " + MinV2(listaGenerada));
        Console.WriteLine("\nEl maximo de la lista 1 es: " + MaxV2(listaGenerada));
        Console.WriteLine("\nEl minimo de la lista 2 es: " + MinV2(listaGenerada2));
        Console.WriteLine("\nEl maximo de la lista 2 es: " + MaxV2(listaGenerada2));
        Console.WriteLine("\nSuma de listas 1 y 2:");
        Stopwatch stopwatch = new Stopwatch();
        stopwatch.Start();
        Console.WriteLine($"Listas sumadas: {SumarListas(listaGenerada, listaGenerada2).Sum()}");
        stopwatch.Stop();

        Console.WriteLine($"Tiempo de ejecución: {stopwatch.ElapsedMilliseconds} milisegundos");
        Console.ReadKey();
    }

    public static List<int> ListaRandom(int n)
    {
        Random random = new Random();
        List<int> lista = new List<int>();

        Console.Write("[");
        for (int i = 0; i < n; i++)
        {
            lista.Add(random.Next(-100, 100));
            Console.Write(lista[i] + ", ");
        }
        Console.Write("]\n");

        return lista;
    }

    public static int MinV2(List<int> lista)
    {
        int minimo = lista[0];
        for (int i = 1; i < lista.Count; i++)
        {
            if (lista[i] < minimo)
            {
                minimo = lista[i];
            }
        }
        return minimo;
    }

    public static int MaxV2(List<int> lista)
    {
        int maximo = lista[0];
        for (int i = 0; i < lista.Count; i++)
        {
            if (lista[i] > maximo)
            {
                maximo = lista[i];
            }
        }
        return maximo;
    }

    public static List<int> SumarListas(List<int> lista1, List<int> lista2)
    {
        List<int> sumaListas = new List<int>();

        Console.Write("[");
        for (int i = 0; i < lista1.Count; i++)
        {
            sumaListas.Add(lista1[i] + lista2[i]);
            Console.Write(sumaListas[i] + ", ");
        }
        Console.Write("]\n");

        return sumaListas;
    }
}
