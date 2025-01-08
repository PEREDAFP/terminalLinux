### Sesión de Clase: Uso del Bucle `for` en Shell Linux

#### **Objetivo de la Clase**
- Comprender el uso del bucle `for` en shell scripting de Linux.
- Explorar las diferencias entre distintos intérpretes (Bash, Zsh, etc.).
- Usar el bucle `for` para resolver problemas prácticos.

---

### **Sección 1: Introducción al Bucle `for`**

El bucle `for` es una estructura de control que permite iterar sobre una lista de elementos o ejecutar un bloque de comandos varias veces. Es especialmente útil para automatizar tareas en scripts.

**Sintaxis básica en Bash:**

```bash
for variable in lista; do
    comando1
    comando2
done
```

- **`variable`**: Recibe el valor de cada elemento en la lista.
- **`lista`**: Conjunto de valores a iterar, que puede ser una lista explícita, una expansión de rango o el resultado de un comando.
- **`comando1`, `comando2`**: Comandos que se ejecutan para cada valor de la lista.

---

### **Sección 2: Ejemplos Prácticos**

#### **Ejemplo 1: Iterar sobre una lista fija**
```bash
for color in rojo verde azul; do
    echo "El color es $color"
done
```

**Salida:**
```
El color es rojo
El color es verde
El color es azul
```

#### **Ejemplo 2: Usar un rango de números**
```bash
for i in {1..5}; do
    echo "Número: $i"
done
```

**Salida:**
```
Número: 1
Número: 2
Número: 3
Número: 4
Número: 5
```

#### **Ejemplo 3: Iterar sobre archivos**
```bash
for archivo in *.txt; do
    echo "Procesando $archivo"
done
```

---

### **Sección 3: Variaciones entre Intérpretes**

1. **Bash (Bourne Again Shell):**
   - Soporta la expansión de rangos `{1..5}` y expresiones como `{a..z}`.
   - Ejemplo: `for i in {1..5..2}; do echo $i; done` (incrementos de 2).

2. **Zsh (Z Shell):**
   - Similar a Bash, pero más estricto en algunos aspectos.
   - Admite `{1..5}`, pero puede requerir habilitar ciertas opciones.

3. **POSIX sh (Shell):**
   - Más simple, no soporta rangos `{}`.
   - Se usa `seq` para iterar:
     ```bash
     for i in $(seq 1 5); do
         echo $i
     done
     ```

4. **Fish Shell:**
   - Sintaxis diferente:
     ```fish
     for i in 1 2 3 4 5
         echo $i
     end
     ```

---

### **Sección 4: Casos Comunes y Errores**

1. **Lista Vacía**
   - Si la lista está vacía, el cuerpo del bucle no se ejecuta.
   ```bash
   for i in ""; do
       echo "Esto no se imprimirá"
   done
   ```

2. **Cuidado con los comodines**
   - Al usar `*.txt`, asegúrate de que haya archivos coincidentes, o el bucle intentará usar el comodín literal como entrada.

---

### **Ejercicios Propuestos**

1. Escribe un script que:
   - Itere sobre los números del 1 al 10.
   - Imprima si el número es par o impar.

2. Crea un script para renombrar todos los archivos `.txt` en un directorio añadiendo el prefijo `backup_`.


---
