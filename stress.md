### **¿Qué es el comando `stress`?**

El comando `stress` es una herramienta en Linux diseñada para generar **carga artificial** en el sistema. Se utiliza comúnmente para probar la estabilidad de un sistema bajo condiciones de alta carga, como un consumo intensivo de CPU, memoria o I/O. Esto es útil para pruebas de rendimiento, depuración o simulación de condiciones extremas en un entorno controlado.

---

### **Principales características de `stress`**
1. **Generación de carga:**  
   - Puede saturar uno o varios núcleos del procesador.
   - Consumo intensivo de memoria RAM.
   - Creación de operaciones pesadas de escritura/lectura en disco.
   - Uso extensivo de procesos de carga personalizados.

2. **Simulación controlada:**  
   - Puedes definir cuánto tiempo dura la prueba.
   - Ajustar el nivel de estrés generado en el sistema.

3. **Ligero y fácil de usar:**  
   - Rápida instalación y sencilla ejecución desde la línea de comandos.

---

### **Sintaxis básica del comando `stress`**
```bash
stress [opciones]
```

---

### **Opciones principales**
1. **Opciones relacionadas con la CPU:**
   - `--cpu <N>`: Usa `N` procesos que realizan cálculos matemáticos intensivos (satura núcleos).  
     Ejemplo:
     ```bash
     stress --cpu 4
     ```
     Usa 4 procesos para consumir CPU.

2. **Opciones relacionadas con la memoria:**
   - `--vm <N>`: Crea `N` procesos que asignan memoria.  
     - `--vm-bytes <TAMAÑO>`: Cantidad de memoria asignada por proceso.  
     Ejemplo:
     ```bash
     stress --vm 2 --vm-bytes 512M
     ```
     Crea 2 procesos que consumen 512 MB de memoria cada uno.

3. **Opciones relacionadas con I/O:**
   - `--io <N>`: Crea `N` procesos que realizan operaciones de entrada/salida intensivas (lectura/escritura en disco).  
     Ejemplo:
     ```bash
     stress --io 2
     ```
     Crea 2 procesos de carga de I/O.

4. **Duración de la prueba:**
   - `--timeout <TIEMPO>`: Establece el tiempo de ejecución de la prueba.  
     Ejemplo:
     ```bash
     stress --cpu 2 --timeout 60
     ```
     Realiza carga en 2 núcleos durante 60 segundos.

5. **Número de procesos totales:**
   - `--fork <N>`: Crea `N` procesos hijos para simular una carga general en el sistema.

---

### **Ejemplos de uso**
#### **1. Cargar intensivamente todos los núcleos del procesador**
```bash
stress --cpu 4
```
Consume 4 núcleos (útil en equipos con 4 o más núcleos).

#### **2. Consumir memoria RAM**
```bash
stress --vm 3 --vm-bytes 1G --timeout 30
```
- Crea 3 procesos que consumen 1 GB de RAM cada uno.
- Detiene la prueba tras 30 segundos.

#### **3. Simular carga combinada**
```bash
stress --cpu 2 --vm 1 --vm-bytes 512M --io 1 --timeout 45
```
- Usa 2 procesos para consumir CPU.
- Usa 1 proceso para consumir 512 MB de RAM.
- Crea 1 proceso de I/O.
- Dura 45 segundos.

#### **4. Simular un sistema con muchas bifurcaciones de procesos**
```bash
stress --fork 50 --timeout 20
```
Genera 50 procesos hijos que bifurcan otros procesos, durante 20 segundos.

---

### **Instalación del comando `stress`**
Si no está instalado en tu sistema, puedes añadirlo con el gestor de paquetes correspondiente:
- **Debian/Ubuntu:**
  ```bash
  sudo apt install stress
 

---

### **Alternativa: `stress-ng`**
- Una versión más avanzada de `stress` es **`stress-ng`**, que incluye más opciones y permite pruebas específicas en hardware, como GPUs, baterías, etc.
- Ejemplo:
  ```bash
  stress-ng --cpu 4 --timeout 30s
  ```

---
