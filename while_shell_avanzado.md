20 ejercicios en **Shell scripting con bucles `while`** orientados a administradores de sistemas:

---

### **Gestión de usuarios y permisos**
1. **Verificar si existen usuarios en una lista**
```bash
#!/bin/bash
while read usuario; do
    if id "$usuario" &>/dev/null; then
        echo "Usuario $usuario existe."
    else
        echo "Usuario $usuario no existe."
    fi
done < usuarios.txt
```

2. **Monitorizar intentos fallidos de login**
```bash
#!/bin/bash
while true; do
    grep "Failed password" /var/log/auth.log | tail -n 10
    sleep 10
done
```

3. **Cambiar permisos a una lista de archivos**
```bash
#!/bin/bash
while read archivo; do
    if [ -f "$archivo" ]; then
        chmod 644 "$archivo"
        echo "Permisos de $archivo cambiados a 644."
    else
        echo "Archivo $archivo no encontrado."
    fi
done < archivos.txt
```

4. **Detectar cuentas inactivas y eliminarlas**
```bash
#!/bin/bash
while read usuario; do
    if [ "$(lastlog -u $usuario | awk 'NR==2 {print $4}')" == "**Never logged in**" ]; then
        echo "Eliminando usuario inactivo: $usuario"
        userdel "$usuario"
    fi
done < usuarios.txt
```

5. **Crear múltiples usuarios automáticamente**
```bash
#!/bin/bash
while IFS=',' read usuario contrasena; do
    if id "$usuario" &>/dev/null; then
        echo "El usuario $usuario ya existe."
    else
        useradd -m -p "$(openssl passwd -crypt $contrasena)" "$usuario"
        echo "Usuario $usuario creado."
    fi
done < usuarios.csv
```

---

### **Gestión de procesos y recursos**
6. **Finalizar procesos con alto consumo de CPU**
```bash
#!/bin/bash
while true; do
    for pid in $(ps -eo pid,%cpu --sort=-%cpu | awk '$2 > 80 {print $1}'); do
        echo "Matando proceso $pid por alto uso de CPU."
        kill -9 "$pid"
    done
    sleep 10
done
```

7. **Monitorizar memoria libre**
```bash
#!/bin/bash
while true; do
    memoria=$(free -m | awk '/Mem:/ {print $4}')
    if [ "$memoria" -lt 200 ]; then
        echo "ALERTA: Memoria libre baja: ${memoria}MB"
    fi
    sleep 10
done
```

8. **Controlar uso de disco**
```bash
#!/bin/bash
while true; do
    uso=$(df / | awk 'NR==2 {print $5}' | sed 's/%//')
    if [ "$uso" -gt 80 ]; then
        echo "ALERTA: Uso de disco del sistema superior al 80%."
    fi
    sleep 30
done
```

9. **Reiniciar servicios automáticamente si fallan**
```bash
#!/bin/bash
while true; do
    if ! systemctl is-active --quiet nginx; then
        echo "Reiniciando servicio nginx."
        systemctl restart nginx
    fi
    sleep 5
done
```

10. **Generar reportes de procesos en ejecución**
```bash
#!/bin/bash
while true; do
    ps -eo pid,comm,%mem --sort=-%mem | head -n 10 > reporte_procesos.txt
    echo "Reporte generado: $(date)"
    sleep 600
done
```

---

### **Automatización de tareas**
11. **Realizar backups en bucle**
```bash
#!/bin/bash
while true; do
    rsync -av --update /ruta/origen/ /ruta/destino/
    echo "Backup completado a las $(date)"
    sleep 86400  # 24 horas
done
```

12. **Enviar mensajes de alerta a usuarios conectados**
```bash
#!/bin/bash
while true; do
    for usuario in $(who | awk '{print $1}'); do
        echo "Mensaje de alerta: Mantén tu sesión segura." | write "$usuario"
    done
    sleep 60
done
```

13. **Actualizar software automáticamente**
```bash
#!/bin/bash
while read paquete; do
    if apt list --upgradable | grep -q "$paquete"; then
        echo "Actualizando $paquete."
        apt-get install -y "$paquete"
    fi
done < paquetes.txt
```

14. **Eliminar archivos temporales antiguos**
```bash
#!/bin/bash
while true; do
    find /tmp -type f -mtime +7 -exec rm -f {} \;
    echo "Archivos temporales eliminados."
    sleep 3600
done
```

15. **Escanear puertos abiertos en la red local**
```bash
#!/bin/bash
while true; do
    nmap -p 1-65535 192.168.1.0/24 > puertos_abiertos.txt
    echo "Escaneo completado a las $(date)"
    sleep 1800
done
```

---

### **Seguridad y registros**
16. **Buscar intentos de intrusión en logs**
```bash
#!/bin/bash
while true; do
    grep -E "failed|unauthorized|error" /var/log/auth.log | tail -n 5
    sleep 10
done
```

17. **Verificar integridad de archivos**
```bash
#!/bin/bash
while read archivo; do
    if [ -f "$archivo" ]; then
        checksum=$(sha256sum "$archivo" | awk '{print $1}')
        echo "Archivo: $archivo, Checksum: $checksum"
    fi
done < archivos.txt
```

18. **Bloquear direcciones IP maliciosas**
```bash
#!/bin/bash
while true; do
    for ip in $(grep "Failed password" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | awk '$1 > 5 {print $2}'); do
        echo "Bloqueando IP $ip"
        iptables -A INPUT -s "$ip" -j DROP
    done
    sleep 600
done
```

19. **Analizar logs del sistema periódicamente**
```bash
#!/bin/bash
while true; do
    grep "error" /var/log/syslog | tail -n 20 > errores.log
    echo "Errores registrados: $(date)"
    sleep 3600
done
```

20. **Revisar conexiones activas y desconectar sospechosas**
```bash
#!/bin/bash
while true; do
    netstat -ntu | awk '$6 == "ESTABLISHED" && $5 ~ /:12345/ {print $5}' | while read ip; do
        echo "Desconectando $ip"
        iptables -A INPUT -s "$ip" -j DROP
    done
    sleep 60
done
```

---

Cada uno de estos scripts puede ser personalizado según las necesidades específicas del sistema o del administrador.