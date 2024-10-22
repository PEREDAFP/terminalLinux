### 1. **Introducción a `ps`**

El comando `ps` se utiliza para mostrar una lista de procesos en ejecución en el sistema. Es una herramienta fundamental para observar el estado de los procesos, identificarlos y obtener información detallada sobre su uso de recursos.

#### Sintaxis general:
```bash
ps [opciones]
```

#### Opciones más comunes:
- `-e` : Muestra todos los procesos.
- `-f` : Muestra detalles completos (full format).
- `-u usuario` : Muestra procesos pertenecientes a un usuario específico.
- `-aux` : Muestra todos los procesos con información detallada.
- `-T` : Muestra los hilos de los procesos.

---

#### Actividades con `ps`

1. **Mostrar todos los procesos en ejecución:**
   - **Comando**:
     ```bash
     ps -e
     ```

2. **Mostrar procesos con información detallada (formato largo):**
   - **Comando**:
     ```bash
     ps -ef
     ```

3. **Mostrar los procesos ejecutados por un usuario específico:**
   - **Comando**:
     ```bash
     ps -u nombre_usuario
     ```

4. **Mostrar los procesos con más uso de CPU y memoria:**
   - **Comando**:
     ```bash
     ps aux --sort=-%cpu,-%mem
     ```

5. **Mostrar los procesos con el formato largo para un usuario específico:**
   - **Comando**:
     ```bash
     ps -fU nombre_usuario
     ```

6. **Listar los procesos en ejecución y sus threads (hilos):**
   - **Comando**:
     ```bash
     ps -eT
     ```

7. **Mostrar el árbol de procesos para visualizar jerarquías:**
   - **Comando**:
     ```bash
     ps -ef --forest
     ```

8. **Mostrar solo el PID y nombre del proceso en ejecución:**
   - **Comando**:
     ```bash
     ps -e -o pid,comm
     ```

9. **Obtener información detallada de un proceso específico por su PID:**
   - **Comando**:
     ```bash
     ps -p PID -f
     ```

10. **Filtrar procesos que ejecutan un programa específico (ej: `bash`):**
    - **Comando**:
      ```bash
      ps -C bash
      ```

---

### 2. **Introducción a `lsof`**

El comando `lsof` (List Open Files) es usado para listar todos los archivos abiertos por procesos. En Linux, todo (archivos, sockets, dispositivos) es considerado un archivo, por lo que `lsof` permite observar tanto archivos normales como conexiones de red abiertas.

#### Sintaxis general:
```bash
lsof [opciones]
```

#### Opciones más comunes:
- `-i` : Muestra conexiones de red y sockets.
- `-u usuario` : Lista los archivos abiertos por un usuario.
- `-p PID` : Lista los archivos abiertos por un proceso específico.
- `-c comando` : Filtra los archivos abiertos por un comando específico.
- `+D directorio` : Lista todos los archivos abiertos dentro de un directorio.

---

#### Actividades con `lsof`

1. **Listar todos los archivos abiertos por todos los procesos:**
   - **Comando**:
     ```bash
     lsof
     ```

2. **Listar los archivos abiertos por un proceso específico (PID):**
   - **Comando**:
     ```bash
     lsof -p PID
     ```

3. **Listar los archivos abiertos por un usuario específico:**
   - **Comando**:
     ```bash
     lsof -u nombre_usuario
     ```

4. **Listar las conexiones de red activas (TCP y UDP):**
   - **Comando**:
     ```bash
     lsof -i
     ```

5. **Mostrar solo las conexiones abiertas en un puerto específico (ej: 80):**
   - **Comando**:
     ```bash
     lsof -i :80
     ```

6. **Listar los archivos abiertos dentro de un directorio específico:**
   - **Comando**:
     ```bash
     lsof +D /ruta/del/directorio
     ```

7. **Listar archivos abiertos por un comando específico (ej: `sshd`):**
   - **Comando**:
     ```bash
     lsof -c sshd
     ```

8. **Listar conexiones de red para un usuario específico:**
   - **Comando**:
     ```bash
     lsof -i -u nombre_usuario
     ```

9. **Listar archivos abiertos por un proceso en un sistema de archivos determinado (ej: `/var`):**
   - **Comando**:
     ```bash
     lsof +D /var
     ```

10. **Listar todas las conexiones activas de tipo UDP:**
    - **Comando**:
      ```bash
      lsof -i udp
      ```

---

### 3. **Introducción a `strace`**

El comando `strace` es una herramienta avanzada para rastrear las llamadas al sistema y las señales de un proceso en ejecución. Es muy útil para depuración y diagnóstico de problemas de rendimiento o fallos en un programa.

#### Sintaxis general:
```bash
strace [opciones] [comando]
```

#### Opciones más comunes:
- `-p` : Adjuntar `strace` a un proceso existente (por PID).
- `-e` : Filtrar las llamadas al sistema (ej: `open`, `read`, `write`).
- `-c` : Muestra estadísticas de las llamadas al sistema.
- `-o archivo` : Redirigir la salida de `strace` a un archivo.

---

#### Actividades con `strace`

1. **Rastrear las llamadas al sistema de un comando (ej: `ls`):**
   - **Comando**:
     ```bash
     strace ls
     ```

2. **Rastrear las llamadas al sistema de un proceso específico por PID:**
   - **Comando**:
     ```bash
     strace -p PID
     ```

3. **Filtrar y mostrar solo las llamadas al sistema `open` de un proceso:**
   - **Comando**:
     ```bash
     strace -e open ls
     ```

4. **Generar un resumen de estadísticas de llamadas al sistema para un proceso:**
   - **Comando**:
     ```bash
     strace -c ls
     ```

5. **Adjuntar `strace` a un proceso en ejecución y mostrar solo las llamadas `write`:**
   - **Comando**:
     ```bash
     strace -p PID -e write
     ```

6. **Registrar todas las llamadas al sistema de un proceso en un archivo de salida:**
   - **Comando**:
     ```bash
     strace -o salida_strace.txt ls
     ```

7. **Rastrear un proceso y mostrar solo las llamadas al sistema relacionadas con la red (ej: `connect`, `sendto`, `recvfrom`):**
   - **Comando**:
     ```bash
     strace -e trace=network curl google.com
     ```

8. **Adjuntar `strace` a un proceso en ejecución y mostrar todas las señales recibidas:**
   - **Comando**:
     ```bash
     strace -p PID -e signal
     ```

9. **Rastrear un comando y mostrar todas las llamadas a la función `read`:**
   - **Comando**:
     ```bash
     strace -e read cat archivo.txt
     ```

10. **Rastrear un proceso y filtrar solo las llamadas relacionadas con el acceso a archivos (`open`, `close`, `read`, `write`):**
    - **Comando**:
      ```bash
      strace -e trace=file -p PID
      ```

---

### Resumen de las herramientas:

- **`ps`**: Utilizado para listar y obtener información sobre los procesos que se están ejecutando en el sistema. Ideal para monitorear el uso de CPU, memoria, y jerarquías de procesos.
  
- **`lsof`**: Muestra los archivos abiertos por los procesos, incluyendo archivos de dispositivos y conexiones de red. Es fundamental para identificar qué procesos están usando recursos o archivos.
  
- **`strace`**: Una herramienta avanzada de depuración que rastrea las llamadas al sistema de un proceso. Útil para diagnosticar problemas, identificar fallos en la ejecución y comprender la interacción de los programas con el sistema operativo.
