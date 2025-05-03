## **Permisos NTFS y su Diferencia entre Active Directory y Equipos Locales**

**Objetivo General**: Comprender los permisos NTFS en Windows y su aplicación tanto en entornos locales como en entornos con Active Directory.

#### **¿Qué es NTFS?**

- Sistema de archivos utilizado por Windows que permite gestionar permisos y seguridad a nivel de archivos y carpetas.

#### **Permisos NTFS Principales**

| Permiso       | Función                                                |
| ------------- | ------------------------------------------------------ |
| Leer          | Ver el contenido                                       |
| Escribir      | Modificar archivos o agregar nuevos                    |
| Ejecutar      | Ejecutar archivos o scripts                            |
| Modificar     | Cambiar y eliminar archivos                            |
| Control total | Todos los anteriores + cambiar permisos y propietarios |

**Nota**: Estos permisos pueden aplicarse a usuarios y grupos.

---

### NTFS en Equipo Local vs. Active Directory (15 min)\*\*

#### **Equipo Normal (sin AD):**

- Los permisos se aplican a usuarios locales del equipo.
- Limitaciones: administración individual, difícil de escalar en redes grandes.

#### **Con Active Directory:**

- Permisos se aplican a usuarios y grupos del dominio.
- Se puede aplicar control centralizado (políticas de grupo, scripts de login, etc.)
- Ejemplo: Grupo “Marketing” tiene acceso de solo lectura a la carpeta “Campañas” desde cualquier equipo del dominio.

**Comparación**:

| Característica    | Equipo Local  | Active Directory      |
| ----------------- | ------------- | --------------------- |
| Usuarios          | Locales       | De dominio            |
| Administración    | Manual por PC | Centralizada          |
| Escalabilidad     | Baja          | Alta                  |
| Control de acceso | Limitado      | Detallado y delegable |
