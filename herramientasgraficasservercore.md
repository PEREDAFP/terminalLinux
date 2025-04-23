### **Herramientas Gráficas en Windows Server Core**

1. **Bloc de notas (Notepad)**

   - Accesible mediante `notepad`.
   - Permite crear, editar y guardar archivos (ej. `.txt`).
   - Útil para ver carpetas y archivos ocultos en el sistema.

2. **Editor del Registro de Windows (Regedit)**

   - Se abre con `regedit`.
   - Interfaz gráfica para modificar el registro (evita errores al editar manualmente en PowerShell).
   - **Importante**: Hacer copias de seguridad (_backups_) antes de cambios.

3. **Información del Sistema (MSInfo32)**

   - Comando: `msinfo32`.
   - Muestra detalles del hardware, sistema operativo, memoria, BIOS y software instalado.

4. **Administrador de Tareas (Task Manager)**

   - Acceso con:
     - `Ctrl + Shift + Esc`
     - `Ctrl + Alt + Supr` → Opción "Administrador de tareas".
     - Comando: `taskmgr`.
   - Monitoriza procesos, rendimiento, usuarios y servicios.

5. **Instalador de Paquetes (MSIEXEC)**
   - Comando: `msiexec`.
   - Permite instalar aplicaciones mediante archivos `.msi`.

---

### **Limitaciones en Server Core**

- **No incluye**:
  - Explorador de archivos (`explorer.exe`).
  - Internet Explorer u otros navegadores gráficos.
  - Interfaz gráfica completa (como en Windows Server estándar).
