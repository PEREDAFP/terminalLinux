**Políticas de Grupo (GPOs):**

### **Puntos clave:**

1. **Definición y propósito:**

   - Las GPOs permiten **controlar y configurar** equipos y usuarios de forma masiva en un dominio.
   - Son esenciales para **reducir costos, mejorar seguridad y mantener la productividad** de los usuarios.
   - El principio es **"configurar una vez, aplicar a muchos"**, lo que simplifica la administración.

2. **Relación con las Unidades Organizativas (OUs):**

   - Las GPOs se **vinculan a OUs**, por lo que una estructura bien definida de OUs (por departamentos, funciones, etc.) es crucial para aplicar políticas de manera eficiente.

3. **Alcance de las GPOs:**

   - Existen **más de 15,000 configuraciones** disponibles en Windows Server, desde ajustes básicos hasta controles avanzados.

4. **Requisitos para usar GPOs:**

   - La red debe estar basada en **Active Directory Domain Services (AD DS)**.
   - Los equipos y usuarios deben estar **unidos al dominio** y usar credenciales de dominio.
   - El administrador debe tener permisos para editar GPOs (**Grupo Policy Management Console - GPMC**).

5. **Diferencias entre GPOs locales y de dominio:**
   - Las **GPOs locales** se aplican a equipos individuales, mientras que las **GPOs de dominio** se despliegan masivamente.

### **Conclusión:**

Las Políticas de Grupo son una herramienta poderosa para **automatizar y estandarizar configuraciones** en un entorno de dominio.
