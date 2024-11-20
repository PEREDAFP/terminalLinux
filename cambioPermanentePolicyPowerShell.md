Cambiar de manera permanente la política de ejecución en PowerShell implica modificar la configuración para que persista después de cerrar y volver a abrir PowerShell. Esto se puede lograr estableciendo la política en el ámbito **`LocalMachine`** o **`CurrentUser`**, dependiendo de tus necesidades.

---

### **Pasos para cambiar la política de ejecución de manera permanente**

1. **Abrir PowerShell como administrador (para ámbito `LocalMachine`)**:
   - Presiona `Win + S`, escribe "PowerShell".
   - Haz clic derecho en "PowerShell" y selecciona **Ejecutar como administrador**.

2. **Verifica la política actual en todos los ámbitos**:
   Usa el siguiente comando para listar las políticas de ejecución configuradas:
   ```powershell
   Get-ExecutionPolicy -List
   ```
   - **`LocalMachine`**: Afecta a todos los usuarios del sistema.
   - **`CurrentUser`**: Afecta solo al usuario actual.

3. **Cambiar la política para el ámbito deseado**:
   Usa el cmdlet `Set-ExecutionPolicy` para establecer una nueva política.

   #### Cambiar para todos los usuarios (requiere permisos de administrador):
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
   ```
   - Esto configura la política para todos los usuarios del equipo.
   - Sustituye `RemoteSigned` por la política deseada (`Restricted`, `AllSigned`, `Unrestricted`, etc.).

   #### Cambiar solo para el usuario actual:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
   - Esto afecta únicamente al usuario que ejecuta el comando.

4. **Confirma el cambio**:
   - Si se te solicita confirmación, escribe `Y` (Yes) y presiona Enter.

5. **Verifica que la política se aplicó correctamente**:
   Usa nuevamente el siguiente comando:
   ```powershell
   Get-ExecutionPolicy -List
   ```

---

### **Notas importantes**
- Cambiar la política de manera permanente podría generar riesgos de seguridad si eliges una configuración como `Unrestricted` o `Bypass`. Usa estas políticas solo en entornos controlados.
- Para revertir a la configuración predeterminada:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy Restricted -Scope LocalMachine
  ```

---

### **Ejemplo Completo**
#### Escenario: Configurar `RemoteSigned` como política permanente para todos los usuarios.

1. Abre PowerShell como administrador.
2. Cambia la política:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
   ```
3. Verifica que se aplicó:
   ```powershell
   Get-ExecutionPolicy -List
   ```
   Salida esperada:
   ```
   Scope          ExecutionPolicy
   -----          ---------------
   MachinePolicy  Undefined
   UserPolicy     Undefined
   Process        Undefined
   CurrentUser    Undefined
   LocalMachine   RemoteSigned
   ```

---

### **Alternativa: Usar el Registro de Windows**
Puedes cambiar la política directamente en el registro de Windows, aunque esto no es recomendado para usuarios principiantes.

1. Abre el Editor del Registro (`regedit`).
2. Navega a:
   - **Para todos los usuarios**: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell`
   - **Para el usuario actual**: `HKEY_CURRENT_USER\SOFTWARE\Microsoft\PowerShell\1\ShellIds\Microsoft.PowerShell`
3. Busca la clave **`ExecutionPolicy`** y modifica su valor por la política deseada (`Restricted`, `AllSigned`, `RemoteSigned`, etc.).
4. Cierra y abre PowerShell para que el cambio surta efecto.