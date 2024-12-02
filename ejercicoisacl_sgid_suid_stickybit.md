
### **Actividades para comprobar el funcionamiento de SUID, SGID, Sticky Bit y ACLs**

---

### **1. Actividad: Comprobar el funcionamiento de SUID**

#### **Objetivo:**
Ver cómo el bit **SUID** permite que un archivo se ejecute con los permisos del propietario del archivo (normalmente `root`).

#### **Instrucciones:**
1. Crea un archivo de prueba, por ejemplo `prueba_suid.sh`, con el siguiente contenido:
   ```bash
   #!/bin/bash
   id
   ```
   Este script muestra el ID del usuario que lo ejecuta.

2. Asigna permisos de ejecución al archivo:
   ```bash
   chmod +x prueba_suid.sh
   ```

3. Cambia el propietario del archivo a `root`:
   ```bash
   sudo chown root:root prueba_suid.sh
   ```

4. Establece el bit SUID en el archivo:
   ```bash
   sudo chmod u+s prueba_suid.sh
   ```

5. Ejecuta el archivo como un usuario normal (que no sea `root`):
   ```bash
   ./prueba_suid.sh
   ```

#### **Resultado esperado:**
- El script debería mostrar que el ID de usuario es el de `root`, aunque lo hayas ejecutado como un usuario normal. Esto ocurre porque el bit **SUID** hace que el script se ejecute con los privilegios del propietario (en este caso, `root`).

---

### **2. Actividad: Comprobar el funcionamiento de SGID en archivos**

#### **Objetivo:**
Ver cómo el bit **SGID** permite que un archivo se ejecute con los permisos del grupo propietario.

#### **Instrucciones:**
1. Crea un archivo de prueba, por ejemplo `prueba_sgid.sh`, con el siguiente contenido:
   ```bash
   #!/bin/bash
   groups
   ```

2. Asigna permisos de ejecución al archivo:
   ```bash
   chmod +x prueba_sgid.sh
   ```

3. Cambia el grupo del archivo a un grupo específico, por ejemplo `grupo1`:
   ```bash
   sudo chgrp grupo1 prueba_sgid.sh
   ```

4. Establece el bit **SGID** en el archivo:
   ```bash
   sudo chmod g+s prueba_sgid.sh
   ```

5. Ejecuta el archivo como un usuario que no pertenezca al grupo `grupo1`:
   ```bash
   ./prueba_sgid.sh
   ```

#### **Resultado esperado:**
- El comando `groups` debería mostrar que el grupo es el del propietario del archivo (`grupo1`), no el grupo del usuario que ejecuta el script. Esto es posible gracias al bit **SGID**.

---

### **3. Actividad: Comprobar el funcionamiento de SGID en directorios**

#### **Objetivo:**
Ver cómo el bit **SGID** afecta a los archivos creados dentro de un directorio, asignando automáticamente el grupo del directorio.

#### **Instrucciones:**
1. Crea un directorio llamado `directorio_sgid`:
   ```bash
   mkdir directorio_sgid
   ```

2. Cambia el grupo del directorio a un grupo específico, por ejemplo `grupo1`:
   ```bash
   sudo chgrp grupo1 directorio_sgid
   ```

3. Establece el bit **SGID** en el directorio:
   ```bash
   sudo chmod g+s directorio_sgid
   ```

4. Crea un archivo dentro del directorio como un usuario que no pertenezca al grupo `grupo1`:
   ```bash
   touch directorio_sgid/archivo1.txt
   ```

5. Verifica el grupo del archivo recién creado:
   ```bash
   ls -l directorio_sgid/archivo1.txt
   ```

#### **Resultado esperado:**
- El grupo del archivo `archivo1.txt` debería ser `grupo1`, no el grupo del usuario que lo creó. Esto ocurre gracias al bit **SGID** en el directorio.

---

### **4. Actividad: Comprobar el funcionamiento del Sticky Bit**

#### **Objetivo:**
Ver cómo el **Sticky Bit** restringe la eliminación o renombrado de archivos dentro de un directorio, permitiendo solo a los propietarios de los archivos realizar estas acciones.

#### **Instrucciones:**
1. Crea un directorio llamado `directorio_sticky`:
   ```bash
   mkdir directorio_sticky
   ```

2. Establece el **Sticky Bit** en el directorio:
   ```bash
   sudo chmod +t directorio_sticky
   ```

3. Crea dos archivos dentro del directorio, uno como un usuario diferente:
   ```bash
   touch directorio_sticky/archivo1.txt
   sudo -u usuario1 touch directorio_sticky/archivo2.txt
   ```

4. Intenta eliminar el archivo `archivo2.txt` desde tu usuario (sin ser el propietario):
   ```bash
   rm directorio_sticky/archivo2.txt
   ```

5. Intenta eliminar el archivo `archivo1.txt` desde el usuario propietario:
   ```bash
   rm directorio_sticky/archivo1.txt
   ```

#### **Resultado esperado:**
- **El archivo `archivo2.txt` no podrá ser eliminado** por el usuario que no es su propietario, debido a que el **Sticky Bit** está activado.
- **El archivo `archivo1.txt` podrá ser eliminado** por su propietario.

---

### **5. Actividad: Comprobar el funcionamiento de ACL**

#### **Objetivo:**
Ver cómo las **ACLs** permiten otorgar permisos más detallados a usuarios y grupos específicos en archivos y directorios.

#### **Instrucciones:**
1. Asegúrate de que las ACLs estén habilitadas en tu sistema (si no, instala el paquete `acl`):
   ```bash
   sudo apt install acl
   ```

   ```bash
   touch archivo_acl.txt
   ```

3. Asigna permisos de lectura a un usuario específico, por ejemplo `usuario1`:
   ```bash
   setfacl -m u:usuario1:r archivo_acl.txt
   ```

4. Verifica los permisos ACL del archivo:
   ```bash
   getfacl archivo_acl.txt
   ```

5. Elimina la ACL para el usuario `usuario1`:
   ```bash
   setfacl -x u:usuario1 archivo_acl.txt
   ```

6. Verifica nuevamente las ACLs del archivo:
   ```bash
   getfacl archivo_acl.txt
   ```

#### **Resultado esperado:**
- Después de añadir la ACL, el archivo debe mostrar que `usuario1` tiene permisos de lectura.
- Después de eliminar la ACL, ya no aparecerá la entrada para `usuario1`.

---

### **Resumen de Actividades**
Estas actividades te permitirán:
- Ver cómo el **SUID** permite que los archivos se ejecuten con los privilegios del propietario del archivo (por lo general, `root`).
- Entender cómo el **SGID** afecta tanto a los archivos como a los directorios, estableciendo los permisos de grupo.
- Experimentar con el **Sticky Bit** en directorios para limitar la eliminación de archivos a sus propietarios.
- Comprobar el funcionamiento de **ACLs**, que proporcionan un control de acceso más detallado y específico que los permisos tradicionales.

