

### Introducción a `find`

El comando `find` en Linux es una herramienta poderosa para buscar archivos y directorios dentro de un sistema de archivos, basándose en varios criterios como nombre, tipo, tamaño, fecha de modificación, permisos, entre otros. Es ideal para realizar búsquedas complejas y ejecutar acciones en los resultados.

---

### Actividades prácticas con `find`

1. **Buscar todos los archivos con una extensión específica (por ejemplo, `.txt`):**
   - **Actividad**: Encuentra todos los archivos `.txt` en el directorio actual y subdirectorios.
   - **Comando**:
     ```bash
     find . -name "*.txt"
     ```
   
2. **Buscar archivos por tamaño mayor a 100 MB:**
   - **Actividad**: Encuentra archivos mayores a 100 MB en el sistema.
   - **Comando**:
     ```bash
     find / -size +100M
     ```

3. **Buscar archivos modificados en los últimos 7 días:**
   - **Actividad**: Encuentra archivos modificados en la última semana.
   - **Comando**:
     ```bash
     find /ruta/a/buscar -mtime -7
     ```

4. **Buscar archivos modificados hace más de 30 días:**
   - **Actividad**: Encuentra archivos que no han sido modificados en los últimos 30 días.
   - **Comando**:
     ```bash
     find /ruta/a/buscar -mtime +30
     ```

5. **Buscar archivos por permisos (por ejemplo, archivos con permisos 777):**
   - **Actividad**: Encuentra todos los archivos con permisos 777.
   - **Comando**:
     ```bash
     find /ruta/a/buscar -perm 777
     ```

6. **Buscar archivos de un usuario específico:**
   - **Actividad**: Encuentra todos los archivos que pertenecen al usuario `nombre_usuario`.
   - **Comando**:
     ```bash
     find /ruta/a/buscar -user nombre_usuario
     ```

7. **Buscar archivos por grupo:**
   - **Actividad**: Encuentra todos los archivos que pertenecen al grupo `nombre_grupo`.
   - **Comando**:
     ```bash
     find /ruta/a/buscar -group nombre_grupo
     ```

8. **Buscar directorios únicamente (no archivos):**
   - **Actividad**: Encuentra todos los directorios dentro de un directorio específico.
   - **Comando**:
     ```bash
     find /ruta/a/buscar -type d
     ```

9. **Buscar archivos vacíos (de tamaño cero):**
   - **Actividad**: Encuentra todos los archivos vacíos.
   - **Comando**:
     ```bash
     find /ruta/a/buscar -empty
     ```

10. **Buscar y eliminar archivos `.tmp`:**
    - **Actividad**: Encuentra todos los archivos con la extensión `.tmp` y elimínalos.
    - **Comando**:
      ```bash
      find /ruta/a/buscar -name "*.tmp" -exec rm {} \;
      ```

11. **Buscar archivos y ejecutar un comando (mover archivos):**
    - **Actividad**: Encuentra archivos `.log` y muévelos a otro directorio.
    - **Comando**:
      ```bash
      find /ruta/a/buscar -name "*.log" -exec mv {} /ruta/destino \;
      ```

12. **Buscar archivos mayores de 1 GB y eliminarlos:**
    - **Actividad**: Encuentra archivos mayores de 1 GB y los elimina.
    - **Comando**:
      ```bash
      find /ruta/a/buscar -size +1G -exec rm {} \;
      ```

13. **Buscar archivos con nombre insensible a mayúsculas:**
    - **Actividad**: Encuentra archivos llamados `documento.txt` sin importar mayúsculas/minúsculas.
    - **Comando**:
      ```bash
      find /ruta/a/buscar -iname "documento.txt"
      ```

14. **Buscar archivos con nombres que coincidan parcialmente (expresión regular):**
    - **Actividad**: Encuentra archivos cuyo nombre comience con `log` seguido de cualquier número.
    - **Comando**:
      ```bash
      find /ruta/a/buscar -regex ".*log[0-9]+.*"
      ```

15. **Buscar archivos más recientes que un archivo dado:**
    - **Actividad**: Encuentra todos los archivos modificados después de `archivo_de_referencia.txt`.
    - **Comando**:
      ```bash
      find /ruta/a/buscar -newer archivo_de_referencia.txt
      ```

16. **Buscar archivos y listar solo los primeros 10 resultados:**
    - **Actividad**: Encuentra archivos `.jpg` y muestra solo los primeros 10 resultados.
    - **Comando**:
      ```bash
      find /ruta/a/buscar -name "*.jpg" | head -n 10
      ```

17. **Buscar archivos modificados hace exactamente 5 días:**
    - **Actividad**: Encuentra archivos modificados hace exactamente 5 días.
    - **Comando**:
      ```bash
      find /ruta/a/buscar -mtime 5
      ```

18. **Buscar y cambiar permisos de archivos:**
    - **Actividad**: Encuentra todos los archivos `.sh` y cambia sus permisos para hacerlos ejecutables.
    - **Comando**:
      ```bash
      find /ruta/a/buscar -name "*.sh" -exec chmod +x {} \;
      ```

19. **Buscar archivos por número de enlaces (hard links):**
    - **Actividad**: Encuentra archivos que tengan exactamente 2 enlaces duros.
    - **Comando**:
      ```bash
      find /ruta/a/buscar -links 2
      ```

20. **Buscar y comprimir archivos:**
    - **Actividad**: Encuentra todos los archivos `.log` y los comprime en un archivo `.tar.gz`.
    - **Comando**:
      ```bash
      find /ruta/a/buscar -name "*.log" -exec tar -czvf logs.tar.gz {} +
      ```

---

### Explicación de las opciones más usadas de `find`:

- **`-name`**: Busca archivos por nombre exacto o patrón con comodines (`*.txt`).
- **`-iname`**: Igual que `-name`, pero sin distinguir entre mayúsculas y minúsculas.
- **`-size`**: Busca archivos según su tamaño (p.ej. `+100M` para más de 100 MB).
- **`-mtime`**: Busca archivos según la fecha de modificación (en días, p.ej. `-mtime -7` para modificados en la última semana).
- **`-perm`**: Filtra archivos por permisos (p.ej. `777`).
- **`-user` y `-group`**: Filtra archivos por el usuario o grupo propietario.
- **`-type`**: Filtra por tipo (`f` para archivos y `d` para directorios).
- **`-empty`**: Encuentra archivos o directorios vacíos.
- **`-exec`**: Ejecuta un comando sobre cada archivo encontrado.
- **`-newer`**: Encuentra archivos más recientes que un archivo de referencia.

---
