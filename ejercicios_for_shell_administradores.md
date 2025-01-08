### 20 Ejercicios Prácticos con `for` para Administradores de Sistemas

#### **1. Iterar sobre usuarios del sistema**
**Ejercicio:**
Escribe un script que muestre todos los usuarios del sistema desde el archivo `/etc/passwd`.

**Solución:**
```bash
for user in $(cut -d: -f1 /etc/passwd); do
    echo "Usuario: $user"
done
```

---

#### **2. Comprobar conectividad a múltiples servidores**
**Ejercicio:**
Crea un script que haga ping a una lista de servidores y reporte si están accesibles.

**Solución:**
```bash
for server in google.com yahoo.com bing.com; do
    if ping -c 1 $server &> /dev/null; then
        echo "$server está accesible"
    else
        echo "$server no responde"
    fi
done
```

---

#### **3. Procesar archivos en un directorio**
**Ejercicio:**
Renombra todos los archivos `.log` en un directorio añadiendo el prefijo `backup_`.

**Solución:**
```bash
for file in *.log; do
    mv "$file" "backup_$file"
done
```

---

#### **4. Contar líneas en múltiples archivos**
**Ejercicio:**
Cuenta el número de líneas en cada archivo `.txt` en el directorio actual.

**Solución:**
```bash
for file in *.txt; do
    echo "$file tiene $(wc -l < $file) líneas"
done
```

---

#### **5. Crear múltiples usuarios**
**Ejercicio:**
Crea un script que añada 5 usuarios (`user1` a `user5`) al sistema.

**Solución:**
```bash
for i in {1..5}; do
    sudo useradd "user$i"
    echo "Usuario user$i creado"
done
```

---

#### **6. Copiar archivos a múltiples directorios**
**Ejercicio:**
Copia un archivo llamado `config.cfg` a tres directorios diferentes: `/etc/app1`, `/etc/app2` y `/etc/app3`.

**Solución:**
```bash
for dir in /etc/app1 /etc/app2 /etc/app3; do
    cp config.cfg "$dir"
    echo "Archivo copiado a $dir"
done
```

---

#### **7. Verificar permisos de archivos**
**Ejercicio:**
Muestra los permisos de todos los archivos `.sh` en el directorio actual.

**Solución:**
```bash
for script in *.sh; do
    ls -l "$script"
done
```

---

#### **8. Eliminar archivos antiguos**
**Ejercicio:**
Elimina todos los archivos `.tmp` que tengan más de 7 días.

**Solución:**
```bash
for file in $(find . -name "*.tmp" -mtime +7); do
    rm "$file"
    echo "$file eliminado"
done
```

---

#### **9. Reiniciar servicios en una lista de servidores**
**Ejercicio:**
Crea un script que reinicie el servicio `nginx` en tres servidores remotos usando SSH.

**Solución:**
```bash
for server in server1 server2 server3; do
    ssh "$server" "sudo systemctl restart nginx"
    echo "nginx reiniciado en $server"
done
```

---

#### **10. Buscar palabras clave en logs**
**Ejercicio:**
Busca la palabra "error" en todos los archivos `.log` y muestra en qué archivo aparece.

**Solución:**
```bash
for file in *.log; do
    if grep -q "error" "$file"; then
        echo "Error encontrado en $file"
    fi
done
```

---

#### **11. Crear múltiples directorios**
**Ejercicio:**
Crea directorios llamados `backup_202301`, `backup_202302`, y así hasta `backup_202312`.

**Solución:**
```bash
for month in {01..12}; do
    mkdir "backup_2023$month"
done
```

---

#### **12. Generar contraseñas para usuarios**
**Ejercicio:**
Genera una contraseña aleatoria para 5 usuarios y muéstrala en pantalla.

**Solución:**
```bash
for user in user1 user2 user3 user4 user5; do
    password=$(openssl rand -base64 12)
    echo "Contraseña para $user: $password"
done
```

---

#### **13. Cambiar permisos recursivamente**
**Ejercicio:**
Cambia los permisos de todos los archivos `.sh` en un directorio para que sean ejecutables.

**Solución:**
```bash
for script in *.sh; do
    chmod +x "$script"
    echo "Permisos cambiados para $script"
done
```

---

#### **14. Comparar archivos en dos directorios**
**Ejercicio:**
Compara los archivos `.conf` entre dos directorios y muestra las diferencias.

**Solución:**
```bash
for file in /etc/app1/*.conf; do
    diff "$file" "/etc/app2/$(basename $file)"
done
```

---

#### **15. Archivar logs antiguos**
**Ejercicio:**
Comprime todos los archivos `.log` mayores a 1 MB en un archivo tar.

**Solución:**
```bash
for file in $(find . -name "*.log" -size +1M); do
    tar -rvf logs_backup.tar "$file"
done
```

---

#### **16. Configurar permisos para múltiples usuarios**
**Ejercicio:**
Cambia el grupo de varios usuarios (`user1`, `user2`, `user3`) al grupo `admin`.

**Solución:**
```bash
for user in user1 user2 user3; do
    sudo usermod -aG admin $user
    echo "Usuario $user añadido al grupo admin"
done
```

---

#### **17. Chequear estado de servicios**
**Ejercicio:**
Verifica si los servicios `nginx`, `mysql` y `ssh` están activos en el sistema.

**Solución:**
```bash
for service in nginx mysql ssh; do
    systemctl is-active --quiet $service && echo "$service está activo" || echo "$service está inactivo"
done
```

---

#### **18. Descargar múltiples archivos**
**Ejercicio:**
Descarga una lista de archivos desde diferentes URLs.

**Solución:**
```bash
for url in https://example.com/file1 https://example.com/file2; do
    wget "$url"
done
```

---

#### **19. Limpiar archivos duplicados**
**Ejercicio:**
Elimina archivos duplicados en un directorio basándote en el comando `md5sum`.

**Solución:**
```bash
for file in *; do
    md5sum "$file" | sort | uniq -d | while read hash name; do
        echo "Eliminando duplicado: $name"
        rm "$name"
    done
done
```

---

#### **20. Actualizar paquetes en servidores remotos**
**Ejercicio:**
Actualiza los paquetes en una lista de servidores usando SSH.

**Solución:**
```bash
for server in server1 server2 server3; do
    ssh "$server" "sudo apt update && sudo apt upgrade -y"
    echo "Paquetes actualizados en $server"
done
```