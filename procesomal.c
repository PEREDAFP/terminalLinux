#include <stdio.h>
#include <unistd.h>
#include <time.h>

int main() {
    FILE *fp;
    time_t rawtime;
    struct tm *timeinfo;
    char buffer[80];
    pid_t pid;

    while (1) {
        fp = fopen("/var/log/procesosmal.log", "a");
        if (fp == NULL) {
            perror("Error opening file");
            return 1;
        }

        time(&rawtime);
        timeinfo = localtime(&rawtime);

        strftime(buffer, sizeof(buffer), "%d-%m-%Y %H:%M:%S", timeinfo);

        pid = getpid();

        fprintf(fp, "[%s] Ejecutando un proceso a lo tonto (PID: %d)\n", buffer, pid);

        fclose(fp);

        sleep(1);
    }

    return 0;
}
