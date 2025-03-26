`sar` (System Activity Reporter) es una herramienta de monitorización del rendimiento del sistema disponible en sistemas Linux y UNIX. Forma parte del paquete **sysstat** y permite recopilar, visualizar y analizar datos sobre el uso de CPU, memoria, disco, red y otros recursos del sistema.

### **Principales funciones de `sar`**

- Monitoriza el uso de **CPU**, memoria RAM y swap.
- Analiza la actividad de **discos y dispositivos de E/S**.
- Muestra el uso de la **red** y estadísticas de sockets.
- Registra la actividad del sistema a lo largo del tiempo.

### **Instalación de `sar`**

Si `sar` no está instalado en tu sistema, puedes instalarlo con:

- **Ubuntu/Debian**:

  ```bash
  sudo apt install sysstat
  ```

- **CentOS/RHEL**:

  ```bash
  sudo yum install sysstat
  ```

- **Arch Linux**:
  ```bash
  sudo pacman -S sysstat
  ```

### **Ejemplos de uso**

1. **Ver el uso de CPU en intervalos de 1 segundo, 5 veces**:

   ```bash
   sar -u 1 5
   ```

2. **Observar el uso de memoria RAM y swap**:

   ```bash
   sar -r 1 5
   ```

3. **Ver la actividad del disco**:

   ```bash
   sar -d 1 5
   ```

4. **Mostrar tráfico de red**:

   ```bash
   sar -n DEV 1 5
   ```

5. **Ver el historial de carga del sistema**:
   ```bash
   sar -q
   ```

### **Registro de datos**

Para habilitar la recolección automática de datos en sistemas basados en Debian, edita el archivo `/etc/default/sysstat` y cambia:

```bash
ENABLED="false"
```

por:

```bash
ENABLED="true"
```

Luego, reinicia el servicio:

```bash
sudo systemctl restart sysstat
```

`sar` es muy útil para analizar el rendimiento del sistema a lo largo del tiempo y detectar problemas como alto consumo de CPU, falta de memoria o cuellos de botella en el disco.
