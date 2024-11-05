Obtener el PID de un proceso lanzado por un servicio que no podemos parar por tener un Restart=always en su .service
1. Ejecuta el siguiente comando para obtener el PID del proceso que deseas investigar:

```
pgrep procesosmal
```
o

```
lsof -f | grep procesomal
```

Esto mostrará el PID del proceso `procesomal` en la salida estándar.

2. Una vez que tengas el PID del proceso, puedes utilizar el siguiente comando para obtener el nombre del servicio que lo está lanzando:

```
systemctl status $(ps -o unit:1 -p <PID>)
```

Reemplaza `<PID>` con el PID del proceso que obtuviste en el paso anterior. Este comando utiliza el comando `ps` para obtener el nombre de la unidad systemd asociada con el PID especificado, y luego utiliza el comando `systemctl status` para obtener información detallada sobre el servicio.

Por ejemplo, si el PID del proceso `procesosmal` es `12345`, el comando completo sería:

```
systemctl status $(ps -o unit:1 -p 12345)
```

Esto mostrará información detallada sobre el servicio que está lanzando el proceso `procesosmal`, incluyendo su nombre.