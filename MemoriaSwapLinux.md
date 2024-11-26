### **Sesión: Trabajo con Memoria Virtual en Linux**

**Objetivo:**  
En esta sesión, los alumnos aprenderán a gestionar la memoria virtual en Linux mediante el uso de herramientas como `dd`, `mkswap`, y la configuración de particiones `linux-swap`. 
---

### **1. Introducción a la memoria virtual**
- **Memoria virtual:** Espacio en disco configurado para actuar como memoria RAM cuando esta última se agota. 
- **Swap:** En Linux, la memoria virtual se implementa a través de particiones `linux-swap` o archivos de intercambio. Su configuración puede mejorar el rendimiento en sistemas con poca RAM.
  
---

### **2. Comandos esenciales para gestionar memoria virtual**
#### **Crear un archivo de swap con `dd` y configurarlo**
1. **Crear un archivo para swap:**
   ```bash
   sudo dd if=/dev/zero of=/swapfile bs=1M count=1024
   ```
   - `if=/dev/zero`: Usa el archivo especial para generar datos vacíos.
   - `of=/swapfile`: Nombre del archivo de salida.
   - `bs=1M`: Tamaño de bloque (1 MB).
   - `count=1024`: Número de bloques (1 GB).

2. **Configurar el archivo como swap:**
   ```bash
   sudo chmod 600 /swapfile  # Ajustar permisos
   sudo mkswap /swapfile     # Convertir el archivo en swap
   sudo swapon /swapfile     # Activar el archivo swap
   ```

3. **Verificar el uso de swap:**
   ```bash
   free -h
   swapon --show
   ```

4. **Hacer el archivo swap permanente: (esto lo veremos con más detalle en la sesión de fstab)**
   Añadir esta línea al archivo `/etc/fstab`:
   ```bash
   /swapfile none swap sw 0 0
   ```

#### **Crear una partición `linux-swap` y configurarla: (previa instalación de un nuevo disco en la MV. Puedes realizarlo con gparted)**
1. **Crear una partición con `fdisk`:**
   - Selecciona un disco con `sudo fdisk /dev/sdX` (reemplaza `X` con la unidad correspondiente).
   - Dentro de `fdisk`:
     - Presiona `n` para crear una nueva partición.
     - Elige el tamaño deseado.
     - Presiona `t` y selecciona el tipo `82` (Linux Swap).
     - Guarda los cambios con `w`.

2. **Configurar y activar la partición como swap:**
   ```bash
   sudo mkswap /dev/sdX1  # Reemplaza con la partición creada
   sudo swapon /dev/sdX1
   ```

3. **Verificar y hacer permanente:**
   - Verifica con:
     ```bash
     free -h
     swapon --show
     ```
   - Añade al archivo `/etc/fstab`:
     ```bash
     /dev/sdX1 none swap sw 0 0
     ```

---

### **3. Monitoreo de la memoria en Linux**
- **Comandos útiles:**
  - `free -h`: Muestra el estado de la memoria (RAM y swap) en formato legible.
  - `vmstat`: Proporciona estadísticas de uso de memoria y swap.
  - `top` o `htop`: Muestra procesos activos y su consumo de memoria.
  - `swapon --show`: Lista todas las áreas de swap activas.
  - `cat /proc/meminfo`: Detalles sobre la memoria del sistema, incluida la swap.
  - `dstat -g --swap`: Monitorea el uso de swap en tiempo real.

---

### **4. Ejercicios prácticos**
#### **Ejercicio 1:** Crear un archivo de 512 MB como swap y activarlo temporalmente.  
#### **Ejercicio 2:** Crear ulo veremos con más detalle en el tema de procesos y prioridades)** Configurar el archivo `/proc/sys/vm/swappiness` para cambiar la prioridad de uso de swap.

---

### **5. Soluciones**
#### **Solución Ejercicio 1:**
```bash
sudo dd if=/dev/zero of=/swapfile bs=1M count=512
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
swapon --show
```

#### **Solución Ejercicio 2:**
1. Crea la partición con `fdisk` seleccionando tipo `82`.
2. Configúrala:
   ```bash
   sudo mkswap /dev/sdX1
   sudo swapon /dev/sdX1
   ```

#### **Solución Ejercicio 3:**
```bash
sudo swapoff /swapfile  # Desactiva archivo swap
sudo swapoff /dev/sdX1  # Desactiva partición swap
```

#### **Solución Ejercicio 4:**
1. Crear un archivo adicional:
   ```bash
   sudo dd if=/dev/zero of=/extra_swap bs=1M count=1024
   sudo chmod 600 /extra_swap
   sudo mkswap /extra_swap
   sudo swapon /extra_swap
   ```
2. Verifica con `swapon --show`.

#### **Solución Ejercicio 5:**
```bash
free -h
vmstat
```

#### **Solución Ejercicio 6:**
1. Crear archivo swap:
   ```bash
   sudo dd if=/dev/zero of=/swapfile bs=1M count=512
   sudo chmod 600 /swapfile
   sudo mkswap /swapfile
   sudo swapon /swapfile
   ```
2. Añadir a `/etc/fstab`:
   ```plaintext
   /swapfile none swap sw 0 0
   ```

#### **Solución Ejercicio 7:**
1. Configura la partición externa:
   ```bash
   sudo mkswap /dev/sdY1
   sudo swapon /dev/sdY1
   ```
2. Añade a `/etc/fstab`:
   ```plaintext
   /dev/sdY1 none swap sw 0 0
   ```

#### **Solución Ejercicio 8:**
```bash
top  # Busca la columna de swap
```

#### **Solución Ejercicio 9:**
1. Ejecuta un script que consume memoria y monitorea:
   ```bash
   while true; do malloc 1000000; done
   ```
2. Observa con:
   ```bash
   vmstat 1
   free -h
   ```

#### **Solución Ejercicio 10:**
1. Cambiar prioridad de uso de swap:
   ```bash
   echo 10 | sudo tee /proc/sys/vm/swappiness
   ```
2. Hacerlo permanente añadiendo a `/etc/sysctl.conf`:
   ```plaintext
   vm.swappiness=10
   ```

---
