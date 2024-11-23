### **Políticas de Seguridad en PowerShell**

#### **Objetivos de la clase**
1. Conocer las diferentes políticas de ejecución de scripts en PowerShell.
2. Aprender a cambiar la política de seguridad según las necesidades.
3. Realizar ejercicios prácticos para entender su funcionamiento.

---

### **1. Introducción a las políticas de ejecución de PowerShell**
Las políticas de ejecución en PowerShell controlan cómo y si los scripts pueden ejecutarse en el sistema. Estas políticas se diseñaron para ayudar a prevenir la ejecución de scripts maliciosos.

#### **Tipos de políticas de ejecución**
1. **Restricted (Predeterminada)**  
   - No permite la ejecución de scripts.
   - Solo se pueden ejecutar comandos interactivos.

2. **AllSigned**  
   - Solo permite ejecutar scripts firmados por un editor de confianza.
   - Requiere confirmación para ejecutar scripts firmados por editores no confiables.

3. **RemoteSigned**  
   - Permite ejecutar scripts creados localmente sin firma.
   - Los scripts descargados de Internet deben estar firmados por un editor de confianza.

4. **Unrestricted**  
   - Permite ejecutar cualquier script sin restricciones.
   - Muestra advertencias antes de ejecutar scripts descargados de Internet.

5. **Bypass**  
   - No aplica restricciones de seguridad ni genera advertencias.
   - Usado típicamente para tareas automatizadas en entornos controlados.

6. **Undefined**  
   - Indica que no se ha configurado una política de ejecución para el ámbito actual.

---

### **2. Cómo cambiar la política de ejecución**
Se utiliza el cmdlet `Set-ExecutionPolicy` para modificar la política de ejecución.

#### **Cmdlets principales**
- **Ver la política actual**:  
  ```powershell
  Get-ExecutionPolicy
  ```

- **Cambiar la política de ejecución**:  
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy [Política] -Scope [Ámbito]
  ```
  Ejemplo:  
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

#### **Ámbitos de aplicación**
- **LocalMachine**: Afecta a todos los usuarios del equipo (requiere privilegios de administrador).
- **CurrentUser**: Solo afecta al usuario actual.
- **Process**: Solo aplica a la sesión de PowerShell actual.

#### **Ejemplo interactivo**
1. Consulta la política actual:  
   ```powershell
   Get-ExecutionPolicy -List
   ```
2. Cambia la política a `Unrestricted` para el usuario actual:  
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
   ```
3. Verifica que el cambio se haya aplicado correctamente:  
   ```powershell
   Get-ExecutionPolicy -List
   ```

---

### **3. Ejercicios prácticos**

#### **Ejercicio 1: Consultar y cambiar la política**
**Problema**:  
El sistema tiene configurada la política `Restricted`. Cambia la política para que permita ejecutar scripts creados localmente y verifica el cambio.

**Solución**:  
1. Consulta la política actual:
   ```powershell
   Get-ExecutionPolicy
   ```
2. Cambia la política a `RemoteSigned`:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
3. Verifica que la política se cambió:
   ```powershell
   Get-ExecutionPolicy
   ```

---

#### **Ejercicio 2: Ejecutar un script descargado con política RemoteSigned**
**Problema**:  
Descargaste un script llamado `test-script.ps1`. Con la política `RemoteSigned`, intenta ejecutarlo y observa el resultado.

**Solución**:
1. Configura la política en `RemoteSigned`:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
   ```
2. Intenta ejecutar el script descargado:
   ```powershell
   .\test-script.ps1
   ```
3. Si PowerShell bloquea el script, desbloquéalo con:
   ```powershell
   Unblock-File -Path .\test-script.ps1
   ```
4. Vuelve a ejecutar el script:
   ```powershell
   .\test-script.ps1
   ```

---

#### **Ejercicio 3: Cambiar la política solo para la sesión actual**
**Problema**:  
Quieres permitir cualquier tipo de script durante la sesión actual sin cambiar la configuración para otros usuarios o sesiones.

**Solución**:  
1. Cambia la política para la sesión actual:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
   ```
2. Verifica la política para la sesión actual:
   ```powershell
   Get-ExecutionPolicy -Scope Process
   ```
3. Intenta ejecutar un script sin restricciones.

---

### **4. Buenas prácticas**
- Cambia la política de ejecución solo cuando sea necesario.
- Usa `AllSigned` o `RemoteSigned` en entornos de producción.
- Configura `Bypass` o `Unrestricted` solo en entornos controlados.
- Siempre verifica la fuente de los scripts antes de ejecutarlos.

---

### **5. Ejercicio final**
**Problema**:  
Configura una política que permita ejecutar scripts locales sin firma, pero que bloquee scripts descargados de Internet. Intenta ejecutar un script local y uno descargado, desbloquea el descargado y ejecútalo nuevamente.

**Solución**:  
1. Configura la política:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
2. Crea un script local llamado `local-script.ps1` y ejecútalo:
   ```powershell
   Write-Host "Script local ejecutado exitosamente."
   ```
   ```powershell
   .\local-script.ps1
   ```
3. Descarga un script de prueba de Internet y ejecútalo. Observa el bloqueo.
4. Desbloquea el script descargado:
   ```powershell
   Unblock-File -Path .\downloaded-script.ps1
   ```
5. Vuelve a ejecutarlo y verifica el resultado.

---

### **Cierre de la sesión**
1. ¿Qué política se recomienda para desarrollo vs producción?
2. ¿Qué diferencia hay entre `Bypass` y `Unrestricted`?
3. Revisión de conceptos clave con preguntas rápidas.