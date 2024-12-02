### **Sesión: Permisos y Usuarios en Linux**

#### **Introducción a Permisos y Usuarios en Linux**

En Linux, los permisos y usuarios son fundamentales para gestionar la seguridad y el acceso a los recursos del sistema. Cada archivo o directorio tiene permisos asignados para el propietario, el grupo y otros usuarios. 

Los permisos principales son:
- **r** (read): Permite leer el contenido del archivo o listar el directorio.
- **w** (write): Permite modificar el archivo o añadir/eliminar elementos en el directorio.
- **x** (execute): Permite ejecutar un archivo o acceder al contenido del directorio.

Los permisos están organizados en tres conjuntos:
1. Propietario (owner).
2. Grupo (group).
3. Otros (others).

Se representan con códigos numéricos (octales) o simbólicos:
- **Octales:** 4 (r), 2 (w), 1 (x).
- **Simbólicos:** `chmod u+x` (agrega ejecución al propietario).

---

### **40 Ejercicios de Permisos y Usuarios en Linux**

#### **Sección 1: Gestión de Usuarios**
1. Crear un nuevo usuario llamado `usuario1`.
   ```bash
   sudo adduser usuario1
   ```
2. Cambiar la contraseña del usuario `usuario1`.
   ```bash
   sudo passwd usuario1
   ```
3. Crear un grupo llamado `grupo1`.
   ```bash
   sudo groupadd grupo1
   ```
4. Añadir `usuario1` al grupo `grupo1`.
   ```bash
   sudo usermod -aG grupo1 usuario1
   ```
5. Listar todos los usuarios del sistema.
   ```bash
   cat /etc/passwd
   ```
6. Ver los grupos a los que pertenece `usuario1`.
   ```bash
   groups usuario1
   ```
7. Cambiar el grupo principal de `usuario1` a `grupo1`.
   ```bash
   sudo usermod -g grupo1 usuario1
   ```
8. Eliminar el usuario `usuario1` (con todos sus archivos).
   ```bash
   sudo userdel -r usuario1
   ```
9. Cambiar el nombre de un usuario (por ejemplo, `usuario1` a `usuario2`).
   ```bash
   sudo usermod -l usuario2 usuario1
   ```
10. Ver los usuarios conectados actualmente al sistema.
    ```bash
    who
    ```

---

#### **Sección 2: Gestión de Permisos Básicos**
11. Crear un archivo `archivo1.txt`.
    ```bash
    touch archivo1.txt
    ```
12. Ver los permisos de `archivo1.txt`.
    ```bash
    ls -l archivo1.txt
    ```
13. Cambiar los permisos de `archivo1.txt` para que solo el propietario pueda leerlo y escribirlo.
    ```bash
    chmod 600 archivo1.txt
    ```
14. Hacer que `archivo1.txt` sea ejecutable para el propietario.
    ```bash
    chmod u+x archivo1.txt
    ```
15. Permitir que el grupo tenga permiso de escritura sobre `archivo1.txt`.
    ```bash
    chmod g+w archivo1.txt
    ```
16. Denegar todos los permisos a otros usuarios sobre `archivo1.txt`.
    ```bash
    chmod o-rwx archivo1.txt
    ```
17. Asignar permisos `rw-r--r--` (octal 644) a `archivo1.txt`.
    ```bash
    chmod 644 archivo1.txt
    ```
18. Crear un directorio `directorio1`.
    ```bash
    mkdir directorio1
    ```
19. Permitir a todos los usuarios acceder y ejecutar el directorio `directorio1`.
    ```bash
    chmod 755 directorio1
    ```
20. Cambiar el propietario de `archivo1.txt` a `usuario1`.
    ```bash
    sudo chown usuario1 archivo1.txt
    ```

---

#### **Sección 3: Permisos Avanzados**
21. Cambiar el grupo de `archivo1.txt` a `grupo1`.
    ```bash
    sudo chgrp grupo1 archivo1.txt
    ```
22. Crear un archivo y establecer su bit SUID.
    ```bash
    chmod u+s archivo1.txt
    ```
23. Crear un directorio y establecer su bit SGID.
    ```bash
    chmod g+s directorio1
    ```
24. Crear un directorio y habilitar el sticky bit.
    ```bash
    chmod +t directorio1
    ```
25. Asignar permisos `rwxr-xr--` a `archivo1.txt` usando la representación simbólica.
    ```bash
    chmod u=rwx,g=rx,o=r archivo1.txt
    ```
26. Eliminar el bit de ejecución para el grupo y otros en `archivo1.txt`.
    ```bash
    chmod go-x archivo1.txt
    ```
27. Crear un archivo y otorgarle permisos `r-xrwxr--`.
    ```bash
    chmod 475 archivo1.txt
    ```
28. Ver el umask actual del sistema.
    ```bash
    umask
    ```
29. Cambiar el umask a `0022`.
    ```bash
    umask 0022
    ```
30. Crear un archivo después de cambiar el umask y verificar sus permisos.

---

#### **Sección 4: Ejercicios con ACL (Access Control List)**
31. Instalar `acl` (si no está instalado).
    ```bash
    sudo apt install acl
    ```
32. Permitir que un usuario específico (`usuario1`) tenga acceso de lectura a `archivo1.txt`.
    ```bash
    setfacl -m u:usuario1:r archivo1.txt
    ```
33. Ver las ACL asignadas a un archivo.
    ```bash
    getfacl archivo1.txt
    ```
34. Quitar las ACL de un archivo.
    ```bash
    setfacl -b archivo1.txt
    ```
35. Permitir que un grupo específico (`grupo1`) tenga acceso completo a un archivo.
    ```bash
    setfacl -m g:grupo1:rwx archivo1.txt
    ```
36. Crear un directorio con ACL por defecto para su contenido.
    ```bash
    setfacl -d -m u:usuario1:rw directorio1
    ```
37. Permitir que todos los usuarios tengan permisos de solo lectura en `archivo1.txt`.
    ```bash
    setfacl -m o::r archivo1.txt
    ```
38. Asignar permisos específicos a múltiples usuarios en un archivo.
    ```bash
    setfacl -m u:usuario1:rw,u:usuario2:r archivo1.txt
    ```
39. Verificar si un sistema soporta ACL.
    ```bash
    mount | grep acl
    ```
40. Eliminar el acceso de un usuario específico de las ACL.
    ```bash
    setfacl -x u:usuario1 archivo1.txt
    ```

---
