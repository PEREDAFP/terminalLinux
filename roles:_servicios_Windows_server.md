## 🎙️ _"Roles y Servicios de Rol en Windows Server: ¿Qué, cómo y para qué?"_

### 🎯 Objetivo de la charla:

Entender qué son los **roles y servicios de rol** en Windows Server, cómo se instalan, y para qué sirve cada uno en la práctica. ¡Con ejemplos y consejos para elegir el correcto!

---

### 🔹 1. ¿Qué es un **rol** en Windows Server?

Un **rol** es una función principal que un servidor puede desempeñar. Piénsalo como “el trabajo principal” que va a hacer ese servidor.

📌 _Ejemplos de roles comunes_:

- **Active Directory Domain Services** (AD DS)
- **DNS Server**
- **DHCP Server**
- **Web Server (IIS)**
- **File and Storage Services**

---

### 🔹 2. ¿Qué es un **servicio de rol**?

Los **servicios de rol** son funcionalidades específicas dentro de un rol. Permiten afinar aún más lo que hará el servidor.

📌 _Ejemplo_:  
En el rol **Web Server (IIS)** puedes activar servicios como:

- Servidor FTP
- Redirección HTTP
- ASP.NET

---

### 🔹 3. Diferencia entre funciones del servidor, características, roles y servicios

| Concepto            | ¿Qué hace?                                              |
| ------------------- | ------------------------------------------------------- |
| **Rol**             | Función principal del servidor                          |
| **Servicio de rol** | Subfunciones dentro de un rol                           |
| **Características** | Funcionalidades adicionales (no están ligadas a un rol) |

📌 Ejemplo de característica: **.NET Framework**, **Failover Clustering**

---

### 🔹 4. Cómo instalar un rol (con y sin GUI)

#### ✔️ Desde GUI (Server Manager)

- Dashboard → "Agregar roles y características"
- Seleccionas el servidor, el rol, los servicios, y listo.

#### 💻 Desde PowerShell (ideal para Core)

```powershell
Install-WindowsFeature -Name AD-Domain-Services
```

---

### 🔹 5. Principales roles y para qué sirven (con ejemplos reales)

| Rol                         | Descripción                  | Caso de uso                        |
| --------------------------- | ---------------------------- | ---------------------------------- |
| **AD DS**                   | Controlador de dominio       | Gestión de usuarios y GPOs         |
| **DNS Server**              | Resolución de nombres        | Obligatorio en entorno AD          |
| **DHCP Server**             | Asignación automática de IPs | Redes medianas o grandes           |
| **Web Server (IIS)**        | Alojamiento web              | Aplicaciones internas o sitios web |
| **File Services**           | Compartir archivos en red    | Carpetas para departamentos        |
| **Remote Desktop Services** | Acceso remoto a escritorios  | Escritorio virtual centralizado    |

---

### 🔹 6. Buenas prácticas

- Instala solo los roles necesarios (seguridad + rendimiento).
- Usa **Server Core** siempre que sea posible.
- Automatiza con **PowerShell** o **DSC**.
- Documenta cada servidor y su función.

---

### 🔹 7. Metáfora: “El servidor es un empleado”

- Un **rol** es su puesto de trabajo (contador, técnico, recepcionista).
- Un **servicio de rol** es cada una de sus tareas (facturación, responder emails, atención al cliente).
- Una **característica** es una habilidad extra (idiomas, Excel, conducción).

---

### 🔹 8. Conclusión

Entender y elegir correctamente los **roles** y **servicios de rol** es clave para que tu infraestructura funcione bien, sea segura y fácil de mantener.

---

### 🔚 ¿Preguntas?
