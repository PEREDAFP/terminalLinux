
### 1. Introducción a `cut`

El comando `cut` se utiliza para extraer secciones de líneas de archivos de texto. Es útil para seleccionar columnas o partes de un archivo de texto delimitado por caracteres o campos específicos.

#### Sintaxis general:
```bash
cut [opciones] [archivo]
```

#### Opciones más comunes:
- `-d` : Define el delimitador (por ejemplo, una coma o espacio).
- `-f` : Especifica los campos a extraer.
- `-c` : Extrae caracteres específicos en cada línea.

#### Actividades con `cut`

1. **Extraer la primera columna de un archivo CSV:**
   - **Comando**:
     ```bash
     cut -d',' -f1 archivo.csv
     ```

2. **Extraer los primeros 5 caracteres de cada línea en un archivo:**
   - **Comando**:
     ```bash
     cut -c1-5 archivo.txt
     ```

3. **Extraer la segunda y cuarta columna de un archivo delimitado por tabuladores:**
   - **Comando**:
     ```bash
     cut -d$'\t' -f2,4 archivo.txt
     ```

4. **Extraer los campos 3 a 5 de un archivo delimitado por comas:**
   - **Comando**:
     ```bash
     cut -d',' -f3-5 archivo.csv
     ```

5. **Mostrar solo el primer carácter de cada línea de un archivo de texto:**
   - **Comando**:
     ```bash
     cut -c1 archivo.txt
     ```

6. **Extraer múltiples campos de un archivo con delimitador personalizado (ej: `|`):**
   - **Comando**:
     ```bash
     cut -d'|' -f1,3,5 archivo.txt
     ```

7. **Extraer nombres de usuario de un archivo `/etc/passwd` (primer campo):**
   - **Comando**:
     ```bash
     cut -d':' -f1 /etc/passwd
     ```

8. **Extraer las 8 primeras letras de cada línea de un archivo log:**
   - **Comando**:
     ```bash
     cut -c1-8 archivo.log
     ```

9. **Cortar desde el carácter 5 hasta el final de la línea:**
   - **Comando**:
     ```bash
     cut -c5- archivo.txt
     ```

10. **Extraer la tercera columna de un archivo con espacios como delimitadores:**
    - **Comando**:
      ```bash
      cut -d' ' -f3 archivo.txt
      ```

---

### 2. Introducción a `uniq`

`uniq` se utiliza para eliminar o reportar líneas duplicadas en un archivo de texto, pero solo funciona en líneas consecutivas, por lo que se suele usar junto con `sort`.

#### Sintaxis general:
```bash
uniq [opciones] [archivo]
```

#### Opciones más comunes:
- `-c` : Muestra el número de repeticiones de cada línea.
- `-d` : Muestra solo las líneas duplicadas.
- `-u` : Muestra solo las líneas únicas (no repetidas).
- `-i` : Ignora mayúsculas y minúsculas al comparar.

#### Actividades con `uniq`

1. **Eliminar duplicados consecutivos de un archivo:**
   - **Comando**:
     ```bash
     uniq archivo.txt
     ```

2. **Mostrar solo las líneas duplicadas en un archivo:**
   - **Comando**:
     ```bash
     uniq -d archivo.txt
     ```

3. **Mostrar las líneas duplicadas y el número de ocurrencias:**
   - **Comando**:
     ```bash
     uniq -c archivo.txt
     ```

4. **Eliminar duplicados en un archivo sin tener en cuenta mayúsculas/minúsculas:**
   - **Comando**:
     ```bash
     uniq -i archivo.txt
     ```

5. **Mostrar solo las líneas únicas de un archivo:**
   - **Comando**:
     ```bash
     uniq -u archivo.txt
     ```

6. **Eliminar duplicados en una lista de nombres después de ordenarla:**
   - **Comando**:
     ```bash
     sort nombres.txt | uniq
     ```

7. **Mostrar el número de repeticiones de cada línea ignorando mayúsculas:**
   - **Comando**:
     ```bash
     sort archivo.txt | uniq -ci
     ```

8. **Eliminar duplicados en el contenido de una columna de un archivo CSV:**
   - **Comando**:
     ```bash
     cut -d',' -f1 archivo.csv | sort | uniq
     ```

9. **Combinar `uniq` con `sort` para contar las repeticiones en un archivo de logs:**
   - **Comando**:
     ```bash
     sort archivo.log | uniq -c
     ```

10. **Mostrar solo las líneas duplicadas de un archivo de texto (ignora caso):**
    - **Comando**:
      ```bash
      sort archivo.txt | uniq -di
      ```

---

### 3. Introducción a `tar`

`tar` es un comando utilizado para empaquetar (y opcionalmente comprimir) varios archivos en un único archivo "tarball" (`.tar`, `.tar.gz`, `.tgz`).

#### Sintaxis general:
```bash
tar [opciones] [archivo.tar] [archivos_o_directorios]
```

#### Opciones más comunes:
- `-c` : Crear un archivo tar.
- `-x` : Extraer un archivo tar.
- `-v` : Verboso, muestra el progreso.
- `-f` : Especificar el nombre del archivo tar.
- `-z` : Comprimir o descomprimir usando gzip (`.tar.gz`).
- `-j` : Comprimir o descomprimir usando bzip2 (`.tar.bz2`).

#### Actividades con `tar`

1. **Crear un archivo tar de un directorio:**
   - **Comando**:
     ```bash
     tar -cvf archivo.tar /ruta/del/directorio
     ```

2. **Crear un archivo tar y comprimirlo con gzip:**
   - **Comando**:
     ```bash
     tar -czvf archivo.tar.gz /ruta/del/directorio
     ```

3. **Extraer un archivo `.tar.gz`:**
   - **Comando**:
     ```bash
     tar -xzvf archivo.tar.gz
     ```

4. **Crear un archivo tar y comprimirlo con bzip2:**
   - **Comando**:
     ```bash
     tar -cjvf archivo.tar.bz2 /ruta/del/directorio
     ```

5. **Extraer un archivo `.tar.bz2`:**
   - **Comando**:
     ```bash
     tar -xjvf archivo.tar.bz2
     ```

6. **Listar el contenido de un archivo tar sin extraerlo:**
   - **Comando**:
     ```bash
     tar -tvf archivo.tar
     ```

7. **Extraer archivos específicos de un tar:**
   - **Comando**:
     ```bash
     tar -xvf archivo.tar archivo_a_extraer.txt
     ```

8. **Comprimir varios archivos en un tar.gz:**
   - **Comando**:
     ```bash
     tar -czvf archivos_comprimidos.tar.gz archivo1.txt archivo2.txt archivo3.txt
     ```

9. **Agregar archivos a un archivo tar existente:**
   - **Comando**:
     ```bash
     tar -rvf archivo.tar archivo_nuevo.txt
     ```

10. **Comprimir archivos de forma incremental:**
    - **Comando**:
      ```bash
      tar -g archivo.snar -cvf incremental.tar /ruta/del/directorio
      ```

11. **Crear un archivo tar excluyendo ciertos archivos o directorios:**
    - **Comando**:
      ```bash
      tar --exclude='*.log' -cvf archivo.tar /ruta/del/directorio
      ```

12. **Dividir un archivo tar en varios archivos más pequeños:**
    - **Comando**:
      ```bash
      tar -cvf - /ruta/del/directorio | split -b 500M - archivo_parte.tar.
      ```

13. **Comprimir el contenido de varios directorios en un archivo `.tar.gz`:**
    - **Comando**:
      ```bash
      tar -czvf archivo.tar.gz /directorio1 /directorio2
      ```

14. **Comprimir todos los archivos `.txt` en un archivo `.tar`:**
    - **Comando**:
      ```bash
      tar -cvf archivos_texto.tar *.txt
      ```

15. **Extraer un archivo tar sin sobrescribir los archivos existentes:**
    - **Comando**:
      ```bash
      tar -xvfk archivo.tar
      ```

16. **Comprimir un archivo tar con `xz`:**
    - **Comando**:
      ```bash
      tar -cJvf archivo.tar.xz

 /ruta/del/directorio
      ```

17. **Extraer un archivo `.tar.xz`:**
    - **Comando**:
      ```bash
      tar -xJvf archivo.tar.xz
      ```

18. **Verificar la integridad de un archivo `.tar.gz`:**
    - **Comando**:
      ```bash
      tar -tzvf archivo.tar.gz
      ```

19. **Listar el contenido de un archivo `.tar.gz`:**
    - **Comando**:
      ```bash
      tar -tzvf archivo.tar.gz
      ```

20. **Eliminar un archivo de un archivo tar:**
    - **Comando**:
      ```bash
      tar --delete -f archivo.tar archivo_a_eliminar.txt
      ```

---
