#include <stdio.h>
#include <stdlib.h>

#define MEMORY_SIZE 2000000000 // 2 GB

int main() {
    void *ptr = malloc(MEMORY_SIZE);

    if (ptr == NULL) {
        fprintf(stderr, "\033[1;31mError: No se pudo reservar la memoria necesaria: 2  GB.\033[0m\n");
        return 1;
    } else {
        printf("\033[1;32mÉxito: Se ha reservado 2 GB de memoria.\033[0m\n");
        free(ptr);
        return 0;
    }
}