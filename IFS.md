En los scripts de Shell, la variable `IFS` (Internal Field Separator) define los delimitadores que el shell usa para dividir palabras o campos de entrada. En los bucles `while`, se usa a menudo para controlar cómo se dividen las líneas o palabras al leer datos, especialmente cuando se usa `read`.

### 📌 **Usos comunes de `IFS=` en bucles `while`**

#### 1️⃣ **Leer líneas completas incluyendo espacios**

Por defecto, `read` divide las líneas en palabras separadas por espacios, tabulaciones o saltos de línea. Para evitarlo y leer la línea completa, podemos usar `IFS=`.

```bash
#!/bin/bash
while IFS= read -r linea; do
    echo "Línea completa: '$linea'"
done < archivo.txt
```

🔹 **Explicación**:

- `IFS=` evita que `read` divida la línea en palabras.
- `-r` evita que los backslashes (`\`) sean interpretados como caracteres de escape.

---

#### 2️⃣ **Leer un archivo CSV separando por comas**

Podemos cambiar `IFS` para dividir una línea en campos específicos.

```bash
#!/bin/bash
while IFS=',' read -r nombre edad ciudad; do
    echo "Nombre: $nombre, Edad: $edad, Ciudad: $ciudad"
done < datos.csv
```

🔹 **Explicación**:

- `IFS=','` hace que `read` divida la línea en partes usando `,` como separador.
- Si `datos.csv` tiene:

  ```
  Juan,25,Madrid
  Ana,30,Barcelona
  ```

  Salida:

  ```
  Nombre: Juan, Edad: 25, Ciudad: Madrid
  Nombre: Ana, Edad: 30, Ciudad: Barcelona
  ```

---

#### 3️⃣ **Procesar una lista de valores separados por dos puntos (`:`)**

Esto es útil para manejar rutas en `PATH` u otros datos con separadores personalizados.

```bash
#!/bin/bash
IFS=':'
caminos="/usr/bin:/bin:/usr/local/bin"

while read -r ruta; do
    echo "Directorio: $ruta"
done <<< "$caminos"
```

🔹 **Explicación**:

- `IFS=':'` hace que `read` divida los valores usando `:` como separador.
- `<<< "$caminos"` usa redirección de `here string` para pasar la cadena al bucle.

📌 **Salida esperada**:

```
Directorio: /usr/bin
Directorio: /bin
Directorio: /usr/local/bin
```

---

#### 4️⃣ **Leer solo el primer campo de cada línea**

Si queremos solo la primera palabra de cada línea sin importar el resto, podemos ajustar `IFS`:

```bash
#!/bin/bash
while IFS=' ' read -r primer_palabra _; do
    echo "Primera palabra: $primer_palabra"
done < archivo.txt
```

🔹 **Explicación**:

- `_` ignora el resto de la línea.
- Si `archivo.txt` contiene:

  ```
  Hola mundo
  Bienvenidos a Bash
  ```

  📌 **Salida esperada**:

  ```
  Primera palabra: Hola
  Primera palabra: Bienvenidos
  ```

---

### 🚀 **Conclusión**

- `IFS=` permite **leer líneas completas** sin que los espacios dividan palabras.
- Se puede modificar para **separar valores** con otros delimitadores (`,`, `:`).
- Útil para procesar archivos CSV, variables de entorno y más.
