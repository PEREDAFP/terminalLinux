### **Sesión: RAID (Redundant Array of Independent Disks)**

#### **Introducción a RAID**
RAID (Redundant Array of Independent Disks) es una tecnología que combina múltiples discos duros en una única unidad lógica para mejorar el rendimiento, la redundancia de datos o ambas. Se utiliza tanto en hardware como en software y tiene varias configuraciones llamadas "niveles de RAID."

---

### **1. Tipos de RAID: Software y Hardware**

#### **RAID por hardware:**
- **Descripción:**
  - Se implementa usando controladores RAID dedicados, tarjetas específicas o funcionalidades integradas en la placa base.
  - El controlador se encarga de gestionar las operaciones RAID, haciendo que el sistema operativo lo vea como un único disco lógico.
- **Ventajas:**
  - Mejor rendimiento, ya que el controlador libera al sistema operativo de las operaciones RAID.
  - Es independiente del sistema operativo.
- **Inconvenientes:**
  - Más costoso debido al hardware dedicado.
  - Dependencia del controlador: si falla, puede ser difícil recuperar los datos.

#### **RAID por software:**
- **Descripción:**
  - Utiliza el sistema operativo para gestionar las operaciones RAID.
  - Ejemplos: `mdadm` en Linux, Storage Spaces en Windows.
- **Ventajas:**
  - Económico, no requiere hardware adicional.
  - Fácil de configurar.
- **Inconvenientes:**
  - Depende de la CPU del sistema, lo que puede impactar en el rendimiento.
  - Generalmente menos eficiente que el hardware RAID.

---

### **2. Niveles de RAID**

#### **RAID 0: División de datos (Striping)**
- **Descripción:** Divide los datos en bloques y los distribuye entre varios discos.
- **Ventajas:**
  - Excelente rendimiento.
  - Uso completo de la capacidad de los discos.
- **Inconvenientes:**
  - Sin redundancia: la falla de un disco significa pérdida total de datos.
  
#### **RAID 1: Espejo (Mirroring)**
- **Descripción:** Duplica los datos en dos discos.
- **Ventajas:**
  - Alta redundancia, ideal para datos críticos.
  - Fácil recuperación en caso de falla.
- **Inconvenientes:**
  - Capacidad efectiva reducida al 50%.

#### **RAID 5: Paridad distribuida**
- **Descripción:** Divide los datos y agrega paridad (datos de recuperación) distribuidos entre los discos.
- **Ventajas:**
  - Redundancia eficiente.
  - Equilibrio entre rendimiento y tolerancia a fallos.
- **Inconvenientes:**
  - Requiere al menos 3 discos.
  - La reconstrucción tras un fallo puede ser lenta.

#### **RAID 6: Paridad doble**
- **Descripción:** Similar a RAID 5, pero con dos bloques de paridad por cada conjunto de datos.
- **Ventajas:**
  - Soporta la falla de dos discos simultáneamente.
- **Inconvenientes:**
  - Requiere más espacio para la paridad.
  - Mayor impacto en el rendimiento.

#### **RAID 10 (1+0): Combinación de RAID 1 y RAID 0**
- **Descripción:** Combina espejado y división de datos.
- **Ventajas:**
  - Excelente rendimiento y alta redundancia.
- **Inconvenientes:**
  - Requiere un número par de discos, mínimo 4.
  - Costoso en términos de capacidad efectiva.

---

### **3. Ventajas y desventajas generales**

#### **Ventajas:**
- Redundancia: aumenta la tolerancia a fallos.
- Rendimiento: mejora la velocidad de lectura y escritura.
- Escalabilidad: permite combinar discos de distintas capacidades.

#### **Inconvenientes:**
- Complejidad: la configuración y recuperación pueden ser complicadas.
- Costos: requiere más discos y, en el caso del RAID por hardware, componentes adicionales.
- No sustituye el backup: aunque mejora la disponibilidad, un error humano o virus puede afectar a todos los discos.

---

### **4. Actividades propuestas**

1. **Identificar y diferenciar RAID por hardware y software.**
   - **Objetivo:** Entender las diferencias clave entre ambos métodos.

2. **Simular un RAID 0 en una máquina virtual utilizando `mdadm`.**
   - **Objetivo:** Aprender a configurar y comprobar un RAID básico.

3. **Configurar un RAID 1 y probar la recuperación de datos tras la falla de un disco.**
   - **Objetivo:** Comprender cómo funciona el espejado y la tolerancia a fallos.

4. **Analizar los requisitos de un RAID 5 y configurarlo en un entorno simulado.**
   - **Objetivo:** Practicar la configuración y entender el uso de paridad.

5. **Investigar casos de uso reales de RAID en entornos empresariales.**
   - **Objetivo:** Relacionar la teoría con la práctica en infraestructuras reales.

6. **Dibujar un esquema que represente los niveles RAID 0, 1, 5 y 10.**
   - **Objetivo:** Visualizar cómo se distribuyen los datos en los diferentes niveles.

7. **Simular un RAID 6 y medir el rendimiento comparado con RAID 5.**
   - **Objetivo:** Evaluar las diferencias de rendimiento y tolerancia a fallos.

8. **Crear un documento de ventajas e inconvenientes de cada nivel RAID.**
   - **Objetivo:** Consolidar el aprendizaje teórico.

9. **Realizar un análisis de costo-beneficio entre RAID 5 y RAID 10 para un proyecto.**
   - **Objetivo:** Evaluar cuál es más adecuado según un escenario específico.

10. **Debatir la necesidad de RAID en dispositivos personales versus servidores.**
    - **Objetivo:** Reflexionar sobre cuándo y dónde se justifica el uso de RAID.

