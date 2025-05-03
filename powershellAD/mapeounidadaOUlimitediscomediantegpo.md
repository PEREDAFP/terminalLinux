## 🧠 **Práctica PowerShell: Mapear recurso compartido a una OU y aplicar cuota de 500 MB por usuario**

---

### 🎯 Objetivo

1. Crear un **script de inicio de sesión** para mapear `\\servidor\empresa` como unidad Z: a los usuarios de una OU.
2. Crear una **GPO** y vincularla a la OU para limitar el uso del recurso compartido a **500 MB por usuario** con cuotas de disco.

---

## 🔧 PARTE 1: Crear script de mapeo y asignarlo a los usuarios de una OU

```powershell
# Parámetros personalizables
$OU = "OU=Contabilidad,DC=midominio,DC=local"
$unidad = "Z:"
$servidor = "SRV-ARCHIVOS"
$recurso = "empresa"
$RutaRed = "\\$servidor\$recurso"
$NetlogonPath = "\\$servidor\NETLOGON"

# Obtener usuarios de la OU
$usuarios = Get-ADUser -Filter * -SearchBase $OU

foreach ($usuario in $usuarios) {
    $scriptNombre = "$($usuario.SamAccountName).bat"
    $scriptContenido = "@echo off`r`nnet use $unidad $RutaRed /persistent:no"
    $scriptRuta = Join-Path $NetlogonPath $scriptNombre

    # Crear script en NETLOGON
    $scriptContenido | Out-File -FilePath $scriptRuta -Encoding ASCII -Force

    # Asignar el script al usuario
    Set-ADUser -Identity $usuario -ScriptPath $scriptNombre
}

Write-Host "[OK] Scripts de inicio de sesión creados y asignados para los usuarios de la OU."
```

---

## 🔧 PARTE 2: Crear GPO y establecer política de cuota de disco

> Requiere RSAT (`GroupPolicy` y `Storage` módulos) y permisos de administración.

```powershell
# Parámetros
$NombreGPO = "Limite500MB_Empresa"
$OUName = "Contabilidad"
$Dominio = "midominio.local"
$OUPath = "OU=$OUName,DC=midominio,DC=local"
$Drive = "C:"

# Crear la GPO
New-GPO -Name $NombreGPO -Comment "Limita espacio a 500MB por usuario en C:\empresa" | Out-Null

# Vincular a la OU
New-GPLink -Name $NombreGPO -Target $OUPath | Out-Null

# Habilitar administración de cuotas de disco
Set-GPRegistryValue -Name $NombreGPO -Key "HKLM\Software\Policies\Microsoft\Windows NT\DiskQuota" -ValueName "Enable" -Type DWord -Value 1

# Aplicar cuota predeterminada de 500MB (en KB)
Set-GPRegistryValue -Name $NombreGPO -Key "HKLM\Software\Policies\Microsoft\Windows NT\DiskQuota" -ValueName "LimitDiskSpace" -Type DWord -Value 1
Set-GPRegistryValue -Name $NombreGPO -Key "HKLM\Software\Policies\Microsoft\Windows NT\DiskQuota" -ValueName "DefaultLimit" -Type String -Value "524288"  # 500MB
Set-GPRegistryValue -Name $NombreGPO -Key "HKLM\Software\Policies\Microsoft\Windows NT\DiskQuota" -ValueName "DenyDiskSpace" -Type DWord -Value 1

Write-Host "[OK] GPO creada y configurada para establecer cuota de 500MB."

# Activar cuotas en la unidad (localmente)
fsutil quota track $Drive
fsutil quota enforce $Drive

# Establecer cuota por defecto manualmente (opcional refuerzo)
fsutil quota modify $Drive 524288 524288 everyone

Write-Host "[OK] Cuotas activadas en $Drive. Cada usuario está limitado a 500MB."
```

---

## ✅ Resultado

- Todos los usuarios de la OU "Contabilidad" ejecutan un script que mapea `\\SRV-ARCHIVOS\empresa` como `Z:`.
- Se aplica una GPO que **impide que cada usuario use más de 500 MB** del volumen `C:\empresa`.
