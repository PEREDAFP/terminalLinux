
---

### **1. ACL (Access Control List)**

**ACL** (Lista de Control de Acceso) es un mecanismo avanzado de control de acceso en sistemas de archivos, que permite especificar permisos de acceso más detallados que los permisos tradicionales de Linux (propietario, grupo y otros).

#### **¿Cómo funciona?**
En un sistema con permisos tradicionales, un archivo o directorio solo puede tener permisos asignados para el propietario, el grupo y los demás usuarios. Sin embargo, ACLs permiten establecer permisos adicionales para usuarios o grupos específicos, lo que ofrece mayor flexibilidad.

#### **Ejemplo de ACL:**
Supongamos que tienes un archivo llamado `archivo.txt` y quieres otorgar permisos específicos a un usuario, digamos `usuario1`, y a un grupo, digamos `grupo1`.

- Para asignar permisos de lectura a `usuario1`:
  ```bash
  setfacl -m u:usuario1:r archivo.txt
  ```

- Para dar permisos de escritura y ejecución a `grupo1`:
  ```bash
  setfacl -m g:grupo1:rw archivo.txt
  ```

- Para ver las ACLs de un archivo:
  ```bash
  getfacl archivo.txt
  ```

#### **Ventajas de ACLs:**
- Permiten gestionar permisos con mucha más granularidad, otorgando permisos a múltiples usuarios y grupos en un solo archivo o directorio.
- Utilizan una estructura flexible que no se ve limitada por los tres niveles tradicionales de permisos (propietario, grupo, otros).

---

### **2. SUID (Set User ID)**

El **SUID** es un tipo especial de permiso de ejecución en sistemas Unix y Linux, utilizado principalmente para programas que necesitan ejecutarse con los privilegios del propietario del archivo, no del usuario que ejecuta el programa.

#### **¿Cómo funciona el SUID?**
Cuando se establece el bit SUID en un archivo ejecutable, el programa se ejecuta con los privilegios del propietario del archivo en lugar de con los privilegios del usuario que lo ejecuta. Esto es útil para tareas que requieren permisos especiales (por ejemplo, cambiar contraseñas, editar archivos del sistema).

#### **Ejemplo de SUID:**
Imagina que tienes un archivo ejecutable llamado `programa` y quieres que siempre se ejecute con los permisos del propietario del archivo (en lugar de los del usuario que lo ejecuta):
```bash
chmod u+s programa
```

Esto hace que `programa` se ejecute con los privilegios del usuario propietario del archivo (por ejemplo, `root`), incluso si el usuario que ejecuta el programa no tiene privilegios de `root`.

#### **Ejemplo típico del SUID:**
El comando `passwd` (para cambiar contraseñas) tiene el bit SUID activado, ya que necesita acceso a archivos protegidos como `/etc/shadow` que sólo `root` puede editar. Gracias a SUID, los usuarios pueden cambiar sus contraseñas sin ser `root`.

#### **Verificación del SUID:**
Puedes ver si un archivo tiene el bit SUID con el comando:
```bash
ls -l programa
```
Si tiene el bit SUID activado, aparecerá como una `s` en los permisos, como en `rwsr-xr-x`.

---

### **3. SGID (Set Group ID)**

El **SGID** es similar al SUID, pero en lugar de dar privilegios al usuario propietario, otorga los privilegios del grupo propietario del archivo. También tiene un comportamiento especial cuando se aplica a directorios.

#### **¿Cómo funciona el SGID?**
- **En archivos:** El SGID establece que el programa se ejecute con los privilegios del grupo propietario, no con el grupo del usuario que ejecuta el programa. Esto es útil en entornos donde se desea que los usuarios compartan acceso a recursos pero manteniendo los permisos del grupo adecuado.
  
- **En directorios:** Cuando el SGID se aplica a un directorio, cualquier archivo creado dentro de ese directorio se asigna automáticamente al mismo grupo del directorio, no al grupo del usuario que lo creó.

#### **Ejemplo de SGID en archivos:**
Para establecer el bit SGID en un archivo, usas el siguiente comando:
```bash
chmod g+s archivo
```

#### **Ejemplo de SGID en directorios:**
Para que todos los archivos creados dentro de un directorio tengan el mismo grupo que el directorio:
```bash
chmod g+s directorio
```

- Esto es útil, por ejemplo, en entornos donde varios usuarios deben trabajar sobre archivos que pertenezcan a un mismo grupo y mantener la coherencia de los permisos.

---

### **4. Sticky Bit**

El **Sticky Bit** es un permiso especial que se aplica generalmente a directorios. Su función principal es garantizar que los archivos dentro de un directorio solo puedan ser eliminados o renombrados por el propietario del archivo o el propietario del directorio, incluso si otros usuarios tienen permisos de escritura en el directorio.

#### **¿Cómo funciona el Sticky Bit?**
Cuando un directorio tiene el sticky bit establecido, los usuarios pueden crear, modificar y acceder a archivos en el directorio, pero no pueden eliminar o renombrar archivos que no les pertenecen. Esto es especialmente útil en directorios públicos, como `/tmp`, donde los usuarios pueden tener acceso, pero no deben interferir con los archivos de otros.

#### **Ejemplo del Sticky Bit:**
Para establecer el sticky bit en un directorio:
```bash
chmod +t directorio
```

- Esto asegurará que, aunque varios usuarios puedan escribir en el directorio, solo podrán eliminar o modificar los archivos que les pertenezcan.

#### **Verificación del Sticky Bit:**
Al mostrar los permisos de un directorio con `ls -l`, si el sticky bit está activado, aparecerá como una `t` en lugar de una `x` en los permisos de "otros", por ejemplo:
```
drwxrwxrwt 2 root root 4096 dic  2 10:00 directorio
```

---

### **Resumen de los permisos especiales**

- **SUID (Set User ID):** Permite que un archivo se ejecute con los permisos del propietario, no del usuario que lo ejecuta.
- **SGID (Set Group ID):** Permite que un archivo se ejecute con los permisos del grupo propietario, o asigna automáticamente el grupo del directorio al archivo creado dentro de él.
- **Sticky Bit:** Solo el propietario de un archivo puede eliminarlo o renombrarlo dentro de un directorio con el sticky bit activado, incluso si otros usuarios tienen permisos de escritura.

---

### **Casos de uso**
- **SUID:** Se usa en programas como `passwd` o `ping` que necesitan permisos de superusuario para acceder a archivos protegidos.
- **SGID:** Se utiliza en aplicaciones compartidas por grupos de usuarios que necesitan acceder a archivos bajo el mismo grupo sin que el grupo del creador del archivo sea sobrescrito.
- **Sticky Bit:** Se usa en directorios públicos (como `/tmp`) donde los usuarios pueden almacenar archivos pero no deben eliminar o modificar los de otros usuarios.

