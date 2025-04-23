### **Unión de un Equipo Cliente al Dominio en Active Directory**

#### **Objetivo**

Aprender el proceso para **unir un equipo cliente (ej: Windows 10 Pro)** a un dominio de **Active Directory**, permitiendo la autenticación centralizada y la gestión de políticas.

---

### **Requisitos Previos**

1. **Licencia del equipo cliente**:

   - Solo ediciones **Professional, Enterprise o Education** de Windows pueden unirse al dominio.
   - No funciona con versiones _Home_.

2. **Configuración de red**:

   - El equipo debe estar en la **misma red** que el controlador de dominio.
   - **DNS correcto**: La IP del servidor DNS (controlador de dominio) debe estar configurada en el cliente.
     - Ejemplo: Si el controlador tiene IP `192.168.0.5`, el cliente debe usarla como DNS primario.

3. **Credenciales adecuadas**:
   - Solo cuentas con permisos de **"Administradores de Dominio"** pueden unir equipos al dominio (ej: el usuario `Administrador` por defecto).

---

### **Pasos para Unir el Equipo al Dominio**

1. **Cambiar el nombre del equipo** (opcional, pero recomendado):

   - Usar una nomenclatura clara (ej: `PC-ASIR01`).

2. **Configurar la red del cliente**:

   - Establecer IP estática o DHCP (según la infraestructura).
   - **Asegurarse de que el DNS apunte al controlador de dominio**:
     ```
     DNS preferido: 192.168.0.5
     ```
   - Verificar conectividad con `ping 192.168.0.5`.

3. **Unir el equipo al dominio**:

   - Método 1 (Windows 10):
     - `Configuración > Sistema > Acerca de > Conectar a un dominio`.
   - Método 2 (Clásico):
     - `Panel de Control > Sistema > Cambiar configuración > Unir a un dominio`.
   - Ingresar el nombre del dominio (ej: `iesvillaverde.local`).
   - Proporcionar credenciales de un **administrador de dominio**.

4. **Reiniciar el equipo** para aplicar los cambios.

---

### **Verificación Post-Unión**

- **En el cliente**:
  - Al iniciar sesión, seleccionar **"Iniciar sesión en el dominio"** (ej: `IESVILLAVERDE\usuario`).
  - El usuario debe cambiar su contraseña en el primer inicio (si está configurado en AD).
- **En el servidor (Active Directory)**:
  - Verificar que el equipo aparezca en la OU `Computers` o en la unidad organizativa asignada.
  - Confirmar el **último inicio de sesión** del usuario en las propiedades de la cuenta.

---

### **Beneficios de Unir Equipos al Dominio**

1. **Autenticación centralizada**: Los usuarios inician sesión con credenciales de AD.
2. **Aplicación de GPOs**: Se pueden implementar políticas de grupo para controlar configuraciones.
3. **Gestión de recursos compartidos**: Acceso a carpetas, impresoras y otros recursos con permisos de AD.
4. **Seguridad**: Evita el uso de cuentas locales y centraliza la administración.

---

### **Errores Comunes y Soluciones**

- **"No se puede contactar con el controlador de dominio"**:
  - Verificar que el DNS del cliente apunte al servidor AD.
  - Confirmar que el equipo esté en la misma red.
- **Permisos insuficientes**:
  - Usar una cuenta con derechos de **"Administradores de Dominio"**.

---
