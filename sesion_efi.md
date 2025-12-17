# EFI (Extensible Firmware Interface)

## 1. Introducción

En los sistemas actuales, el antiguo BIOS ha sido sustituido por **UEFI (Unified Extensible Firmware Interface)**, también conocido de forma genérica como **EFI**. UEFI es una especificación que define una interfaz moderna entre el firmware del equipo y el sistema operativo, aportando mayor seguridad, flexibilidad y capacidad de gestión del arranque.

En este documento trabajaremos:

- Cómo funciona EFI/UEFI.
- La estructura de arranque en sistemas modernos.
- El uso de la herramienta **efibootmgr** en Linux.
- Prácticas habituales: cambio de orden de arranque y recuperación del EFI tanto en Windows 11 como en Linux.
- Problemas frecuentes relacionados con las actualizaciones de Windows y el firmware.

---

## 2. Funcionamiento de EFI / UEFI

### 2.1. Componentes principales

Un sistema UEFI se compone de los siguientes elementos:

- **Firmware UEFI**: Sustituye al BIOS tradicional. Inicializa el hardware y lanza el gestor de arranque.
- **ESP (EFI System Partition)**: Partición especial en disco (formato FAT32) donde se almacenan los cargadores de arranque.
- **Boot Manager UEFI**: Módulo del firmware que gestiona las entradas de arranque almacenadas en NVRAM.
- **NVRAM**: Memoria no volátil donde se guardan las entradas EFI (orden de arranque, rutas a ejecutables EFI, etc.).

### 2.2. Proceso de arranque

1. El equipo se enciende y el firmware UEFI inicializa el hardware.
2. UEFI consulta la **NVRAM** para conocer el orden de arranque (BootOrder).
3. Se localiza la entrada EFI correspondiente (por ejemplo, Windows Boot Manager o GRUB).
4. Se ejecuta el archivo `.efi` almacenado en la ESP.
5. El gestor de arranque carga el sistema operativo.

### 2.3. Estructura típica de la ESP

La partición EFI suele montarse en Linux en `/boot/efi` y contiene una estructura similar a:

```
/EFI
 ├── Boot
 │   └── bootx64.efi
 ├── Microsoft
 │   └── Boot
 │       └── bootmgfw.efi
 └── ubuntu
     └── grubx64.efi
```

Cada sistema operativo registra su propia entrada en la NVRAM apuntando a su archivo `.efi`.

---

## 3. efibootmgr

### 3.1. ¿Qué es efibootmgr?

**efibootmgr** es una herramienta de Linux que permite **consultar y modificar las entradas de arranque UEFI** almacenadas en la NVRAM. Es fundamental para la administración del arranque en sistemas UEFI.

### 3.2. Requisitos

- Sistema arrancado en modo UEFI (no Legacy/CSM).
- Partición EFI correctamente montada.
- Permisos de superusuario.

### 3.3. Comandos básicos

Mostrar las entradas EFI:

```
sudo efibootmgr
```

Ejemplo de salida:

```
BootCurrent: 0001
BootOrder: 0001,0000
Boot0000* Windows Boot Manager
Boot0001* ubuntu
```

Significado:

- **BootCurrent**: entrada usada en el arranque actual.
- **BootOrder**: orden de prioridad.
- **BootXXXX**: entradas EFI registradas.

---

## 4. Práctica 1: Cambio del orden de arranque EFI

### Objetivo

Cambiar el orden de arranque para priorizar Linux o Windows.

### Procedimiento

1. Listar las entradas existentes:

```
sudo efibootmgr
```

2. Identificar los identificadores (por ejemplo, `0000` para Windows y `0001` para Linux).

3. Modificar el orden de arranque:

```
sudo efibootmgr -o 0001,0000
```

4. Reiniciar el sistema y comprobar el resultado.

### Observaciones

- El cambio es inmediato.
- Algunas actualizaciones de Windows pueden revertir este orden.

---

## 5. Práctica 2: Recuperación de un EFI eliminado en Windows 11

### Escenario

La entrada **Windows Boot Manager** ha sido eliminada de la NVRAM.

### Procedimiento

1. Arrancar con un **USB de instalación de Windows 11**.
2. Seleccionar **Reparar el equipo → Solucionar problemas → Símbolo del sistema**.
3. Identificar la partición EFI:

```
diskpart
list disk
select disk 0
list vol
```

4. Asignar una letra a la partición EFI:

```
select vol X
assign letter=S:
exit
```

5. Reconstruir el cargador EFI:

```
bcdboot C:\Windows /s S: /f UEFI
```

6. Reiniciar y comprobar que Windows aparece de nuevo en el firmware.

---

## 6. Práctica 3: Recuperación de un EFI eliminado en Linux

### Escenario

La entrada de GRUB ha desaparecido tras una actualización o instalación de Windows.

### Procedimiento

1. Arrancar con un **Live USB de Linux**.
2. Montar el sistema instalado:

```
sudo mount /dev/sdXn /mnt
sudo mount /dev/sdX1 /mnt/boot/efi
```

3. Entrar en chroot:

```
sudo chroot /mnt
```

4. Reinstalar GRUB en modo UEFI:

```
grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=ubuntu
update-grub
```

5. Verificar la entrada:

```
efibootmgr
```

6. Reiniciar el sistema.

---

## 7. Problemas con actualizaciones de Windows y el firmware

### 7.1. Actualización automática del firmware

Windows 11 puede:

- Actualizar el firmware UEFI.
- Modificar la NVRAM.
- Cambiar el orden de arranque.
- Marcar su gestor como prioritario.

### 7.2. Problemas habituales

- Desaparición de GRUB.
- Cambio automático del BootOrder.
- Activación de **Secure Boot** tras una actualización.
- Incompatibilidad con gestores de arranque antiguos.

### 7.3. Medidas preventivas

- Deshabilitar en Windows las **actualizaciones de firmware** desde Windows Update.
- Mantener copias de seguridad de la ESP.
- Conocer y usar `efibootmgr` para restaurar el orden.
- Verificar Secure Boot tras cada gran actualización.

---
