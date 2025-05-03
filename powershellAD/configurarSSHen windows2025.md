# Configuración del Firewall en Windows Server 2025 Core para Permitir solo Acceso SSH

## 🎯 Objetivo

Configurar el firewall de Windows Server 2025 Core para **permitir exclusivamente el acceso por SSH (puerto 22 TCP)**, y bloquear todo el tráfico entrante restante.

---

## 📋 Requisitos Previos

- Windows Server 2025 Core instalado.
- Acceso de administrador (local o remoto).
- PowerShell disponible.
- Servicio OpenSSH Server instalado y habilitado.

---

## 🛠️ Pasos de Configuración (PowerShell)

```powershell
# 1. Habilitar el servicio de OpenSSH si no está instalado
Add-WindowsCapability -Online -Name OpenSSH.Server~~~~0.0.1.0

# 2. Iniciar y configurar el servicio SSH para que arranque automáticamente
Start-Service sshd
Set-Service -Name sshd -StartupType 'Automatic'

# 3. (Opcional) Eliminar reglas entrantes previas para partir desde cero
Get-NetFirewallRule -Direction Inbound | Remove-NetFirewallRule

# 4. Crear regla para permitir solo el puerto SSH (22 TCP)
New-NetFirewallRule -DisplayName "Permitir SSH" -Direction Inbound -Protocol TCP `
    -LocalPort 22 -Action Allow

# 5. Configurar el firewall para bloquear todo tráfico entrante que no esté explícitamente permitido
Set-NetFirewallProfile -Profile Domain,Private,Public -DefaultInboundAction Block

# 6. (Opcional) Verificar las reglas activas
Get-NetFirewallRule | Where-Object { $_.Direction -eq 'Inbound' }
```
