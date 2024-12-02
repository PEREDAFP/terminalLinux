### **Respuestas a las actividades**

---

#### **1. Identificar y diferenciar RAID por hardware y software.**
- **Respuesta:**
  - RAID por hardware utiliza controladores dedicados, mientras que RAID por software depende del sistema operativo.
  - El hardware ofrece mejor rendimiento y es independiente del sistema operativo, pero es más costoso.
  - El software es más económico y fácil de configurar, pero consume recursos del sistema.

---

#### **2. Simular un RAID 0 en una máquina virtual utilizando `mdadm`.**
- **Respuesta:**
  - Comandos utilizados:
    ```bash
    sudo mdadm --create --verbose /dev/md0 --level=0 --raid-devices=2 /dev/sdb /dev/sdc
    ```
  - Resultado: Los datos se distribuyen entre ambos discos, mejorando el rendimiento, pero no hay redundancia.

---

#### **3. Configurar un RAID 1 y probar la recuperación de datos tras la falla de un disco.**
- **Respuesta:**
  - Configuración:
    ```bash
    sudo mdadm --create /dev/md0 --level=1 --raid-devices=2 /dev/sdb /dev/sdc
    ```
  - Simulación de falla:
    ```bash
    sudo mdadm --fail /dev/md0 /dev/sdb
    ```
  - Resultado: RAID 1 sigue funcionando con el disco restante, garantizando la disponibilidad de los datos.

---

#### **4. Analizar los requisitos de un RAID 5 y configurarlo en un entorno simulado.**
- **Respuesta:**
  - Requisitos: Al menos 3 discos. Ofrece redundancia con un impacto moderado en la capacidad de almacenamiento.
  - Configuración:
    ```bash
    sudo mdadm --create /dev/md0 --level=5 --raid-devices=3 /dev/sdb /dev/sdc /dev/sdd
    ```
  - Resultado: Distribución de datos y paridad, permitiendo la recuperación si falla un disco.

---

#### **5. Investigar casos de uso reales de RAID en entornos empresariales.**
- **Respuesta:**
  - RAID 0: Usado en aplicaciones donde el rendimiento es crítico, como edición de video.
  - RAID 1: Usado para datos financieros o médicos donde la redundancia es prioritaria.
  - RAID 5/6: Común en servidores empresariales donde se necesita redundancia y capacidad eficiente.
  - RAID 10: Usado en bases de datos críticas por su rendimiento y tolerancia a fallos.

---

#### **6. Dibujar un esquema que represente los niveles RAID 0, 1, 5 y 10.**
- **Respuesta:**
  - RAID 0: Los bloques de datos se distribuyen entre los discos.
  - RAID 1: Los datos se duplican en dos discos.
  - RAID 5: Los bloques de datos y paridad se distribuyen entre tres o más discos.
  - RAID 10: Combina espejado (RAID 1) con división de datos (RAID 0).

*(Este dibujo puede ser hecho en papel o digital, pero la explicación textual cubre la representación.)*

---

#### **7. Simular un RAID 6 y medir el rendimiento comparado con RAID 5.**
- **Respuesta:**
  - Configuración RAID 6:
    ```bash
    sudo mdadm --create /dev/md0 --level=6 --raid-devices=4 /dev/sdb /dev/sdc /dev/sdd /dev/sde
    ```
  - Observación:
    - RAID 5: Más rápido en escritura porque solo almacena un bloque de paridad.
    - RAID 6: Más lento debido a la doble paridad, pero ofrece mayor tolerancia a fallos.

---

#### **8. Crear un documento de ventajas e inconvenientes de cada nivel RAID.**
- **Respuesta:**
  - RAID 0: Rendimiento alto, sin redundancia.
  - RAID 1: Alta redundancia, capacidad reducida al 50%.
  - RAID 5: Buen equilibrio entre redundancia y capacidad, lenta recuperación tras fallos.
  - RAID 6: Mayor tolerancia a fallos que RAID 5, pero con menor rendimiento.
  - RAID 10: Excelente rendimiento y redundancia, costoso en términos de discos.

---

#### **9. Realizar un análisis de costo-beneficio entre RAID 5 y RAID 10 para un proyecto.**
- **Respuesta:**
  - RAID 5: Más económico en términos de capacidad usable, ideal para almacenamiento masivo con accesos moderados.
  - RAID 10: Costoso porque necesita el doble de discos, pero adecuado para bases de datos o sistemas con altas demandas de rendimiento y redundancia.

---

#### **10. Debatir la necesidad de RAID en dispositivos personales versus servidores.**
- **Respuesta:**
  - **Dispositivos personales:**
    - Generalmente no necesitan RAID, ya que las copias de seguridad en la nube son suficientes.
    - RAID puede ser útil para entusiastas que buscan rendimiento (RAID 0) o redundancia (RAID 1).
  - **Servidores:**
    - RAID es esencial para garantizar la disponibilidad y redundancia de datos críticos.
    - Los niveles RAID más utilizados son RAID 5, 6 y 10 según las necesidades específicas.

