
### **Paso 1: Preparativos iniciales**
1. **Instala una máquina virtual:**
   - Descarga e instala VirtualBox, VMware, o cualquier otro software de virtualización.

2. **Descarga la ISO de Linux:**
   - Descarga una distribución de Linux adecuada para servidores, como Ubuntu Server o CentOS.

3. **Configura la máquina virtual:**
   - Asigna al menos **1 GB de RAM** y **20 GB de almacenamiento**.
   - Añade **tres discos duros adicionales** (simularán los discos para el RAID):
     - En VirtualBox, ve a **Configuración > Almacenamiento > Añadir disco duro** y crea tres discos virtuales adicionales (5-10 GB cada uno).

---

### **Paso 2: Instalación de Linux**
1. Inicia la máquina virtual con la ISO de Linux.
2. Sigue el asistente de instalación y asegúrate de instalar un entorno mínimo sin GUI.
3. Una vez instalado el sistema operativo, inicia sesión con el usuario configurado.

---

### **Paso 3: Configuración del RAID**
#### 1. **Verifica los discos disponibles**
   En la terminal, usa el comando:
   ```bash
   lsblk
   ```
   Deberías ver los discos adicionales (por ejemplo: `/dev/sdb`, `/dev/sdc`, `/dev/sdd`).

#### 2. **Instala herramientas para RAID**
   Si estás en Ubuntu:
   ```bash
   sudo apt update
   sudo apt install mdadm
   ```

#### 3. **Crea un RAID**
   Decide el tipo de RAID (RAID 0, 1, 5, etc.). A continuación, un ejemplo para RAID 5:
   ```bash
   sudo mdadm --create --verbose /dev/md0 --level=5 --raid-devices=3 /dev/sdb /dev/sdc /dev/sdd
   ```

   - `/dev/md0` es el dispositivo RAID que se crea.
   - `--level=5` especifica RAID 5.
   - `--raid-devices=3` indica el número de discos.

#### 4. **Confirma la creación del RAID**
   Para verificar el estado del RAID:
   ```bash
   cat /proc/mdstat
   sudo mdadm --detail /dev/md0
   ```

#### 5. **Formatea y monta el RAID**
   - Formatea el RAID con un sistema de archivos, por ejemplo, ext4:
     ```bash
     sudo mkfs.ext4 /dev/md0
     ```
   - Crea un punto de montaje y monta el RAID:
     ```bash
     sudo mkdir /mnt/raid
     sudo mount /dev/md0 /mnt/raid
     ```
   - Verifica que esté montado:
     ```bash
     df -h
     ```

---

### **Paso 4: Configuración persistente**
1. **Guarda la configuración del RAID:**
   ```bash
   sudo mdadm --detail --scan >> /etc/mdadm/mdadm.conf
   ```

2. **Configura el montaje automático:**
   - Edita el archivo `/etc/fstab`:
     ```bash
     sudo nano /etc/fstab
     ```
   - Añade esta línea al final:
     ```
     /dev/md0 /mnt/raid ext4 defaults 0 0
     ```

---

### **Paso 5: Pruebas**
1. Crea archivos en el RAID para confirmar que funciona.
2. Simula un fallo eliminando un disco:
   ```bash
   sudo mdadm --fail /dev/md0 /dev/sdb
   sudo mdadm --remove /dev/md0 /dev/sdb
   ```
   - Reemplázalo y vuelve a añadirlo:
     ```bash
     sudo mdadm --add /dev/md0 /dev/sdb
     ```

