
```powershell
# Clase de Demostración: Where-Object y Pipelines en PowerShell

# 1. Conceptos Básicos de Filtrado
Write-Host "1. Filtrado Básico con Where-Object" -ForegroundColor Green
Get-Process | Where-Object { $_.CPU -gt 10 }

# 2. Múltiples Condiciones
Write-Host "`n2. Múltiples Condiciones de Filtrado" -ForegroundColor Green
Get-Process | Where-Object { 
    $_.CPU -gt 10 -and $_.Name -like "*chrome*" 
}

# 3. Comparaciones con Propiedades
Write-Host "`n3. Comparaciones Complejas" -ForegroundColor Green
Get-ChildItem C:\ | Where-Object { 
    $_.Length -gt 1MB -and $_.Extension -eq ".log" 
}

# 4. Filtrado con Operadores Especiales
Write-Host "`n4. Operadores de Comparación" -ForegroundColor Green
$procesos = Get-Process | Where-Object {
    $_.Name -match "^[A-Z]" # Procesos que empiezan con mayúscula
}
$procesos | Select-Object Name, Id

# 5. Filtrado con Propiedades Booleanas
Write-Host "`n5. Filtrado con Propiedades Booleanas" -ForegroundColor Green
Get-Service | Where-Object { 
    $_.Status -eq 'Running' -and $_.StartType -eq 'Automatic' 
}

# 6. Uso Avanzado con Scriptblocks
Write-Host "`n6. ScriptBlocks Avanzados" -ForegroundColor Green
$umbralMemoria = 100
Get-Process | Where-Object { 
    $_.WorkingSet64 / 1MB -gt $umbralMemoria 
} | Sort-Object WorkingSet64 -Descending | Select-Object -First 5

# 7. Filtrado con Operadores de Comparación
Write-Host "`n7. Operadores de Comparación" -ForegroundColor Green
$usuarios = Get-LocalUser | Where-Object {
    $_.Enabled -eq $true -and $_.PasswordExpired -eq $false
}
$usuarios | Format-Table Name, Enabled, PasswordExpired

# 8. Pipeline Complejo
Write-Host "`n8. Pipeline Complejo" -ForegroundColor Green
Get-ChildItem C:\Windows\System32 | 
    Where-Object { $_.Extension -eq '.dll' } | 
    Sort-Object Length -Descending | 
    Select-Object Name, Length -First 10 | 
    Format-Table

# 9. Filtrado con Operador -in
Write-Host "`n9. Uso de Operador -in" -ForegroundColor Green
$procesosInteres = @('chrome', 'firefox', 'code')
Get-Process | Where-Object { $_.Name -in $procesosInteres }

# 10. Función Personalizada de Filtrado
Write-Host "`n10. Función de Filtrado Personalizada" -ForegroundColor Green
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

# Ejemplo de uso de la función
Find-LargeFiles -SizeThresholdMB 50 | Format-Table

# Bonus: Rendimiento y Optimización
Write-Host "`nBonus: Comparación de Rendimiento" -ForegroundColor Green
Measure-Command { Get-Process | Where-Object { $_.CPU -gt 10 } }
Measure-Command { Get-Process | Where-Object CPU -gt 10 }
```

Explicación de Conceptos Clave:

1. **Pipeline (`|`)**: 
   - Permite encadenar comandos
   - Pasa la salida de un comando como entrada al siguiente

2. **Where-Object**:
   - Filtra objetos basándose en condiciones
   - Dos formas principales de uso:
     a. `{ script block }`
     b. Comparación directa con parámetro

3. **Operadores de Comparación**:
   - `-eq`: Igual
   - `-ne`: No igual
   - `-gt`: Mayor que
   - `-lt`: Menor que
   - `-match`: Coincidencia de patrón
   - `-in`: Pertenece a una colección

4. **Propiedades Especiales**:
   - `$_`: Representa el objeto actual en la tubería
   - Permite acceder a propiedades del objeto

🚀 Consejos de Rendimiento:
- Usar filtrado nativo cuando sea posible
- Preferir `Where-Object` con comparación directa
- Limitar el alcance de búsqueda
