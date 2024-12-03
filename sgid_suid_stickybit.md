Las propiedades de los permisos especiales `SGID`, `SUID` y `Sticky Bit` en Linux son conceptos fundamentales para la gestión de permisos y seguridad de archivos y directorios. 

### 1. **SUID (Set User ID)**
El **SUID** (Set User ID) es un permiso especial que se aplica a archivos ejecutables. Cuando un archivo tiene el bit SUID activado, el proceso que ejecuta ese archivo obtiene los privilegios del propietario del archivo, no del usuario que ejecuta el archivo. Esto es útil para programas que requieren privilegios elevados (por ejemplo, `passwd`, que permite cambiar contraseñas de usuarios).

- **Cómo se activa el SUID**: Se utiliza el comando `chmod` con el valor `4000`. Por ejemplo:
  ```bash
  chmod u+s archivo
  ```

- **Ejemplo práctico**: Si creamos un archivo ejecutable con permisos SUID, el usuario que lo ejecute obtiene permisos del propietario del archivo.

  Vamos a modificar el código anterior para demostrar cómo aplicar SUID al programa creado.

  **Código modificado (con SUID)**:
  ```c
  #include <stdio.h>
  #include <sys/stat.h>
  #include <sys/types.h>

  int main() {
      const char *directorio = "/home/madrid";

      if (mkdir(directorio, 0755) == -1) {
          perror("Error al crear el directorio");
          return 1;
      }

      printf("Directorio '%s' creado exitosamente.\n", directorio);
      return 0;
  }
  ```

  Después de compilar el archivo (como se explicó anteriormente), se puede activar el bit SUID con:
  ```bash
  chmod u+s crear_directorio
  ```

  Al ejecutar el programa `./crear_directorio`, si el propietario del archivo es root, el programa se ejecutará con privilegios de root, aunque el usuario que lo ejecuta no sea root.

### 2. **SGID (Set Group ID)**
El **SGID** (Set Group ID) se aplica a los archivos y directorios. Para archivos ejecutables, el SGID funciona de manera similar al SUID: hace que el proceso que ejecuta el archivo obtenga los privilegios del grupo del archivo en lugar del grupo del usuario que ejecuta el archivo.

Para directorios, el SGID tiene un comportamiento diferente: cuando un archivo es creado dentro de un directorio con el bit SGID, el archivo hereda el grupo del directorio, no el grupo del usuario que lo crea.

- **Cómo se activa el SGID**: Se utiliza el comando `chmod` con el valor `2000`. Por ejemplo:
  ```bash
  chmod g+s directorio
  ```

  **Ejemplo práctico (con SGID en directorio)**:
  Si quieres que todos los archivos creados en el directorio `/home/madrid` hereden el grupo del directorio en lugar del grupo del usuario, puedes aplicar el bit SGID al directorio.

  Ejemplo:
  ```bash
  chmod g+s /home/madrid
  ```

  De esta manera, cualquier archivo creado dentro de `/home/madrid` tendrá el grupo del directorio, no el grupo del usuario que lo crea.

### 3. **Sticky Bit**
El **Sticky Bit** se aplica a directorios y es utilizado para asegurar que los archivos dentro de un directorio solo puedan ser eliminados o renombrados por su propietario o el root, aunque otros usuarios tengan permisos de escritura en ese directorio.

- **Cómo se activa el Sticky Bit**: Se utiliza el comando `chmod` con el valor `1000`. Por ejemplo:
  ```bash
  chmod +t directorio
  ```

  **Ejemplo práctico (con Sticky Bit en directorio)**:
  Si activas el Sticky Bit en un directorio, los usuarios solo podrán eliminar o renombrar los archivos que sean de su propiedad, incluso si tienen permisos de escritura en el directorio.

  Ejemplo:
  ```bash
  chmod +t /home/madrid
  ```

### Resumen de los comandos para cada permiso especial:

1. **SUID (Set User ID)**
   - Para archivos ejecutables:
     ```bash
     chmod u+s archivo
     ```
   
2. **SGID (Set Group ID)**
   - Para archivos ejecutables (funciona como SUID):
     ```bash
     chmod g+s archivo
     ```
   - Para directorios (heredar grupo del directorio):
     ```bash
     chmod g+s directorio
     ```

3. **Sticky Bit**
   - Para directorios (impide que los usuarios eliminen archivos de otros):
     ```bash
     chmod +t directorio
     ```

### Activación de los permisos en el código proporcionado:

En el código que proporcioné antes para crear el directorio `/home/madrid`, si deseas que el directorio tenga uno de estos permisos especiales, puedes agregar las siguientes líneas después de crear el directorio:

1. **Aplicar SUID al archivo ejecutable** (aunque en este caso no tiene mucho efecto, ya que no se está ejecutando con privilegios elevados):
   ```bash
   chmod u+s crear_directorio
   ```

2. **Aplicar SGID a un directorio**:
   ```bash
   chmod g+s /home/madrid
   ```

3. **Aplicar Sticky Bit a un directorio**:
   ```bash
   chmod +t /home/madrid
   ```

Recuerda que **SUID** y **SGID** sólo se aplican a archivos ejecutables binarios, no script,  y **Sticky Bit** a directorios.