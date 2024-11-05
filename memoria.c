#include <stdio.h>
#include <stdlib.h>

int main() {
    long long int size = 1024 * 1024 * 1024;  // 1 GB
    long long int step = 1024 * 1024 * 128;  // 128 MB
    long long int total = 0;
    char *memory = NULL;

    printf("Monitorizando el uso de memoria en el sistema...\n");

    while (1) {
        memory = (char *)malloc(step);

        if (memory == NULL) {
            printf("No se pudo asignar más memoria.\n");
            break;
        }

        total += step;
        printf("Memoria asignada: %lld GB\n", total / (1024 * 1024 * 1024));

        // Realiza alguna operación con la memoria asignada para evitar que el compilador la optimice
        for (long long int i = 0; i < step; i++) {
            memory[i] = 'A';
        }

        // Muestra el uso de memoria en el sistema
        system("free -m");

        printf("Presiona Enter para asignar más memoria o Ctrl+C para salir...\n");
        getchar();

        free(memory);
        printf("Memoria liberada.\n");
    }

    return 0;
}
