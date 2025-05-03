### **Sesión de Clase: Configuración de NIC Teaming en Windows Server 2025 Core**

---

#### **Objetivos**

1. Aprender a crear un **grupo de NICs (NIC Teaming)** para redundancia y balanceo de carga.
2. Simular una falla en una NIC y verificar la conmutación automática.

---

### **Parte Teórica**

**¿Qué es NIC Teaming?**

- Técnica que agrupa múltiples NICs en un único interfaz lógico para:
  - **Redundancia**: Si una NIC falla, el tráfico se redirige a otra.
  - **Balanceo de carga**: Distribuir el tráfico para mejorar el rendimiento.

**Modos comunes**:

- **SwitchIndependent**: No requiere configuración en el switch de red.
- **LACP (SwitchDependent)**: Requiere soporte del switch (protocolo LACP).

---

### **Práctica: Crear y Probar un NIC Team**

#### **Paso 1: Verificar NICs disponibles**

```powershell
Get-NetAdapter | Where-Object { $_.Status -eq 'Up' }
```

- **Objetivo**: Confirmar que hay al menos dos NICs activas (ej: "Ethernet1", "Ethernet2").

---

#### **Paso 2: Crear el NIC Team**

```powershell
New-NetLbfoTeam -Name "TeamRedundante" -TeamMembers "Ethernet1", "Ethernet2" -TeamingMode SwitchIndependent -LoadBalancingAlgorithm Dynamic
```

- **Parámetros**:
  - `-TeamingMode SwitchIndependent`: No depende del switch.
  - `-LoadBalancingAlgorithm Dynamic`: Balanceo inteligente basado en tráfico.

---

#### **Paso 3: Verificar el equipo creado**

```powershell
Get-NetLbfoTeam | Format-List Name, TeamMembers, Status
```

- **Salida esperada**:
  ```
  Name          : TeamRedundante
  TeamMembers   : {Ethernet1, Ethernet2}
  Status        : Up
  ```

---

#### **Paso 4: Asignar IP al equipo**

```powershell
New-NetIPAddress -InterfaceAlias "TeamRedundante" -IPAddress 192.168.1.100 -PrefixLength 24 -DefaultGateway 192.168.1.1
Set-DnsClientServerAddress -InterfaceAlias "TeamRedundante" -ServerAddresses 8.8.8.8, 8.8.4.4
```

---

#### **Paso 5: Simular fallo en una NIC**

1. **Desconectar físicamente el cable de "Ethernet1"** (o deshabilitarla en PowerShell):

```powershell
Disable-NetAdapter -Name "Ethernet1" -Confirm:$false
```

2. **Verificar estado del equipo**:

```powershell
Get-NetLbfoTeamMember -TeamName "TeamRedundante" | Select Name, Status
```

- **Salida esperada**:
  ```
  Name      Status
  ----      ------
  Ethernet1 Disconnected
  Ethernet2 Active
  ```

---

#### **Paso 6: Probar conectividad**

```powershell
Test-NetConnection -ComputerName "www.google.com" -Port 80
```

- **Resultado esperado**: `TcpTestSucceeded: True`, indicando que el tráfico se redirige a "Ethernet2".

---

#### **Paso 7: Reactivar la NIC desconectada**

```powershell
Enable-NetAdapter -Name "Ethernet1"
```

- Verificar que el equipo vuelve a tener ambas NICs activas:

```powershell
Get-NetLbfoTeamMember -TeamName "TeamRedundante" | Select Name, Status
```

---

### **Evaluación Práctica**

1. ¿Qué sucede si ambas NICs están conectadas al mismo switch físico?
2. ¿Por qué es importante el parámetro `-LoadBalancingAlgorithm`?
3. Si el equipo pierde conectividad al desactivar una NIC, ¿cuál podría ser la causa?

---

### **Posibles Errores**

- **Error**: "No se pueden agregar los adaptadores al equipo".

  - **Solución**: Asegurarse de que las NICs no tengan configuraciones previas (IP estática, equipos existentes).

- **Error**: "El tráfico no se redirige".
  - **Solución**: Verificar que el modo `SwitchIndependent` esté bien configurado y las NICs estén en la misma subred.

---
