### 🔧 **Práctica: Compartir carpeta `C:\empresa` con el grupo `empresa` usando PowerShell**

#### 🎯 Objetivo:

- Crear una carpeta compartida.
- Dar permisos de acceso solo a los usuarios del grupo de Active Directory llamado `empresa`.

---

### 🪟 **Requisitos Previos:**

- Un grupo de AD llamado `empresa` ya creado.
- PowerShell con privilegios de administrador.
- Servidor miembro del dominio.

---

### ✅ **Pasos:**

#### 1. **Crear la carpeta local**

```powershell
New-Item -Path "C:\" -Name "empresa" -ItemType "Directory" -Force
```

#### 2. **Crear el recurso compartido**

```powershell
New-SmbShare -Name "empresa" -Path "C:\empresa" -FullAccess "DOMINIO\empresa"
```

> Reemplaza `DOMINIO` con el nombre real de tu dominio.

#### 3. **Establecer permisos NTFS**

```powershell
$acl = Get-Acl "C:\empresa"
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("DOMINIO\empresa", "Modify", "ContainerInherit,ObjectInherit", "None", "Allow")
$acl.AddAccessRule($rule)
Set-Acl "C:\empresa" $acl
```

---

### 📌 Verificación:

1. **Verifica el recurso compartido**

```powershell
Get-SmbShare -Name empresa
```

2. **Verifica permisos NTFS**

```powershell
Get-Acl "C:\empresa" | Format-List
```

---

### 📚 Notas adicionales:

- Puedes usar `Read` en lugar de `Modify` si no deseas que escriban archivos.
- Si deseas que todos los usuarios del grupo puedan mapear el recurso, asegúrate de que tengan permisos de red adecuados y no haya bloqueos por firewall.
