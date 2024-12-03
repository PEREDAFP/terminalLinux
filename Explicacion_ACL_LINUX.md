### **Control de Acceso con ACL (Access Control Lists) en Linux**

En un sistema Linux, los permisos estándar (lectura, escritura y ejecución) para archivos y directorios son gestionados mediante tres tipos de usuarios: el propietario del archivo, el grupo al que pertenece el archivo y los demás usuarios. Sin embargo, este modelo de permisos es bastante limitado cuando se requiere un control más granular sobre quién puede acceder a qué archivo o directorio, especialmente en sistemas multiusuario complejos.

Para abordar estas limitaciones, **ACL (Access Control Lists)** fue introducido. Las ACL permiten definir permisos más específicos para usuarios y grupos, de forma que puedas establecer reglas detalladas sobre qué usuarios pueden realizar qué operaciones sobre los archivos.

### **Conceptos Básicos de ACL**

1. **ACL estándar**: Permite definir permisos para tres clases de usuarios:
   - **User (u)**: Usuario propietario del archivo.
   - **Group (g)**: Grupo propietario del archivo.
   - **Other (o)**: Todos los demás usuarios.
   
   Estos permisos son los que gestionan los permisos clásicos de Linux mediante `chmod`.

2. **ACL extendidas**: Permiten asignar permisos más detallados para:
   - **User (u)**: Permiso para un usuario específico.
   - **Group (g)**: Permiso para un grupo específico.
   - **Mask (m)**: Define el máximo conjunto de permisos que un grupo puede tener.
   - **Other (o)**: Permiso para todos los demás usuarios.

### **Habilitar y gestionar ACL en Linux**

#### 1. **Verificar si el sistema de archivos soporta ACL**

Antes de usar ACL, debes asegurarte de que el sistema de archivos esté montado con soporte para ACL. Para verificar si un sistema de archivos tiene habilitado el soporte de ACL:

- **Comando para verificar los parámetros de montaje**:
  ```bash
  mount | grep acl
  ```

Si el sistema de archivos tiene soporte para ACL, debería mostrar algo como `acl` en las opciones de montaje. Si no, puedes habilitar ACL en el montaje modificando `/etc/fstab` o montando el sistema de archivos con la opción `acl`.

#### 2. **Comandos para trabajar con ACL**

Aquí están los comandos más importantes para gestionar ACL en Linux.

1. **Ver ACL de un archivo o directorio**:
   Utiliza el comando `getfacl` para ver las ACL de un archivo o directorio:
   ```bash
   getfacl archivo_o_directorio
   ```

   Esto muestra las ACL del archivo o directorio, incluyendo los permisos para el propietario, el grupo y otros usuarios.

   Ejemplo de salida:
   ```
   # file: archivo.txt
   # owner: usuario
   # group: grupo
   user::rw-
   group::r--
   other::r--
   ```

2. **Asignar una ACL a un archivo o directorio**:
   Para asignar permisos específicos a un usuario o grupo, utilizamos el comando `setfacl`. Por ejemplo:

   - **Agregar un permiso de lectura para el usuario `usuario2`**:
     ```bash
     setfacl -m u:usuario2:r archivo.txt
     ```

   - **Agregar un permiso de escritura para el grupo `grupo2`**:
     ```bash
     setfacl -m g:grupo2:w archivo.txt
     ```

   - **Asignar permisos de lectura y ejecución para el usuario `usuario2` y escritura para el grupo `grupo2`**:
     ```bash
     setfacl -m u:usuario2:rx archivo.txt
     setfacl -m g:grupo2:w archivo.txt
     ```

3. **Eliminar una ACL de un archivo o directorio**:
   Para eliminar una ACL que has configurado, puedes usar el siguiente comando:

   - **Eliminar la ACL de un usuario específico**:
     ```bash
     setfacl -x u:usuario2 archivo.txt
     ```

4. **Eliminar todas las ACL de un archivo o directorio**:
   Si deseas eliminar todas las ACL de un archivo o directorio y restaurar los permisos estándar de Unix, puedes usar:

   ```bash
   setfacl -b archivo.txt
   ```

5. **Asignar un permiso de "máscara" (mask)**:
   La máscara controla los permisos máximos que pueden ser asignados a los grupos en un archivo. Para establecerla:

   ```bash
   setfacl -m m::r archivo.txt
   ```

   Esto asigna el permiso de lectura a la máscara para el archivo `archivo.txt`.

### **Ejemplos de Uso de ACL**

Imagina que tienes un archivo llamado `documento.txt` y deseas otorgar permisos específicos a varios usuarios y grupos. A continuación se muestran varios ejemplos de cómo hacerlo.

1. **Asignar permisos de lectura y escritura para un usuario específico (`usuario1`)**:
   ```bash
   setfacl -m u:usuario1:rw documento.txt
   ```

2. **Otorgar permisos de solo lectura al grupo `grupo1`**:
   ```bash
   setfacl -m g:grupo1:r documento.txt
   ```

3. **Dar permisos de lectura, escritura y ejecución al usuario `usuario2` y solo lectura al grupo `grupo2`**:
   ```bash
   setfacl -m u:usuario2:rwx documento.txt
   setfacl -m g:grupo2:r documento.txt
   ```

4. **Ver las ACL del archivo**:
   Para ver cómo quedaron las ACL después de los cambios:
   ```bash
   getfacl documento.txt
   ```

   Salida posible:
   ```
   # file: documento.txt
   # owner: usuario
   # group: grupo
   user::rw-
   user:usuario1:rw-
   group::r--
   group:grupo1:r--
   group:grupo2:r--
   mask::r--
   other::r--
   ```

### **Comportamiento de las ACL**:
1. **Permiso más específico**: Las ACL ofrecen una forma más detallada de gestionar permisos. Si un archivo tiene una ACL, esta toma precedencia sobre los permisos tradicionales.
2. **Herencia de ACL en directorios**: Cuando se usan ACL en directorios, los archivos creados dentro de ese directorio heredan las ACL del directorio, lo que facilita la gestión de permisos.
   - Ejemplo: Si un directorio tiene una ACL que da permisos a `grupo2`, los archivos creados dentro de ese directorio por cualquier miembro de `grupo2` heredarán esos permisos automáticamente.

### **Eliminar y Restaurar las ACL**:
Si deseas quitar todos los permisos de ACL de un archivo y dejar solo los permisos tradicionales de Linux, puedes usar:

```bash
setfacl -b archivo.txt
```

Este comando elimina todas las ACL asignadas a `archivo.txt` y restaura los permisos tradicionales de usuario, grupo y otros.

### **Resumiendo los Comandos Importantes**:
1. **Ver las ACL de un archivo**:
   ```bash
   getfacl archivo.txt
   ```

2. **Asignar una ACL**:
   ```bash
   setfacl -m u:usuario:r archivo.txt
   setfacl -m g:grupo:rw archivo.txt
   ```

3. **Eliminar una ACL**:
   ```bash
   setfacl -x u:usuario archivo.txt
   ```

4. **Eliminar todas las ACL**:
   ```bash
   setfacl -b archivo.txt
   ```

5. **Verificar si un sistema de archivos soporta ACL**:
   ```bash
   mount | grep acl
   ```

