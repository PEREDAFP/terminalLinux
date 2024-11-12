Las variables de entorno en PowerShell son útiles para almacenar información del sistema, como rutas de archivos, configuraciones del usuario, etc. Estas variables permiten interactuar con configuraciones preexistentes o definir nuevas que se pueden usar en scripts o sesiones. A continuación, se presenta una sesión de PowerShell para trabajar con variables de entorno.

### 1. **Ver todas las variables de entorno**

   ```powershell
   Get-ChildItem Env:
   ```

### 2. **Obtener el valor de una variable de entorno específica**

   Para obtener el valor de una variable como `PATH`:

   ```powershell
   $env:PATH
   ```

### 3. **Crear una nueva variable de entorno (solo para la sesión actual)**

   ```powershell
   $env:MI_VARIABLE = "Este es el valor de mi variable"
   ```

### 4. **Modificar una variable de entorno existente**

   Para añadir una nueva ruta al `PATH`:

   ```powershell
   $env:PATH += ";C:\Nueva\Ruta"
   ```

### 5. **Eliminar una variable de entorno**

   ```powershell
   Remove-Item Env:MI_VARIABLE
   ```

### 6. **Comprobar si una variable de entorno existe**

   ```powershell
   Test-Path Env:MI_VARIABLE
   ```

### 7. **Listar solo nombres de las variables de entorno**

   ```powershell
   Get-ChildItem Env: | ForEach-Object { $_.Name }
   ```

### 8. **Guardar variables de entorno en un archivo**

   Esto crea un archivo `VariablesEntorno.txt` con todas las variables actuales:

   ```powershell
   Get-ChildItem Env: > C:\Ruta\VariablesEntorno.txt
   ```

### 9. **Leer una variable de entorno desde un archivo**

   Supongamos que el archivo contiene una lista de variables y queremos cargar una específica:

   ```powershell
   $contenido = Get-Content -Path C:\Ruta\VariablesEntorno.txt
   $env:MI_VARIABLE = $contenido[0] # Asigna el primer valor del archivo a la variable
   ```

### 10. **Usar variables de entorno en rutas de archivo**

   Las variables de entorno como `USERPROFILE` se pueden usar en rutas de archivo:

   ```powershell
   Get-ChildItem "$env:USERPROFILE\Documentos"
   ```

### 11. **Crear una variable de entorno que persista entre sesiones**

   Se puede crear una variable persistente (requiere privilegios de administrador) usando el registro:

   ```powershell
   [System.Environment]::SetEnvironmentVariable("MI_VARIABLE_PERSISTENTE", "Valor Persistente", "Machine")
   ```

### 12. **Verificar los valores predeterminados de sistema**

   Algunas variables, como `COMPUTERNAME`, `USERNAME` y `OS`, contienen información predeterminada del sistema:

   ```powershell
   $env:COMPUTERNAME
   $env:USERNAME
   $env:OS
   ```

### 13. **Concatenar el valor de una variable de entorno a otra**

   Concatenar dos variables como `MI_VARIABLE` y `USERNAME`:

   ```powershell
   $env:NUEVA_VAR = "$env:MI_VARIABLE-$env:USERNAME"
   ```

### 14. **Listar variables de entorno que contienen una palabra específica**

   ```powershell
   Get-ChildItem Env: | Where-Object { $_.Name -match "PATH" }
   ```

### 15. **Eliminar todas las variables de entorno personalizadas**

   ```powershell
   Get-ChildItem Env: | Where-Object { $_.Name -match "MI_VARIABLE" } | ForEach-Object { Remove-Item -Path "Env:$($_.Name)" }
   ```

### 16. **Crear una variable de entorno temporal para un script**

   Definir variables que se usan solo en el script actual:

   ```powershell
   $env:TEMP_VAR = "Valor temporal"
   ```

### 17. **Guardar y recuperar la configuración del `PATH`**

   Guardar el `PATH` actual en una variable y luego restaurarlo:

   ```powershell
   $oldPath = $env:PATH
   $env:PATH += ";C:\NuevaRuta"
   # Restaura
   $env:PATH = $oldPath
   ```

### 18. **Usar variables de entorno en comandos condicionales**

   ```powershell
   if ($env:USERNAME -eq "Administrador") {
       Write-Output "Eres el Administrador"
   } else {
       Write-Output "No tienes privilegios de administrador"
   }
   ```

### 19. **Hacer referencia a variables de entorno en PowerShell desde otro programa**

   Definir y utilizar una variable que puede ser leída desde otro programa:

   ```powershell
   [System.Environment]::SetEnvironmentVariable("VAR_OTRO_PROGRAMA", "ValorCompartido", "User")
   ```

### 20. **Restaurar variables de entorno a sus valores predeterminados**

   Para restaurar `PATH` o cualquier otra variable:

   ```powershell
   [System.Environment]::SetEnvironmentVariable("PATH", $null, "User")
   ```

