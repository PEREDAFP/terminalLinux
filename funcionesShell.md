
### Objetivos de la sesión:
1. **Entender qué son las funciones en Shell.**
2. **Aprender a declarar funciones en un script Shell.**
3. **Pasar parámetros a funciones y cómo retornan valores.**
4. **Ver ejemplos prácticos de funciones en Shell.**

---

### **1. Introducción a las funciones en Shell**

En Shell, una función es un bloque de código que realiza una tarea específica. Una función se define una sola vez, pero puede ser invocada (o llamada) varias veces durante la ejecución del script. Usar funciones permite estructurar mejor el código y hacerlo más legible y reutilizable.

#### **Sintaxis básica de una función en Shell**
```bash
nombre_funcion() {
    # Cuerpo de la función
    # Instrucciones a ejecutar
}
```

### **2. Definiendo y llamando funciones**

#### **Definir una función:**
```bash
mi_funcion() {
    echo "¡Hola, soy una función en Shell!"
}
```

#### **Llamar a una función:**
```bash
mi_funcion  # Solo escribes el nombre de la función para llamarla
```

### **3. Funciones con parámetros**

Puedes pasar parámetros a las funciones para hacerlas más flexibles. Los parámetros que pasan a una función se acceden dentro de ella mediante `$1`, `$2`, ..., `$N` (para el primer, segundo, ..., N-ésimo argumento).

#### **Ejemplo de función con parámetros:**
```bash
saludar() {
    echo "Hola, $1! Bienvenido a la programación en Shell."
}

saludar "Carlos"  # Salida: Hola, Carlos! Bienvenido a la programación en Shell.
```

En este caso, `$1` hace referencia al primer parámetro, en este caso `"Carlos"`, que es pasado al invocar la función.

### **4. Funciones con retorno de valores**

Las funciones en Shell no devuelven valores de manera directa como en otros lenguajes, pero puedes usar `echo` para imprimir el valor y capturarlo en una variable al invocar la función.

#### **Ejemplo de función que devuelve un valor:**

```bash
suma() {
    local resultado=$(( $1 + $2 ))  # Suma de dos números
    echo $resultado  # Imprime el resultado
}

# Llamar la función y almacenar el resultado en una variable
resultado_suma=$(suma 5 7)
echo "El resultado de la suma es: $resultado_suma"
```

En este ejemplo, la función `suma` toma dos parámetros, los suma y devuelve el resultado usando `echo`. Luego, el valor retornado se captura con `$( )` y se almacena en la variable `resultado_suma`.

### **5. Variables locales y globales dentro de funciones**

- Las **variables globales** son accesibles desde cualquier parte del script.
- Las **variables locales** solo son accesibles dentro de la función donde se definen.

#### **Ejemplo con variables locales y globales:**

```bash
# Variable global
mensaje="Hola desde el script global"

mi_funcion() {
    # Variable local
    local mensaje="Hola desde la función local"
    echo $mensaje  # Se imprimirá "Hola desde la función local"
}

echo $mensaje  # Se imprimirá "Hola desde el script global"
mi_funcion      # Se imprimirá "Hola desde la función local"
```

En este ejemplo, `mensaje` tiene un valor global, pero dentro de la función se declara una variable `mensaje` local, que sobrescribe la global solo dentro de la función.

### **6. Funciones con validación de parámetros**

Es una buena práctica validar los parámetros antes de usarlos dentro de las funciones. Por ejemplo, podrías querer verificar si se pasó un número o si se proporcionaron los parámetros correctos.

#### **Ejemplo de validación:**

```bash
dividir() {
    if [ $# -ne 2 ]; then
        echo "Se requieren exactamente 2 parámetros."
        return 1
    fi

    if [ $2 -eq 0 ]; then
        echo "Error: División por cero no permitida."
        return 1
    fi

    resultado=$(( $1 / $2 ))
    echo "El resultado de la división es: $resultado"
}

dividir 10 2   # Salida: El resultado de la división es: 5
dividir 10 0   # Salida: Error: División por cero no permitida.
```

En este ejemplo, la función `dividir` valida si se pasaron dos parámetros y si el divisor es cero. Si alguna de estas condiciones no se cumple, se muestra un mensaje de error.

### **7. Funciones recursivas**

Las funciones en Shell pueden llamarse a sí mismas, lo que se conoce como recursión. Aunque no es común en Shell, es posible.

#### **Ejemplo de función recursiva:**
```bash
factorial() {
    if [ $1 -le 1 ]; then
        echo 1
    else
        local prev=$(factorial $(( $1 - 1 )))
        echo $(( $1 * prev ))
    fi
}

echo "El factorial de 5 es: $(factorial 5)"
```

En este caso, la función `factorial` se llama a sí misma para calcular el factorial de un número.

### **8. Resumen y buenas prácticas**

- **Modularidad**: Las funciones permiten organizar el código en bloques más pequeños, lo que facilita su mantenimiento y reutilización.
- **Legibilidad**: Usar funciones mejora la legibilidad del código, ya que puedes darles nombres descriptivos que reflejan su propósito.
- **Reusabilidad**: Las funciones te permiten reutilizar el mismo bloque de código varias veces sin tener que escribirlo repetidamente.
- **Validación**: Siempre es recomendable validar los parámetros de entrada para evitar errores en la ejecución del script.

---

### **Ejercicio práctico**

Escribe un script que utilice funciones para realizar las siguientes tareas:

1. Crear una función que calcule el área de un círculo, tomando el radio como parámetro.
2. Crear una función que imprima un mensaje de bienvenida.
3. Llamar a ambas funciones desde el script principal, pasando los parámetros correspondientes.

---
