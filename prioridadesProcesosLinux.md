### **Sesión: Gestión de Prioridades de Procesos en Linux**

**Objetivo:**  
En esta sesión, los alumnos aprenderán cómo funciona el sistema de prioridades en Linux para procesos. Exploraremos cómo visualizar y modificar prioridades utilizando los comandos `nice`, `renice` y otros métodos avanzados. La sesión incluirá ejemplos prácticos y ejercicios para consolidar el conocimiento.

---

### **1. Introducción a las prioridades de procesos en Linux**
- **Concepto de prioridad:**  
  En Linux, la prioridad de un proceso determina la cantidad de tiempo de CPU que se le asigna en relación con otros procesos. Esto se controla mediante los valores de **niceness**.
  
- **Rango de valores de niceness:**  
  - Va de `-20` (prioridad más alta) a `19` (prioridad más baja).
  - Por defecto, los procesos inician con un valor de `0`.

- **Comandos clave:**
  - `nice`: Inicia un proceso con una prioridad específica.
  - `renice`: Cambia la prioridad de un proceso en ejecución.
  - `top`/`htop`: Visualiza y modifica prioridades en tiempo real.

---

### **2. Comandos básicos para trabajar con prioridades**
#### **a. Ver prioridades de procesos**
1. **Usar `ps` para mostrar niceness:**
   ```bash
   ps -eo pid,ni,comm
   ```
   - `pid`: ID del proceso.
   - `ni`: Valor de niceness.
   - `comm`: Nombre del comando.

2. **Usar `top` para monitorear prioridades:**
   - Observa la columna **NI** en la salida de `top`.

#### **b. Cambiar prioridades**
1. **Ejecutar un proceso con una prioridad específica usando `nice`:**
   ```bash
   nice -n 10 sleep 60
   ```
   - `-n 10`: Ajusta el niceness a `10`.

2. **Cambiar la prioridad de un proceso en ejecución usando `renice`:**
   ```bash
   renice -n -5 -p <PID>
   ```
   - `-n -5`: Ajusta el niceness a `-5`.
   - `-p <PID>`: Indica el PID del proceso.

3. **Modificar prioridades desde `htop`:**
   - Selecciona un proceso y usa las teclas `F7`/`F8` para ajustar la prioridad.

#### **c. Usar permisos para controlar prioridades**
- Solo el superusuario puede establecer prioridades más altas (valores negativos de niceness). Para hacerlo:
  ```bash
  sudo nice -n -10 sleep 60
  sudo renice -n -15 -p <PID>
  ```

---

### **3. Ejercicios prácticos**
#### **Ejercicio 1:** Ver la prioridad de todos los procesos actuales  
   Ejecuta el comando `ps` para mostrar los valores de `niceness`.  
   ```bash
   ps -eo pid,ni,comm | head -10
   ```

#### **Ejercicio 2:** Ejecutar un proceso con baja prioridad  
   Inicia un proceso con un valor de niceness de `15`. Observa cómo tarda más en ejecutarse.  
   ```bash
   nice -n 15 dd if=/dev/zero of=/dev/null bs=1M count=100000
   ```

#### **Ejercicio 3:** Cambiar la prioridad de un proceso en ejecución  
   Inicia un proceso en segundo plano, cambia su prioridad y verifica el cambio con `ps`.  
   ```bash
   sleep 300 &
   renice -n -5 -p $(pgrep sleep)
   ```

#### **Ejercicio 4:** Identificar el impacto de la prioridad  
   Inicia dos procesos con diferentes prioridades (uno con `-10` y otro con `10`) y observa el comportamiento en `top`.  
   ```bash
   nice -n -10 dd if=/dev/zero of=/dev/null bs=1M count=100000 &
   nice -n 10 dd if=/dev/zero of=/dev/null bs=1M count=100000 &
   ```

#### **Ejercicio 5:** Cambiar la prioridad de múltiples procesos  
   Cambia la prioridad de todos los procesos de un usuario específico.  
   ```bash
   renice -n 5 -u <usuario>
   ```

#### **Ejercicio 6:** Monitorizar cambios de prioridad en tiempo real  
   Usa `htop` para modificar prioridades de un proceso en ejecución y observa el efecto en su consumo de CPU.

#### **Ejercicio 7:** Comprobar restricciones de permisos  
   Intenta cambiar la prioridad de un proceso a un valor negativo como usuario normal y observa el resultado.  
   ```bash
   renice -n -10 -p $(pgrep sleep)
   ```

#### **Ejercicio 8:** Cambiar prioridad con permisos de superusuario  
   Usa `sudo` para cambiar la prioridad a un valor negativo y verifica el resultado.  
   ```bash
   sudo renice -n -10 -p $(pgrep sleep)
   ```

#### **Ejercicio 9:** Establecer prioridades al lanzar varios procesos  
   Lanza tres procesos con diferentes valores de niceness (`-10`, `0`, `10`) y observa su comportamiento en `top`.

#### **Ejercicio 10:** Simular carga y analizar prioridades  
   Genera una carga artificial con `stress` y ajusta las prioridades de los procesos generados.  
   ```bash
   stress --cpu 4 --timeout 60 &
   renice -n -5 -p $(pgrep stress)
   ```

---

### **4. Soluciones a los ejercicios**
#### **Solución Ejercicio 1:**  
```bash
ps -eo pid,ni,comm | head -10
```

#### **Solución Ejercicio 2:**  
```bash
nice -n 15 dd if=/dev/zero of=/dev/null bs=1M count=100000
```

#### **Solución Ejercicio 3:**  
```bash
sleep 300 &
renice -n -5 -p $(pgrep sleep)
```

#### **Solución Ejercicio 4:**  
```bash
nice -n -10 dd if=/dev/zero of=/dev/null bs=1M count=100000 &
nice -n 10 dd if=/dev/zero of=/dev/null bs=1M count=100000 &
```

#### **Solución Ejercicio 5:**  
```bash
renice -n 5 -u <usuario>
```

#### **Solución Ejercicio 6:**  
Abrir `htop`, localizar un proceso y usar las teclas `F7`/`F8` para ajustar la prioridad.

#### **Solución Ejercicio 7:**  
El intento de cambiar a prioridad negativa fallará:
```bash
renice -n -10 -p $(pgrep sleep)
# Salida: Permission denied
```

#### **Solución Ejercicio 8:**  
```bash
sudo renice -n -10 -p $(pgrep sleep)
```

#### **Solución Ejercicio 9:**  
```bash
nice -n -10 sleep 300 &
nice -n 0 sleep 300 &
nice -n 10 sleep 300 &
```

#### **Solución Ejercicio 10:**  
```bash
stress --cpu 4 --timeout 60 &
renice -n -5 -p $(pgrep stress)
```

---
