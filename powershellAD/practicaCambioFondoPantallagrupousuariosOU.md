## 🧠 **Práctica PowerShell: Crear OU, importar usuarios y aplicar GPO para cambiar el fondo de pantalla**

---

### 🎯 Objetivo:

1. Crear una **Unidad Organizativa (OU)**.
2. Crear **usuarios desde un archivo CSV** dentro de esa OU.
3. Crear una **GPO** que cambie el fondo de pantalla del escritorio de esos usuarios.
4. Aplicar la GPO a la OU.

---

## 📁 Estructura del archivo CSV

**Ejemplo: `usuarios.csv`**

```csv
Nombre,Apellido,NombreUsuario,Contraseña
Laura,García,lgarcia,P@ssw0rd123
Carlos,López,clopez,P@ssw0rd123
```

---

## 🔧 Script PowerShell completo

```powershell
# Parámetros
$ouName = "PersonalContabilidad"
$dominio = "midominio.local"
$ouPath = "OU=$ouName,DC=midominio,DC=local"
$csvPath = "C:\scripts\usuarios.csv"           # Ruta del CSV
$gpoName = "FondoPantallaContabilidad"
$wallpaperPath = "\\SRV-ARCHIVOS\fondos\contabilidad.jpg"  # Debe ser accesible para los usuarios

# Requiere módulos: ActiveDirectory, GroupPolicy

# 1. Crear OU si no existe
if (-not (Get-ADOrganizationalUnit -LDAPFilter "(ou=$ouName)" -ErrorAction SilentlyContinue)) {
    New-ADOrganizationalUnit -Name $ouName -Path "DC=midominio,DC=local"
    Write-Host "[OK] OU '$ouName' creada."
} else {
    Write-Host "[!] OU '$ouName' ya existe."
}

# 2. Crear usuarios desde CSV
Import-Csv -Path $csvPath | ForEach-Object {
    $nombre = $_.Nombre
    $apellido = $_.Apellido
    $usuario = $_.NombreUsuario
    $clave = ConvertTo-SecureString $_.Contraseña -AsPlainText -Force
    $nombreCompleto = "$nombre $apellido"

    New-ADUser -Name $nombreCompleto `
               -SamAccountName $usuario `
               -UserPrincipalName "$usuario@$dominio" `
               -GivenName $nombre `
               -Surname $apellido `
               -AccountPassword $clave `
               -Path $ouPath `
               -Enabled $true

    Write-Host "[OK] Usuario '$usuario' creado."
}

# 3. Crear la GPO de fondo de pantalla
if (-not (Get-GPO -Name $gpoName -ErrorAction SilentlyContinue)) {
    New-GPO -Name $gpoName -Comment "Establece fondo de pantalla corporativo"
    Write-Host "[OK] GPO '$gpoName' creada."
}

# 4. Configurar GPO (fondo de pantalla)
Set-GPRegistryValue -Name $gpoName `
    -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" `
    -ValueName "Wallpaper" `
    -Type String `
    -Value $wallpaperPath

Set-GPRegistryValue -Name $gpoName `
    -Key "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System" `
    -ValueName "WallpaperStyle" `
    -Type String `
    -Value "2"   # 2 = Estirar

# 5. Enlazar GPO a la OU
New-GPLink -Name $gpoName -Target $ouPath -Enforced $false
Write-Host "[OK] GPO vinculada a la OU '$ouName'."
```

---

## ✅ Resultado:

- Se crea una OU llamada **PersonalContabilidad**.
- Se importan usuarios desde `usuarios.csv`.
- Se crea una GPO que **establece un fondo de pantalla corporativo**.
- La GPO se **aplica automáticamente** a todos los usuarios de esa OU.
