Los módulos en PowerShell se pueden clasificar en diferentes tipos según su implementación y distribución. Resumimos las principales diferencias:

1. **Script Modules (.psm1)**
   - Son los más simples y comunes
   - Contienen código PowerShell puro
   - Fáciles de crear y modificar
   - Ejemplo de uso:
   ```powershell
   # Crear un módulo script básico
   New-ModuleManifest -Path .\MiModulo.psd1
   # El código va en MiModulo.psm1
   ```

2. **Binary/Compiled Modules (.dll)**
   - Escritos en lenguajes como C# o VB.NET
   - Compilados como ensamblados .NET
   - Mayor rendimiento que los módulos script
   - Más difíciles de modificar al estar compilados
   - Requieren conocimientos de programación .NET

3. **Manifest Modules (.psd1)**
   - Archivos de manifiesto que describen un módulo
   - Contienen metadatos como versión, dependencias, autor
   - Pueden cargar otros tipos de módulos
   - Ejemplo:
   ```powershell
   # Ver el contenido de un manifiesto
   Test-ModuleManifest -Path .\MiModulo.psd1
   ```

4. **Dynamic Modules**
   - Creados en memoria durante la ejecución
   - No existen como archivos en el disco
   - Útiles para automatización temporal
   - Ejemplo:
   ```powershell
   # Crear un módulo dinámico
   New-Module -Name "ModuloDinamico" -ScriptBlock {
       function Get-Ejemplo { Write-Host "Hola" }
   }
   ```

5. **Workflow Modules**
   - Contienen workflows de PowerShell
   - Diseñados para tareas largas y distribuidas
   - Soportan persistencia y recuperación
   - Capacidad de ejecución paralela

Comparación de características principales:

```powershell
# Verificar el tipo de un módulo
Get-Module | Select-Object Name, ModuleType

# Listar módulos por tipo
Get-Module -ListAvailable | Group-Object ModuleType
```

Ubicaciones típicas de los módulos:
1. **Sistema**
   ```powershell
   $env:SystemRoot\System32\WindowsPowerShell\v1.0\Modules
   ```

2. **Usuario**
   ```powershell
   $HOME\Documents\WindowsPowerShell\Modules
   ```

3. **Personalizados**
   ```powershell
   # Añadir una ruta personalizada
   $env:PSModulePath += ";C:\MisModulos"
   ```

Algunas diferencias clave en el uso:

1. **Instalación**:
   - Script/Manifest: Simplemente copiar archivos
   - Binary: Requieren instalación o registro en GAC
   ```powershell
   # Instalar un módulo desde PowerShell Gallery
   Install-Module -Name "NombreModulo"
   ```

2. **Mantenimiento**:
   - Script: Fácil de modificar con editor de texto
   - Binary: Requiere recompilación
   ```powershell
   # Actualizar un módulo
   Update-Module -Name "NombreModulo"
   ```

3. **Rendimiento**:
   - Binary: Mejor rendimiento
   - Script: Más lentos pero más flexibles
   ```powershell
   # Medir rendimiento
   Measure-Command { Import-Module "NombreModulo" }
   ```

4. **Depuración**:
   - Script: Más fácil de debuggear
   - Binary: Requiere herramientas específicas
   ```powershell
   # Depurar un módulo script
   Set-PSBreakpoint -Script .\MiModulo.psm1 -Line 10
   ```