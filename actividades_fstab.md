**Sesión de Trabajo `fstab`**

---

1. **Identificar las particiones disponibles**
   - Lista las particiones y sistemas de archivos usando `lsblk` y `blkid`.
   - Anota la información relevante (UUID y tipo de sistema de archivos).

2. **Explorar el contenido del archivo `fstab`**
   - Examina el archivo `/etc/fstab` y describe las configuraciones predeterminadas.

3. **Montar una partición manualmente**
   - Usa `mount` para montar una partición en un directorio temporal.
   - Verifica el montaje con `df -h`.

4. **Agregar una partición a `fstab`**
   - Configura una partición para que se monte automáticamente en `/mnt/test` al reiniciar.

5. **Simular un error en `fstab`**
   - Introduce una entrada inválida en `fstab` (por ejemplo, un UUID incorrecto).
   - Reinicia la máquina virtual y repara el problema.

6. **Configurar una partición con opciones erróneas**
   - Edita `fstab` para montar una partición con una opción no válida.
   - Observa el error al intentar reiniciar y corrígelo.

7. **Configurar una partición en modo de solo lectura**
   - Modifica `fstab` para montar una partición como `ro`.
   - Verifica que los archivos en el sistema de archivos no puedan modificarse.

8. **Probar el montaje manual tras un error en `fstab`**
   - Configura mal una entrada en `fstab`.
   - Utiliza `mount -a` para comprobar el error y luego soluciónalo.

9. **Simular el uso de /dev/ en lugar de UUID**
    - Configura `fstab` con el nombre del dispositivo (`/dev/sdX`).
    - Cambia el orden de los discos en la máquina virtual y observa qué sucede.

10. **Corregir un error de configuración con /dev/**
    - Realiza una configuración en `fstab` usando `/dev/sdX`.
    - Cambia el orden de los discos y repara el sistema para usar UUID.

11. **Montar una partición con opción `noauto`**
    - Configura una partición para que no se monte automáticamente.
    - Monta la partición manualmente con `mount` cuando sea necesario siendo un "simple" usuario.

12. **Probar distintas opciones de sincronización**
    - Configura `fstab` para montar una partición con las opciones `sync` y `async`.
    - Observa las diferencias en el comportamiento.

14. **Configurar el montaje con `relatime`**
    - Edita `fstab` para usar `relatime` en una partición.
    - Verifica su impacto en el funcionamiento. Obtén información sobre lo que es relatime

15. **Configurar el montaje de un archivo ISO**
    - Descarga un archivo ISO y configúralo en `fstab` para que se monte automáticamente en `/mnt/iso`.

16. **Simular permisos incorrectos en `fstab`**
    - Configura `fstab` con una opción incorrecta como `uid=1000` para una partición.
    - Verifica qué sucede y corrígelo.

17. **Documentar configuraciones en `fstab`**
    - Agrega comentarios detallados a cada entrada en `fstab` para explicar su propósito.

18. **Comprobar errores en el archivo `fstab`**
    - Usa el comando `mount -a` para identificar errores en el archivo sin reiniciar el sistema.

19. **Probar configuraciones temporales**
    - Monta una partición manualmente sin agregarla a `fstab`.
    - Verifica qué ocurre tras reiniciar.


20. **Trabajar con particiones en memoria usando tmpfs**
    - Configura una entrada en `fstab` para montar una partición temporal en `/mnt/tmp` usando el sistema de archivos `tmpfs`.
    - Establece un límite de 100 MB para el uso de memoria.
    - Crea un script que cree ficheros "muy gordos"  en `/mnt/tmp` y verifica el uso de memoria con `free -m`.

