
### **1. Crear una librería de funciones en Shell**

Una librería en Shell es simplemente un archivo que contiene definiciones de funciones que puedes reutilizar en diferentes scripts. Estas funciones no se ejecutan directamente al cargar el archivo; solo estarán disponibles para ser llamadas.

#### **Ejemplo: Crear una librería llamada `mis_funciones.sh`**

```bash
# Archivo: mis_funciones.sh

# Función para saludar
saludar() {
    echo "Hola, $1. ¡Bienvenido al mundo de Shell!"
}

# Función para calcular el cuadrado de un número
calcular_cuadrado() {
    local numero=$1
    echo $((numero * numero))
}
```

Guarda este archivo en una ubicación accesible para tus scripts, por ejemplo, en el mismo directorio donde está tu script principal.

---

### **2. Importar la librería en un script**

Para usar las funciones de la librería en tu script principal, puedes usar el comando `source` o el operador `.`.

#### **Ejemplo: Script principal llamado `script_principal.sh`**

```bash
#!/bin/bash

# Importar la librería
source ./mis_funciones.sh
# O alternativamente
# . ./mis_funciones.sh

# Llamar a las funciones de la librería
saludar "Carlos"

resultado=$(calcular_cuadrado 5)
echo "El cuadrado de 5 es: $resultado"
```

**Salida del script:**
```
Hola, Carlos. ¡Bienvenido al mundo de Shell!
El cuadrado de 5 es: 25
```

---

### **3. Consideraciones importantes**

#### **3.1 Ruta del archivo de la librería**
- Si el archivo de la librería está en el mismo directorio que el script, puedes usar `source ./nombre_libreria.sh` o simplemente `source nombre_libreria.sh`.
- Si está en otro directorio, debes proporcionar la ruta completa, por ejemplo:
  ```bash
  source /ruta/a/mis_funciones.sh
  ```

#### **3.2 Variables locales y globales**
- Usa la palabra clave `local` dentro de las funciones de tu librería para evitar conflictos de nombres de variables con el script principal.

---

### **4. Uso avanzado: Configurar un directorio para librerías**

Si tienes muchas librerías, puedes centralizarlas en un directorio y configurarlo como parte del entorno para simplificar su uso.

#### **Pasos:**

1. **Crear un directorio para tus librerías**
   ```bash
   mkdir ~/mis_librerias
   mv mis_funciones.sh ~/mis_librerias/
   ```

2. **Agregar el directorio a la variable de entorno `PATH` o configurarlo para importar automáticamente**
   - Agrega este código a tu archivo `~/.bashrc`:
     ```bash
     export LIBRERIAS_SHELL=~/mis_librerias
     ```
   - En tus scripts, usa esta variable:
     ```bash
     source $LIBRERIAS_SHELL/mis_funciones.sh
     ```

---

### **5. Verificación de errores al importar**
Es buena práctica verificar si el archivo de la librería existe antes de importarlo, para evitar errores si la ruta está mal.

#### **Ejemplo: Comprobación de existencia de la librería**
```bash
#!/bin/bash

LIBRERIA="./mis_funciones.sh"

if [ -f "$LIBRERIA" ]; then
    source "$LIBRERIA"
else
    echo "Error: No se encontró la librería $LIBRERIA"
    exit 1
fi
```

---

### **6. Beneficios de usar librerías en Shell**
- **Reusabilidad:** Puedes usar las mismas funciones en múltiples scripts.
- **Organización:** Mantienes tus scripts más limpios y modulares.
- **Mantenibilidad:** Las funciones compartidas se actualizan en un solo lugar.

---

### **7. Ejercicio práctico**

1. Crea una librería llamada `operaciones_matematicas.sh` que contenga las siguientes funciones:
   - `sumar` (recibe dos números y devuelve la suma).
   - `restar` (recibe dos números y devuelve la resta).
   - `multiplicar` (recibe dos números y devuelve el producto).

2. Crea un script principal llamado `calculadora.sh` que importe la librería y permita al usuario seleccionar una operación matemática para realizar.

**Librería (`operaciones_matematicas.sh`):**
```bash
sumar() {
    echo $(( $1 + $2 ))
}

restar() {
    echo $(( $1 - $2 ))
}

multiplicar() {
    echo $(( $1 * $2 ))
}
```

**Script principal (`calculadora.sh`):**
```bash
#!/bin/bash

# Importar la librería
source ./operaciones_matematicas.sh

# Solicitar operación
echo "Selecciona una operación: sumar, restar, multiplicar"
read operacion

echo "Introduce el primer número:"
read num1

echo "Introduce el segundo número:"
read num2

# Ejecutar la operación seleccionada
case $operacion in
    sumar)
        resultado=$(sumar $num1 $num2)
        ;;
    restar)
        resultado=$(restar $num1 $num2)
        ;;
    multiplicar)
        resultado=$(multiplicar $num1 $num2)
        ;;
    *)
        echo "Operación no válida."
        exit 1
        ;;
esac

echo "El resultado de $operacion es: $resultado"
```

