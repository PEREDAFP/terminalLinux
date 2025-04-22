### 🎯 Objetivo de la práctica:

1. Crear una **Unidad Organizativa (OU)**.
2. Crear un **usuario** dentro de esa OU.
3. Crear una **GPO** que impida el acceso a la consola de comandos (`cmd.exe`).
4. **Asignar** la GPO a la OU.

---

## 🧪 PRÁCTICA COMPLETA – Solo PowerShell (modo Core)

> 📝 Asegúrate de tener instalados los módulos necesarios: `GroupPolicy`, `ActiveDirectory`.

---

### 1️⃣ Crear la Unidad Organizativa (OU)

```powershell
# Crear una OU para pruebas
New-ADOrganizationalUnit -Name "UsuariosRestringidos" -Path "DC=midominio,DC=local"
```

🔁 Sustituye `"midominio.local"` por el nombre real de tu dominio. Ten en cuenta que pude tener más DC.

---

### 2️⃣ Crear un usuario dentro de la OU

```powershell
# Crear un nuevo usuario de prueba
New-ADUser -Name "UsuarioCmdBloqueado" `
    -SamAccountName "ucmdbloq" `
    -AccountPassword (ConvertTo-SecureString "P@ssw0rd123" -AsPlainText -Force) `
    -Enabled $true `
    -Path "OU=UsuariosRestringidos,DC=midominio,DC=local"
```

> ⚠️ Requiere que la contraseña cumpla la política del dominio.

---

### 3️⃣ Crear una GPO que bloquee CMD

```powershell
# Crear la GPO
New-GPO -Name "Bloquear CMD"

# Editar la GPO: impedir ejecutar cmd.exe
Set-GPRegistryValue -Name "Bloquear CMD" `
    -Key "HKCU\Software\Policies\Microsoft\Windows\System" `
    -ValueName "DisableCMD" `
    -Type DWord `
    -Value 1
```

📌 `DisableCMD = 1` → Bloquea `cmd.exe` pero permite ejecutar scripts.

Usa `2` si también quieres bloquear la ejecución de scripts `.bat` o `.cmd`.

---

### 4️⃣ Vincular la GPO a la OU

```powershell
# Aplicar la GPO a la OU "UsuariosRestringidos"
New-GPLink -Name "Bloquear CMD" -Target "OU=UsuariosRestringidos,DC=midominio,DC=local"
```

---

### 5️⃣ (Opcional) Forzar la actualización de políticas en el cliente

En el equipo cliente (si lo estás probando):

```powershell
gpupdate /force
```

---

## 🧾 Resumen del flujo completo (puedes copiar y pegar):

```powershell
# 1. Crear OU
New-ADOrganizationalUnit -Name "UsuariosRestringidos" -Path "DC=midominio,DC=local"

# 2. Crear usuario
New-ADUser -Name "UsuarioCmdBloqueado" `
    -SamAccountName "ucmdbloq" `
    -AccountPassword (ConvertTo-SecureString "P@ssw0rd123" -AsPlainText -Force) `
    -Enabled $true `
    -Path "OU=UsuariosRestringidos,DC=midominio,DC=local"

# 3. Crear GPO
New-GPO -Name "Bloquear CMD"

# 4. Configurar GPO
Set-GPRegistryValue -Name "Bloquear CMD" `
    -Key "HKCU\Software\Policies\Microsoft\Windows\System" `
    -ValueName "DisableCMD" `
    -Type DWord `
    -Value 1

# 5. Vincular GPO
New-GPLink -Name "Bloquear CMD" -Target "OU=UsuariosRestringidos,DC=midominio,DC=local"
```

---
