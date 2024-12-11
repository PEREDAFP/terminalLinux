### **Sesión: Ampliación sesión `if` en Programación Shell**



### **1. Estructura básica de `if`**

La estructura general de un bloque `if` en Shell es:

```bash
if [ condición ]; then
    # Bloque de código si la condición es verdadera
fi
```

- La **condición** se evalúa entre corchetes `[ ]`.
- Si la condición es verdadera (código de salida 0), el bloque dentro de `then` se ejecuta.
- Si es falsa (código de salida distinto de 0), el bloque se omite.

---

#### **Ejemplo básico:**

```bash
#!/bin/bash

numero=10

if [ $numero -gt 5 ]; then
    echo "El número es mayor que 5."
fi
```

**Salida:**
```
El número es mayor que 5.
```

En este caso, `[ $numero -gt 5 ]` evalúa si el número es mayor que 5. Como la condición es verdadera, se imprime el mensaje.

---

### **2. Sintaxis de `if-else`**

Para manejar casos donde la condición no se cumple, usamos `else`:

```bash
if [ condición ]; then
    # Código si la condición es verdadera
else
    # Código si la condición es falsa
fi
```

#### **Ejemplo:**

```bash
#!/bin/bash

numero=3

if [ $numero -gt 5 ]; then
    echo "El número es mayor que 5."
else
    echo "El número no es mayor que 5."
fi
```

**Salida:**
```
El número no es mayor que 5.
```

---

### **3. Sintaxis de `if-elif-else`**

Para manejar múltiples condiciones, usamos `elif` (abreviatura de *else if*):

```bash
if [ condición1 ]; then
    # Código si condición1 es verdadera
elif [ condición2 ]; then
    # Código si condición2 es verdadera
else
    # Código si ninguna condición es verdadera
fi
```

#### **Ejemplo:**

```bash
#!/bin/bash

numero=5

if [ $numero -gt 10 ]; then
    echo "El número es mayor que 10."
elif [ $numero -eq 5 ]; then
    echo "El número es igual a 5."
else
    echo "El número es menor que 10 y no es 5."
fi
```

**Salida:**
```
El número es igual a 5.
```

---

### **4. Tipos de condiciones**

#### **Comparación numérica**

| Operador  | Significado             |
|-----------|-------------------------|
| `-eq`     | Igual a                |
| `-ne`     | No igual a             |
| `-gt`     | Mayor que              |
| `-lt`     | Menor que              |
| `-ge`     | Mayor o igual que      |
| `-le`     | Menor o igual que      |

#### **Ejemplo:**

```bash
if [ $a -eq $b ]; then
    echo "a es igual a b."
fi
```

#### **Comparación de cadenas**

| Operador  | Significado             |
|-----------|-------------------------|
| `=`       | Igual a                |
| `!=`      | No igual a             |
| `-z`      | Longitud de la cadena es 0 |
| `-n`      | Longitud de la cadena no es 0 |

#### **Ejemplo:**

```bash
cadena="Hola"

if [ "$cadena" = "Hola" ]; then
    echo "La cadena es 'Hola'."
fi
```

#### **Comprobación de archivos**

| Operador  | Significado                     |
|-----------|---------------------------------|
| `-e`      | El archivo existe              |
| `-f`      | Es un archivo regular          |
| `-d`      | Es un directorio               |
| `-r`      | Es legible                     |
| `-w`      | Es escribible                  |
| `-x`      | Es ejecutable                  |

#### **Ejemplo:**

```bash
if [ -f "/etc/passwd" ]; then
    echo "El archivo /etc/passwd existe."
fi
```

---

### **5. Operadores lógicos**

Podemos combinar condiciones usando:

- **AND (`-a` o `&&`)**: Ambas condiciones deben ser verdaderas.
- **OR (`-o` o `||`)**: Al menos una condición debe ser verdadera.
- **NOT (`!`)**: Invierte el valor de verdad de la condición.

#### **Ejemplo con AND:**

```bash
if [ $a -gt 0 -a $b -gt 0 ]; then
    echo "Ambos números son positivos."
fi
```

#### **Ejemplo con OR:**

```bash
if [ $a -eq 0 -o $b -eq 0 ]; then
    echo "Al menos uno de los números es 0."
fi
```

#### **Ejemplo con NOT:**

```bash
if [ ! -f "/etc/passwd" ]; then
    echo "El archivo /etc/passwd no existe."
fi
```

---

### **6. Ejercicios prácticos**

#### **Ejercicio 1: Verificar si un número es par o impar**

Escribe un script que pida al usuario un número y determine si es par o impar.

```bash
#!/bin/bash

echo "Introduce un número:"
read numero

if [ $((numero % 2)) -eq 0 ]; then
    echo "El número $numero es par."
else
    echo "El número $numero es impar."
fi
```

---

#### **Ejercicio 2: Verificar permisos de un archivo**

Escribe un script que pida al usuario un nombre de archivo y verifique si tiene permisos de lectura, escritura y ejecución.

```bash
#!/bin/bash

echo "Introduce el nombre del archivo:"
read archivo

if [ -e "$archivo" ]; then
    echo "El archivo existe."
    [ -r "$archivo" ] && echo "Tiene permiso de lectura."
    [ -w "$archivo" ] && echo "Tiene permiso de escritura."
    [ -x "$archivo" ] && echo "Tiene permiso de ejecución."
else
    echo "El archivo no existe."
fi
```

---

#### **Ejercicio 3: Comparar dos cadenas**

Escribe un script que compare dos cadenas ingresadas por el usuario.

```bash
#!/bin/bash

echo "Introduce la primera cadena:"
read cadena1
echo "Introduce la segunda cadena:"
read cadena2

if [ "$cadena1" = "$cadena2" ]; then
    echo "Las cadenas son iguales."
else
    echo "Las cadenas son diferentes."
fi
```

---
