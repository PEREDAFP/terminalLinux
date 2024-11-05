Para que este proceso se ejecute al arrancar la máquina lo agregaremos como un servicio del sistema.
Aquí te muestro cómo hacerlo en un sistema Linux basado en systemd:

1. Crea un archivo de unidad de systemd para el servicio. Puedes crear el archivo en la ruta `/etc/systemd/system/procesosmal.service` con el siguiente contenido:

```
[Unit]
Description=Proceso a lo tonto

[Service]
ExecStart=/ruta/al/ejecutable/procesosmal
Restart=always

[Install]
WantedBy=multi-user.target
```

Asegúrate de reemplazar `/ruta/al/ejecutable/procesosmal` con la ruta real al ejecutable que creaste en el paso anterior.

2. Recarga la configuración de systemd para que reconozca el nuevo servicio:

```
sudo systemctl daemon-reload
```

3. Habilita el servicio para que se inicie automáticamente al arrancar la máquina:

```
sudo systemctl enable procesosmal
```

4. Inicia el servicio:

```
sudo systemctl start procesosmal
```

Ahora, cada vez que se inicie la máquina, el servicio `procesosmal` se iniciará automáticamente y ejecutará el proceso a lo tonto. Puedes verificar el estado del servicio con el siguiente comando:

```
sudo systemctl status procesosmal
```

Si deseas detener el servicio, puedes usar el siguiente comando:

```
sudo systemctl stop procesosmal
```

Y si deseas deshabilitar el servicio para que no se inicie automáticamente al arrancar la máquina, puedes usar el siguiente comando:

```
sudo systemctl disable procesosmal
```