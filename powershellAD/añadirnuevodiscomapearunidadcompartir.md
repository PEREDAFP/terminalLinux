## 🛠️ Práctica: Añadir y compartir un nuevo disco en un servidor de dominio usando PowerShell

### 🎯 Objetivo:

- Inicializar un nuevo disco.
- Crear una partición y formatearla con NTFS.
- Asignar una letra de unidad.
- Compartirla con el grupo de AD `clase` con permisos adecuados.

---

### 🧾 Requisitos:

- Un disco nuevo y sin inicializar ya conectado al servidor.
- Grupo de Active Directory llamado `clase`.
- PowerShell ejecutado como **administrador**.
- El servidor debe ser miembro del dominio.

---

### ✅ Pasos:

#### 1. **Detectar el nuevo disco (sin particionar)**

```powershell
Get-Disk | Where-Object PartitionStyle -Eq 'RAW'
```

> Anota el número del disco que aparece como RAW. Supongamos que es el **Disco 2**.

#### 2. **Inicializar el disco (GPT recomendado)**

```powershell
Initialize-Disk -Number 2 -PartitionStyle GPT
```

#### 3. **Crear una partición ocupando todo el disco y formatear con NTFS**

```powershell
New-Partition -DiskNumber 2 -UseMaximumSize -AssignDriveLetter | Format-Volume -FileSystem NTFS -NewFileSystemLabel "DatosClase" -Confirm:$false
```

> Esto asignará automáticamente una letra de unidad (ej: E:, F:, etc.). Puedes ver cuál con:

```powershell
Get-Partition -DiskNumber 2 | Get-Volume
```

Supongamos que la letra asignada es **E:**.

#### 4. **Crear el recurso compartido para el grupo `clase`**

```powershell
New-SmbShare -Name "clase" -Path "E:\" -FullAccess "DOMINIO\clase"
```

> Sustituye `DOMINIO` por el nombre real de tu dominio.

#### 5. **Asignar permisos NTFS al grupo clase**

```powershell
$acl = Get-Acl "E:\"
$rule = New-Object System.Security.AccessControl.FileSystemAccessRule("DOMINIO\clase", "Modify", "ContainerInherit,ObjectInherit", "None", "Allow")
$acl.SetAccessRule($rule)
Set-Acl "E:\" $acl
```

---

### 🔍 Verificación:

- **Ver recurso compartido:**

```powershell
Get-SmbShare -Name clase
```

- **Ver letra de unidad y formato:**

```powershell
Get-Volume -FileSystemLabel "DatosClase"
```

---

### 📝 Notas:

- Puedes cambiar `Modify` por `Read` si quieres limitar los permisos.
- Asegúrate de que las políticas de grupo/firewall permitan compartir archivos.
