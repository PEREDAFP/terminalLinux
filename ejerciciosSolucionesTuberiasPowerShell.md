
### 🔍 Actividades de tuberías en PowerShell con Soluciones

1. **Listar procesos con más de 100 MB de memoria**
```powershell
Get-Process | Where-Object { $_.WorkingSet64 -gt 100MB }
```

2. **Crear un archivo oculto con información del sistema**
```powershell
$infoSistema = "Nombre PC: $env:COMPUTERNAME`nUsuario: $env:USERNAME`nSistema Operativo: $((Get-WmiObject Win32_OperatingSystem).Caption)"
$rutaArchivo = "C:\temp\.infosistema.txt"
$infoSistema | Out-File -FilePath $rutaArchivo
$file = Get-Item $rutaArchivo
$file.Attributes = 'Hidden'
```

3. **Filtrar servicios en ejecución que sean automáticos**
```powershell
Get-Service | Where-Object { $_.Status -eq 'Running' -and $_.StartType -eq 'Automatic' }
```

4. **Buscar archivos .log mayores de 10 MB**
```powershell
Get-ChildItem C:\ -Recurse -Include *.log | Where-Object { $_.Length -gt 10MB }
```

5. **Módulos de PowerShell que contengan "net"**
```powershell
Get-Module -ListAvailable | Where-Object { $_.Name -match "net" }
```

6. **Listar adaptadores de red**
```powershell
Get-NetAdapter | Where-Object { $_.Status -eq 'Up' }
```

7. **Procesos que consumen más del 50% de CPU**
```powershell
Get-Process | Where-Object { $_.CPU -gt 50 }
```

8. **Crear función para encontrar archivos grandes**
```powershell
function Find-LargeFiles {
    param(
        [long]$SizeThresholdMB = 100,
        [string]$Path = 'C:\'
    )
    Get-ChildItem -Path $Path -Recurse | 
        Where-Object { 
            $_.Length/1MB -gt $SizeThresholdMB 
        } | 
        Select-Object FullName, 
        @{Name='SizeMB';Expression={[math]::Round($_.Length/1MB,2)}}
}

# Uso
Find-LargeFiles -SizeThresholdMB 50
```

9. **Filtrar usuarios locales habilitados**
```powershell
Get-LocalUser | Where-Object { $_.Enabled -eq $true -and $_.PasswordExpired -eq $false }
```

10. **Listar directorios del sistema con más de 1000 archivos**
```powershell
Get-ChildItem C:\Windows -Directory | 
    Where-Object { (Get-ChildItem $_.FullName).Count -gt 1000 }
```

11. **Crear módulo dinámico simple**
```powershell
$miModulo = New-Module -Name "MiModuloDinamico" -ScriptBlock {
    function Get-Saludo {
        param($nombre)
        "Hola, $nombre!"
    }
    Export-ModuleMember -Function Get-Saludo
}
```

12. **Filtrar archivos modificados en los últimos 7 días**
```powershell
Get-ChildItem C:\ -Recurse | 
    Where-Object { $_.LastWriteTime -gt (Get-Date).AddDays(-7) }
```

13. **Listar procesos de aplicaciones específicas**
```powershell
$apps = @('chrome', 'firefox', 'code')
Get-Process | Where-Object { $_.Name -in $apps }
```

14. **Obtener información de módulos específicos**
```powershell
Get-Module -ListAvailable | 
    Where-Object { $_.Name -like "*net*" } | 
    Select-Object Name, Version, Path
```

15. **Crear script para monitoreo de servicios**
```powershell
function Monitor-Services {
    param(
        [string[]]$ServiciosImportantes = @('wuauserv', 'bits', 'winmgmt')
    )
    $ServiciosImportantes | ForEach-Object {
        $servicio = Get-Service $_
        [PSCustomObject]@{
            Nombre = $servicio.Name
            Estado = $servicio.Status
            TipoInicio = $servicio.StartType
        }
    }
}

Monitor-Services
```

16. **Filtrar archivos por extensiones múltiples**
```powershell
$extensiones = @('.log', '.txt', '.xml')
Get-ChildItem C:\ -Recurse | 
    Where-Object { $_.Extension -in $extensiones }
```

17. **Script de limpieza de archivos temporales**
```powershell
function Remove-TempFiles {
    param(
        [int]$DiasSinUso = 30,
        [string]$Path = "$env:TEMP"
    )
    Get-ChildItem $Path | 
        Where-Object { 
            $_.LastAccessTime -lt (Get-Date).AddDays(-$DiasSinUso) 
        } | 
        Remove-Item -Force -Recurse
}
```

18. **Comparar versiones de módulos**
```powershell
Get-Module -ListAvailable | 
    Where-Object { $_.Version -gt [Version]"1.0.0.0" } | 
    Sort-Object Version -Descending
```

19. **Filtrar eventos del sistema**
```powershell
Get-EventLog -LogName System | 
    Where-Object { 
        $_.EntryType -eq 'Error' -and 
        $_.TimeGenerated -gt (Get-Date).AddHours(-24) 
    }
```

20. **Función avanzada de búsqueda de archivos**
```powershell
function Find-FilesByPattern {
    param(
        [string]$Path = 'C:\',
        [string]$Pattern = '*',
        [long]$MinSizeMB = 0,
        [long]$MaxSizeMB = [long]::MaxValue
    )
    Get-ChildItem -Path $Path -Recurse -Include $Pattern | 
        Where-Object { 
            $_.Length/1MB -ge $MinSizeMB -and 
            $_.Length/1MB -le $MaxSizeMB 
        }
}

# Ejemplo de uso
Find-FilesByPattern -Path C:\ -Pattern '*.log' -MinSizeMB 10 -MaxSizeMB 100
```

### 📝 Consejos Importantes:

1. Siempre usa `Where-Object` para filtrado avanzado
2. Aprovecha las tuberías (`|`) para encadenar comandos
3. Usa variables y funciones para hacer scripts más reutilizables
4. Presta atención a los tipos de módulos y sus capacidades
5. Sé cuidadoso al crear y manejar archivos ocultos

### 🚀 Recomendaciones Finales:

- Experimenta con diferentes condiciones y parámetros
- Consulta la ayuda de PowerShell (`Get-Help`) para más detalles

