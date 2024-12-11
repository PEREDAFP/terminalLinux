En programación Shell, los **arrays** son estructuras que permiten almacenar múltiples valores en una sola variable. Aunque los arrays en Shell son más simples que en lenguajes como Python o C, ofrecen una manera eficiente de manejar listas de datos. Aquí aprenderemos cómo trabajar con arrays en Shell, cubriendo su creación, manipulación y usos comunes.

---

### **1. Crear un Array**

#### **Declarar un array:**
```bash
mi_array=(valor1 valor2 valor3)
```

#### **Ejemplo:**
```bash
nombres=("Juan" "María" "Carlos")
```

- Los elementos están separados por espacios.
- Se pueden usar comillas para manejar elementos con espacios en su contenido.

---

### **2. Acceder a Elementos del Array**

Puedes acceder a un elemento específico utilizando su índice, comenzando desde `0`.

#### **Ejemplo:**
```bash
echo ${mi_array[0]}  # Imprime "valor1"
echo ${nombres[1]}   # Imprime "María"
```

---

### **3. Modificar Elementos del Array**

Para modificar un elemento, simplemente asigna un nuevo valor a un índice existente.

#### **Ejemplo:**
```bash
mi_array[1]="nuevo_valor"
echo ${mi_array[1]}  # Imprime "nuevo_valor"
```

---

### **4. Añadir Elementos al Array**

Para añadir elementos, asigna un valor a un índice no utilizado.

#### **Ejemplo:**
```bash
mi_array[3]="nuevo_elemento"
echo ${mi_array[3]}  # Imprime "nuevo_elemento"
```

---

### **5. Obtener Todos los Elementos del Array**

Para imprimir todos los elementos, usa el operador `[@]` o `[*]`.

#### **Ejemplo:**
```bash
echo ${mi_array[@]}  # Imprime todos los elementos separados por espacios
echo ${mi_array[*]}  # Hace lo mismo que [@]
```

---

### **6. Obtener el Número de Elementos del Array**

Usa la sintaxis `${#mi_array[@]}` para contar los elementos.

#### **Ejemplo:**
```bash
echo "El array tiene ${#mi_array[@]} elementos."
```

---

### **7. Eliminar Elementos del Array**

Para eliminar un elemento específico, usa el comando `unset`.

#### **Ejemplo:**
```bash
unset mi_array[1]
echo ${mi_array[@]}  # El elemento en el índice 1 se elimina
```

---

### **8. Eliminar Todo el Array**

Para eliminar todo el array, usa `unset` con el nombre del array.

#### **Ejemplo:**
```bash
unset mi_array
```

---

### **9. Iterar Sobre un Array**

Puedes recorrer un array con un bucle `for`.

#### **Ejemplo:**
```bash
mi_array=("uno" "dos" "tres")

for elemento in "${mi_array[@]}"; do
    echo $elemento
done
```

**Salida:**
```
uno
dos
tres
```

---

### **10. Arrays Asociativos (en Bash 4.0 o superior)**

Los arrays asociativos permiten usar claves personalizadas en lugar de índices numéricos.

#### **Declarar un array asociativo:**
```bash
declare -A mi_array_asociativo
mi_array_asociativo[clave1]="valor1"
mi_array_asociativo[clave2]="valor2"
```

#### **Acceder a valores por clave:**
```bash
echo ${mi_array_asociativo[clave1]}  # Imprime "valor1"
```

#### **Recorrer un array asociativo:**
```bash
for clave in "${!mi_array_asociativo[@]}"; do
    echo "Clave: $clave, Valor: ${mi_array_asociativo[$clave]}"
done
```

---

### **11. Usos Comunes de Arrays en Shell**

#### **Almacenar líneas de un archivo en un array:**
```bash
mapfile -t lineas < archivo.txt
```

#### **Ejemplo de uso:**
```bash
for linea in "${lineas[@]}"; do
    echo "$linea"
done
```

---

### **12. Ejemplo Completo**

#### **Script que gestiona una lista de tareas con un array:**

```bash
#!/bin/bash

# Declarar un array vacío
declare -a tareas

# Función para mostrar las tareas
mostrar_tareas() {
    echo "Tareas actuales:"
    for tarea in "${tareas[@]}"; do
        echo "- $tarea"
    done
}

# Función para agregar una tarea
agregar_tarea() {
    echo "Escribe una nueva tarea:"
    read nueva_tarea
    tareas+=("$nueva_tarea")
    echo "Tarea agregada."
}

# Función para eliminar una tarea
eliminar_tarea() {
    echo "¿Qué tarea deseas eliminar? (escribe el número)"
    for i in "${!tareas[@]}"; do
        echo "$i: ${tareas[$i]}"
    done
    read indice
    unset tareas[$indice]
    echo "Tarea eliminada."
}

# Menú principal
while true; do
    echo "1. Mostrar tareas"
    echo "2. Agregar tarea"
    echo "3. Eliminar tarea"
    echo "4. Salir"
    read opcion

    case $opcion in
        1) mostrar_tareas ;;
        2) agregar_tarea ;;
        3) eliminar_tarea ;;
        4) break ;;
        *) echo "Opción no válida." ;;
    esac
done
```

**Salida esperada:**
Este script permite al usuario administrar una lista de tareas con opciones para mostrar, agregar y eliminar elementos del array.

---

### **Resumen**

- Los arrays son útiles para manejar múltiples valores en una variable.
- Se acceden y manipulan mediante índices numéricos o claves (en arrays asociativos).
- Ofrecen funcionalidad suficiente para tareas comunes en scripting Shell.
- Practicar su uso es clave para entender cómo aplicarlos eficientemente en tus scripts.