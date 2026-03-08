### Probamos un servicio que sólo puede activarse por socket

### 1. El Script en Python (El Backendl)

Creamos un pequeño script que simplemente devuelva un mensaje de texto cuando te conectes, pero que tome el socket directamente de systemd.

Crea el archivo `/usr/local/bin/mi-socket-app.py` y pega este código:

```python
#!/usr/bin/env python3
import socket
import sys

# La regla de oro: Systemd SIEMPRE pasa el socket en el File Descriptor 3
try:
    s = socket.fromfd(3, socket.AF_INET, socket.SOCK_STREAM)
except OSError:
    print("Error: Este script debe ser lanzado por systemd mediante un socket.")
    sys.exit(1)

# Bucle infinito para aceptar conexiones de ese socket
while True:
    conn, addr = s.accept()
    mensaje = f"¡Éxito! Conectado desde {addr}. Systemd me ha despertado.\n"
    conn.sendall(mensaje.encode('utf-8'))
    conn.close()

```

Le damos permisos de ejecución:

```bash
sudo chmod 740 /usr/local/bin/mi-socket-app.py

```

---

### 2. El archivo `.socket` (El vigilante)

Este es el archivo que le dice a systemd qué puerto escuchar.

Crea `/etc/systemd/system/mi-app.socket` y añade esto:

```ini
[Unit]
Description=Vigilante del puerto 8888

[Socket]
ListenStream=8888
# Accept=no significa que systemd pasará el socket de escucha general a Python,
# y Python se encargará de aceptar las conexiones individuales.
Accept=no

[Install]
WantedBy=sockets.target

```

---

### 3. El archivo `.service` (El ejecutor)

Este archivo arranca nuestro script. Como tienen el mismo nombre base (`mi-app`), systemd sabe que están enlazados automáticamente.

Crea `/etc/systemd/system/mi-app.service`:

```ini
[Unit]
Description=Mi Servidor Python Nativo

[Service]
ExecStart=/usr/local/bin/mi-socket-app.py
# Evita que systemd cierre los file descriptors que le está pasando a Python
NonBlocking=true

```

---

### 4. Prueba la magia

Ahora vamos a ponerlo en marcha desde cero:

```bash
# 1. Recarga systemd
sudo systemctl daemon-reload

# 2. Activa SOLO el socket
sudo systemctl enable --now mi-app.socket

```

**La comprobación:**
Si miras el estado del servicio (`systemctl status mi-app.service`), verás que está **inactivo (dead)**. El script de Python no está consumiendo ni un solo mega de RAM.

Abre otra terminal o usa la misma y conéctate al puerto usando `nc` (Netcat) o `telnet`:

```bash
nc localhost 8888

```

Al instante, recibirás el mensaje: `"¡Éxito! Conectado desde... Systemd me ha despertado."`

Si ahora vuelves a comprobar el estado del servicio (`systemctl status mi-app.service`), verás que está **activo (running)**. Systemd lo encendió en el milisegundo en que hiciste la petición y le entregó el control.

Cambia el número de puerto. Reinicia la máquina y comprueba que puedes conectarte a ese puerto.

Para finalizar deja el systemd como estaba al principio.
