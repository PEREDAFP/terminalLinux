# **Sesión: Creación de un Script Shell para Obtener Información del Hardware y Guardarla en un CSV**

### 🎯 **Objetivo de la Clase**

Los alumnos aprenderán a escribir un **script Shell** para extraer información del hardware del sistema y almacenarla en un archivo **CSV** para su posterior análisis en una hoja de cálculo.

### 🛠 **Requisitos Previos**

- Conocimientos básicos de Linux y Bash.
- Uso de comandos como `grep`, `awk`, `sed`, `lscpu`, `lsblk`, `free`, `dmidecode`.

---

## 🕐 **Duración Aproximada: 1 Hora**

**1️⃣ Explicación de la estructura del script (10 min)**  
**2️⃣ Desarrollo paso a paso del script (30 min)**  
**3️⃣ Ejecución y exportación a CSV (10 min)**  
**4️⃣ Preguntas y conclusión (10 min)**

---

## **1️⃣ Explicación de la estructura del script**

El script realizará las siguientes tareas:

1. Obtener información del **procesador**.
2. Obtener la cantidad de **memoria RAM** y su tipo.
3. Obtener datos del **disco duro**.
4. Obtener información del **chipset** (si es posible).
5. Guardar estos datos en un **archivo CSV**.

El CSV permitirá importar estos datos a **Excel** o **Google Sheets**.

---

## **2️⃣ Desarrollo Paso a Paso**

### 📌 **Paso 1: Creación del script**

Creamos el archivo con:

```bash
nano hardware_info.sh
```

Añadimos la línea inicial del script:

```bash
#!/bin/bash
```

Esto indica que el script debe ejecutarse con **Bash**.

---

### 📌 **Paso 2: Obtener información del procesador**

Usamos `lscpu` para extraer el modelo del procesador:

```bash
cpu_model=$(lscpu | grep "Model name" | awk -F ':' '{print $2}' | sed 's/^ *//')
```

📌 **Explicación**:

- `lscpu` muestra información del CPU.
- `grep "Model name"` filtra la línea con el modelo del procesador.
- `awk -F ':' '{print $2}'` extrae la segunda columna (el nombre del modelo).
- `sed 's/^ *//'` elimina espacios en blanco al inicio.

---

### 📌 **Paso 3: Obtener la memoria RAM**

Usamos `free -h` para ver la RAM en GB:

```bash
ram_total=$(free -h | awk '/Mem:/ {print $2}')
```

Para conocer el tipo de memoria (DDR3, DDR4, etc.), usamos `dmidecode`:

```bash
ram_type=$(sudo dmidecode -t memory | grep "Type:" | grep -v Unknown | head -n 1 | awk -F ': ' '{print $2}')
```

📌 **Explicación**:

- `dmidecode -t memory` obtiene información de la RAM.
- `grep "Type:"` busca el tipo de memoria.
- `grep -v Unknown` excluye valores desconocidos.
- `head -n 1` toma el primer resultado.
- `awk -F ': ' '{print $2}'` extrae el valor.

---

### 📌 **Paso 4: Obtener información del disco duro**

Usamos `lsblk` para ver los discos duros conectados:

```bash
disk_info=$(lsblk -d -o NAME,SIZE,ROTA | grep -v "NAME")
```

Si queremos solo el primer disco:

```bash
disk_name=$(lsblk -d -o NAME | sed -n '2p')
disk_size=$(lsblk -d -o SIZE | sed -n '2p')
disk_type=$(lsblk -d -o ROTA | sed -n '2p')
```

📌 **Explicación**:

- `lsblk -d` muestra solo discos sin particiones.
- `-o NAME,SIZE,ROTA` selecciona el nombre, tamaño y tipo (`0` = SSD, `1` = HDD).
- `sed -n '2p'` obtiene la segunda línea (la primera es el encabezado).

---

### 📌 **Paso 5: Obtener el chipset**

Si `dmidecode` está disponible, usamos:

```bash
chipset=$(sudo dmidecode -t baseboard | grep "Product Name" | awk -F ': ' '{print $2}')
```

📌 **Explicación**:

- `dmidecode -t baseboard` obtiene información de la placa base.
- `grep "Product Name"` busca el nombre del chipset.
- `awk -F ': ' '{print $2}'` extrae el nombre.

---

### 📌 **Paso 6: Crear la línea de datos para el CSV**

Formateamos los datos para el CSV:

```bash
output="\"$cpu_model\",\"$ram_total\",\"$ram_type\",\"$disk_name\",\"$disk_size\",\"$disk_type\",\"$chipset\""
```

📌 **Explicación**:

- Separamos los valores con comas y los encerramos en comillas dobles para evitar errores.

---

### 📌 **Paso 7: Guardar en un archivo CSV**

Si el archivo no existe, agregamos la cabecera:

```bash
csv_file="hardware_info.csv"

if [ ! -f "$csv_file" ]; then
    echo "\"CPU\",\"RAM Total\",\"RAM Tipo\",\"Disco\",\"Tamaño Disco\",\"Tipo Disco\",\"Chipset\"" > "$csv_file"
fi
```

Ahora añadimos la información:

```bash
echo "$output" >> "$csv_file"
```

📌 **Explicación**:

- `if [ ! -f "$csv_file" ]; then ... fi` verifica si el archivo existe.
- Si no existe, escribe la cabecera en **CSV**.
- Luego, agregamos una nueva línea con `>>`.

---

## **3️⃣ Ejecución del Script**

Hacemos el script ejecutable:

```bash
chmod +x hardware_info.sh
```

Ejecutamos con:

```bash
./hardware_info.sh
```

Verificamos el archivo CSV:

```bash
cat hardware_info.csv
```

---

## **4️⃣ Preguntas y Conclusión**

📌 **Resumen de lo aprendido**:
✔️ Uso de comandos para obtener información del hardware.  
✔️ Procesamiento de datos con `grep`, `awk`, `sed`.  
✔️ Creación y escritura de archivos **CSV** en Bash.  
✔️ Importación del CSV en una hoja de cálculo.

---

### **Tarea para los alumnos** 🎯

Modificar el script para que también:
✅ Obtenga la versión del sistema operativo (`lsb_release -d`).  
✅ Detecte si el equipo tiene batería (`upower -i /org/freedesktop/UPower/devices/battery`).  
✅ Utilizando el script de envío a botTelegram envíe esa información a Telegram.
✅ ¿Cómo podríamos centralizar toda esa información en un fichero dentro de nuestra red? (Para alumnos de ASIR).
