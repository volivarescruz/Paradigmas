#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

void LlenarArreglo(int n, int nums[]);
void ImprimirArreglo(int n, int nums[]);
int BusquedaSecuencial(int numb, int nums[], int n);
void bubbleSort(int nums[], int n);

int main() {
    int n = 0, n2 = 0;

    do {
        printf("Ingrese el numero de elementos (mayor a 1000): ");
        scanf("%d", &n);
    } while (n < 1000);

    clock_t start, end;
    double tiempo;
    int nums[n];
    
    start = clock();

    LlenarArreglo(n, nums);
    ImprimirArreglo(n, nums);

    end = clock();
    tiempo = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Tiempo de llenado e impresión del arreglo: %f segundos\n", tiempo);
    printf("Pulse enter para continuar . . .");
    getchar(); getchar(); // Limpiar el buffer de entrada

    system("clear || cls");

    start = clock();

    while (true) {
        printf("Menú de Opciones:\n");
        printf("1. Buscar número (secuencial)\n");
        printf("2. Ordenar y mostrar arreglo\n");
        printf("3. Salir\n");
        printf("Seleccione una opción: ");

        int option;
        scanf("%d", &option);

        switch (option) {
            case 1:
                printf("Ingrese el número a buscar: ");
                scanf("%d", &n2);

                start = clock();
                BusquedaSecuencial(n2, nums, n);
                end = clock();
                tiempo = ((double) (end - start)) / CLOCKS_PER_SEC;
                printf("Tiempo de búsqueda secuencial: %f segundos\n", tiempo);
                printf("Pulse enter para continuar . . .");
                getchar(); getchar(); // Limpiar el buffer de entrada
                system("clear || cls");
                break;
            case 2:
                start = clock();
                bubbleSort(nums, n);
                ImprimirArreglo(n, nums);
                end = clock();
                tiempo = ((double) (end - start)) / CLOCKS_PER_SEC;
                printf("Tiempo de ordenamiento y mostrar arreglo: %f segundos\n", tiempo);
                printf("Pulse enter para continuar . . .");
                getchar(); getchar(); // Limpiar el buffer de entrada
                system("clear || cls");
                break;
            case 3:
                printf("Saliendo del programa...");
                return 0;
            default:
                printf("Opción no válida. Por favor, seleccione nuevamente.\n");
                break;
        }
    }

    return 0;
}

void LlenarArreglo(int n, int nums[]) {
    srand(time(NULL));

    for (int i = 0; i < n; i++) {
        nums[i] = rand() % n + 1;
    }
}

void ImprimirArreglo(int n, int nums[]) {
    for (int i = 0; i < n; i++) {
        printf("pos %d: %d\n", i + 1, nums[i]);
    }
}

int BusquedaSecuencial(int numb, int nums[], int n) {
    for (int i = 0; i < n; i++) {
        if (nums[i] == numb) {
            printf("Se encontro el %d en la posición: %d\n", numb, i);
            return 1;
        }
    }
    printf("No se encontro el numero :(\n");
    return -1;
}

void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

void bubbleSort(int arr[], int n) {
    int i, j;
    for (i = 0; i < n-1; i++) {
        for (j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                swap(&arr[j], &arr[j+1]);
            }
        }
    }
}
