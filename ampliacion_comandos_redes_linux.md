

### 1. **Configuración de red en Linux (Debian/Ubuntu)**

Primero, veremos cómo configurar interfaces de red, cambiar la puerta de enlace y gestionar la obtención de direcciones IP.

#### Actividades para configuración de red:

1. Configurar una interfaz de red estática en Debian editando el archivo `/etc/network/interfaces`.
2. Configurar una dirección IP dinámica utilizando `dhclient` en una interfaz.
3. Cambiar la puerta de enlace predeterminada usando el comando `ip`.
4. Agregar una nueva ruta estática para una red específica utilizando `ip route add`.
5. Mostrar la tabla de rutas del sistema utilizando `route` y `ip route`.
6. Configurar una dirección IP en una interfaz utilizando el comando `ip addr add`.
7. Verificar la dirección MAC de una interfaz con `ip link`.
8. Cambiar la dirección MAC de una interfaz de red usando `ip link` o `ifconfig`.
9. Desactivar temporalmente una interfaz de red utilizando `ifdown` o `ip link set`.
10. Activar una interfaz de red utilizando `ifup` o `ip link set`.
11. Verificar las estadísticas de la interfaz de red con `ip -s link`.
12. Mostrar las direcciones IP asignadas a todas las interfaces con `ip a`.
13. Configurar una interfaz de red en modo promiscuo para captura de tráfico.
14. Cambiar el servidor DNS utilizado editando el archivo `/etc/resolv.conf`.
15. Verificar si una interfaz de red ha obtenido una dirección IP mediante DHCP usando `dhclient -v`.

---

### 2. **Actividades con `mtr`**

`mtr` (My Traceroute) es una herramienta de diagnóstico de red que combina las funciones de `traceroute` y `ping` para monitorear la ruta y latencia entre el origen y el destino.

#### Actividades para `mtr`:

1. Ejecutar `mtr` para rastrear la ruta hasta un servidor público como `google.com`.
2. Ejecutar un rastreo de red en modo continuo y monitorizar la latencia.
3. Usar `mtr` con la opción de modo texto y guardar los resultados en un archivo de log.
4. Ejecutar `mtr` para un servidor específico mostrando solo 10 saltos.
5. Filtrar los resultados de `mtr` para mostrar solo las direcciones IP sin nombres de host.
6. Configurar `mtr` para usar un número específico de paquetes ICMP por salto.
7. Ejecutar `mtr` usando el puerto de destino específico para una aplicación (por ejemplo, HTTP en el puerto 80).
8. Realizar una prueba de `mtr` usando el protocolo TCP en lugar de ICMP.
9. Modificar el intervalo entre envíos de paquetes en un rastreo `mtr`.
10. Ejecutar un rastreo con `mtr` y mostrar las estadísticas en modo detallado.
11. Limitar el número de repeticiones que hace `mtr` por salto.
12. Usar `mtr` con la opción para mostrar el tiempo en milisegundos.
13. Ejecutar un rastreo `mtr` y mostrar solo la ruta más rápida.
14. Guardar el resultado de un `mtr` a un archivo y luego analizar el rendimiento de la red en diferentes momentos del día.
15. Configurar `mtr` para que no resuelva los nombres de dominio durante el rastreo.

---

### 3. **Actividades con `netstat`**

`netstat` es una herramienta que muestra conexiones de red activas, puertos abiertos, tablas de enrutamiento y estadísticas de red. Aunque está siendo reemplazada por `ss`, sigue siendo una herramienta ampliamente utilizada.

#### Actividades para `netstat`:

1. Mostrar todas las conexiones de red activas con `netstat`.
2. Mostrar solo las conexiones TCP activas utilizando `netstat`.
3. Mostrar las conexiones UDP activas utilizando `netstat`.
4. Ver el estado de las conexiones de red en tiempo real con la opción `watch` y `netstat`.
5. Mostrar las estadísticas de las interfaces de red con `netstat -i`.
6. Usar `netstat` para mostrar la tabla de enrutamiento del sistema.
7. Ver los puertos que están escuchando actualmente en el sistema con `netstat -l`.
8. Filtrar las conexiones abiertas por un puerto específico (por ejemplo, puerto 80) usando `netstat`.
9. Mostrar las estadísticas de tráfico de red (transmitidos y recibidos) usando `netstat`.
10. Mostrar las conexiones activas de una interfaz específica (por ejemplo, `eth0`) con `netstat`.
11. Usar `netstat` para mostrar todas las conexiones que utilizan IPv6.
12. Mostrar las conexiones que están en estado "LISTEN" (esperando conexiones entrantes) con `netstat`.
13. Usar `netstat` para identificar los PID asociados con conexiones activas.
14. Monitorizar el uso de los sockets UNIX locales utilizando `netstat`.
15. Verificar la cantidad de paquetes retransmitidos o perdidos a través de las estadísticas de red con `netstat`.

---

### 4. **Actividades con `tcpdump`**

`tcpdump` es una herramienta poderosa para capturar y analizar paquetes de red en tiempo real. Permite observar todo el tráfico de red que pasa a través de una interfaz.

#### Actividades para `tcpdump`:

1. Capturar todo el tráfico en una interfaz de red específica usando `tcpdump`.
2. Capturar solo los paquetes TCP en una red local con `tcpdump`.
3. Filtrar el tráfico por dirección IP de destino específica con `tcpdump`.
4. Capturar solo paquetes ICMP (ping) utilizando filtros en `tcpdump`.
5. Guardar la captura de tráfico de red en un archivo `.pcap` para su análisis posterior.
6. Capturar y analizar paquetes que utilizan el puerto 80 (HTTP) con `tcpdump`.
7. Capturar tráfico solo de una interfaz en modo promiscuo con `tcpdump`.
8. Capturar tráfico DNS y mostrar las consultas de nombre de dominio.
9. Filtrar paquetes por protocolo específico (ej: UDP) en `tcpdump`.
10. Capturar solo los primeros 100 paquetes de una conexión con `tcpdump`.
11. Mostrar el contenido de los paquetes capturados en formato hexadecimal.
12. Capturar solo tráfico de entrada o salida usando la opción `inbound` o `outbound`.
13. Utilizar `tcpdump` para capturar paquetes y luego analizarlos en Wireshark.
14. Filtrar paquetes por rango de puertos (por ejemplo, del 8000 al 9000).
15. Capturar solo paquetes con una longitud específica de bytes (por ejemplo, paquetes de 64 bytes).

---

### 5. **Actividades con `nmap`**

`nmap` es una herramienta de escaneo de redes que permite descubrir hosts y servicios en una red, así como verificar el estado de los puertos.

#### Actividades para `nmap`:

1. Escanear una dirección IP para descubrir los puertos abiertos.
2. Realizar un escaneo completo de un rango de IPs usando `nmap`.
3. Escanear un host para detectar servicios que están escuchando en los puertos abiertos.
4. Realizar un escaneo rápido de red con `nmap` utilizando la opción `-T4`.
5. Ejecutar un escaneo de puertos específicos (por ejemplo, 22, 80, 443) en un host.
6. Realizar un escaneo para detectar el sistema operativo en un servidor remoto.
7. Escanear una red local para detectar dispositivos conectados utilizando `nmap`.
8. Realizar un escaneo UDP de puertos en un servidor.
9. Ejecutar un escaneo de red silencioso o "stealth" usando la opción `-sS` (SYN scan).
10. Escanear un host remoto para detectar vulnerabilidades conocidas.
11. Realizar un escaneo de versión de servicios (detectar versiones de software) usando `-sV`.
12. Ejecutar un escaneo de puertos con `nmap` y generar un informe en formato XML.
13. Realizar un escaneo de puertos con `nmap` y mostrar solo los puertos cerrados.
14. Ejecutar un escaneo de puertos en paralelo y ver la diferencia de velocidad.
15. Escanear una red utilizando una lista de puertos personalizados con `nmap`.

---

### Ficheros log relacionados con la actividad de red

1. **`/var/log/syslog`**: Contiene registros generales del sistema, incluidas actividades de red.
2. **`/var/log/kern.log`**: Registros del kernel, incluyendo eventos de red.
3. **`/var/log/dmesg`**: Información del arranque del sistema, incluyendo la inicialización de interfaces de red.
4. **`/var/log/auth.log`**: Registros de autenticación y conexión remota.
5. **`/var/log/ufw.log`**: Registros de tráfico filtrado por el firewall UFW.
6. **`/var/log/messages`**: Información general del sistema y eventos de red.
