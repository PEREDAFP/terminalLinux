PowerShell es una herramienta de automatización y administración de sistemas de Microsoft que combina la funcionalidad de una línea de comandos y un lenguaje de scripting. Basado en .NET, permite a los administradores de sistemas realizar tareas de administración en múltiples plataformas, como Windows, Linux y macOS. Con PowerShell, es posible realizar operaciones en el sistema de archivos, gestionar procesos, servicios y mucho más, simplificando y automatizando tareas repetitivas.

**20 actividades** para trabajar con archivos, carpetas y otros comandos esenciales en PowerShell:

### 1. **Listar el contenido de un directorio**
   ```powershell
   Get-ChildItem -Path "C:\Ruta\Directorio"
   ```

### 2. **Copiar archivos**
   ```powershell
   Copy-Item -Path "C:\Ruta\Archivo.txt" -Destination "C:\Ruta\NuevaUbicacion"
   ```

### 3. **Mover archivos**
   ```powershell
   Move-Item -Path "C:\Ruta\Archivo.txt" -Destination "C:\Ruta\NuevaUbicacion"
   ```

### 4. **Borrar archivos**
   ```powershell
   Remove-Item -Path "C:\Ruta\Archivo.txt"
   ```

### 5. **Crear un directorio**
   ```powershell
   New-Item -Path "C:\Ruta\NuevaCarpeta" -ItemType Directory
   ```

### 6. **Eliminar un directorio**
   ```powershell
   Remove-Item -Path "C:\Ruta\Carpeta" -Recurse -Force
   ```

### 7. **Renombrar un archivo o directorio**
   ```powershell
   Rename-Item -Path "C:\Ruta\ArchivoViejo.txt" -NewName "ArchivoNuevo.txt"
   ```

### 8. **Redireccionar la salida de un comando a un archivo**
   ```powershell
   Get-Process > "C:\Ruta\Salida.txt"
   ```

### 9. **Concatenar salida de comando a un archivo**
   ```powershell
   Get-Date >> "C:\Ruta\Salida.txt"
   ```

### 10. **Filtrar contenido en archivos (similar a `grep` en Linux)**
   ```powershell
   Select-String -Path "C:\Ruta\Archivo.txt" -Pattern "TextoABuscar"
   ```

### 11. **Mostrar archivos ocultos en un directorio**
   ```powershell
   Get-ChildItem -Path "C:\Ruta\Directorio" -Force
   ```

### 12. **Crear un archivo oculto**
   ```powershell
   New-Item -Path "C:\Ruta\ArchivoOculto.txt" -ItemType File
   (Get-Item "C:\Ruta\ArchivoOculto.txt").Attributes = "Hidden"
   ```

### 13. **Cambiar el nombre a múltiples archivos**
   ```powershell
   Get-ChildItem -Path "C:\Ruta\Directorio\*.txt" | ForEach-Object { Rename-Item $_ -NewName ($_.Name -replace "Viejo", "Nuevo") }
   ```

### 14. **Crear un archivo de texto**
   ```powershell
   New-Item -Path "C:\Ruta\Archivo.txt" -ItemType File
   ```

### 15. **Escribir texto en un archivo**
   ```powershell
   Set-Content -Path "C:\Ruta\Archivo.txt" -Value "Este es el contenido"
   ```

### 16. **Añadir texto a un archivo existente**
   ```powershell
   Add-Content -Path "C:\Ruta\Archivo.txt" -Value "Texto adicional"
   ```

### 17. **Leer el contenido de un archivo**
   ```powershell
   Get-Content -Path "C:\Ruta\Archivo.txt"
   ```

### 18. **Buscar archivos según una extensión específica**
   ```powershell
   Get-ChildItem -Path "C:\Ruta\Directorio" -Filter *.txt
   ```

### 19. **Verificar si un archivo o carpeta existe**
   ```powershell
   Test-Path -Path "C:\Ruta\ArchivoOCarpeta"
   ```

### 20. **Obtener el tamaño de un archivo**
   ```powershell
   (Get-Item "C:\Ruta\Archivo.txt").Length
   ```

