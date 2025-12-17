# Protección de GRUB: control del arranque y gestión de Windows 11

## 1. Introducción

En esta sesión se aborda la **protección de GRUB**, explicando:

- Por qué es necesario protegerlo.
- Dónde y cómo se realizan los cambios.
- La gestión correcta de `os-prober`.
- La creación manual de entradas de **Windows 11** en `40_custom`.

---

## 2. Objetivos de la protección de GRUB

La protección de GRUB persigue:

- Impedir la edición de entradas de arranque sin autorización.
- Bloquear el acceso a la consola de GRUB.
- Permitir el arranque normal de los sistemas operativos.
- Mantener el control del menú de arranque en entornos multiarranque.

Es importante entender que **GRUB protege el proceso de arranque**, no la seguridad interna de los sistemas operativos.

---

## 3. Protección de GRUB con usuario y contraseña

### 3.1. Generación del hash de la contraseña

GRUB no almacena contraseñas en texto plano.

```
sudo grub-mkpasswd-pbkdf2
```

El comando devuelve un hash PBKDF2 que se usará en la configuración.

---

### 3.2. Definición del usuario administrador de GRUB

Editar el archivo:

```
sudo nano /etc/grub.d/40_custom
```

Añadir al inicio o al final:

```
set superusers="admin"
password_pbkdf2 admin grub.pbkdf2.sha512.10000....
```

Este usuario será el único autorizado para:

- Editar entradas (`e`).
- Acceder a la consola de GRUB.

---

## 4. Gestión de os-prober

### 4.1. Qué es os-prober

`os-prober` es una herramienta que detecta automáticamente otros sistemas operativos instalados (Windows, otros Linux) y genera sus entradas de arranque en GRUB.

### 4.2. Problemas de seguridad y control

En un GRUB protegido:

- `os-prober` genera entradas automáticamente.
- Las entradas pueden no incluir opciones de seguridad deseadas.
- Las configuraciones se pueden perder tras una actualización.

Por ello, **en entornos controlados se recomienda desactivar os-prober** y definir manualmente las entradas necesarias.

---

### 4.3. Desactivación correcta de os-prober

⚠️ Nunca se realiza desde `grub.cfg`, ya que es un archivo autogenerado.

Editar:

```
sudo nano /etc/default/grub
```

Añadir o modificar:

```
GRUB_DISABLE_OS_PROBER=true
```

Aplicar cambios:

```
sudo update-grub
```

### Resultado

- `os-prober` deja de ejecutarse.
- GRUB solo mostrará las entradas definidas manualmente.

---

## 5. Configuración de arranque Linux con --unrestricted

Las entradas de Linux se generan desde `/etc/grub.d/10_linux`.

Para permitir que Linux arranque sin pedir contraseña pero manteniendo la protección:

1. Editar el archivo:

```
sudo nano /etc/grub.d/10_linux
```

2. Localizar las dos líneas `menuentry` (asociadas a `echo $title` y `echo $os`).

3. Añadir `--unrestricted` entre `${CLASS}` y `$menuentry`:

```
menuentry "$title" ${CLASS} --unrestricted "$menuentry_id_option" "$id" {
```

Esto permite el arranque normal, pero bloquea la edición.

---

## 6. Añadir manualmente Windows 11 en 40_custom

Al desactivar `os-prober`, Windows no aparecerá automáticamente. Es necesario crear su entrada manualmente.

### 6.1. Por qué usar 40_custom

- Es un archivo diseñado para entradas personalizadas.
- No se sobrescribe en actualizaciones.
- Permite un control total del arranque.

---

### 6.2. Identificación de la partición EFI

Desde Linux:

```
lsblk -f
```

Se identifica la partición FAT32 montada en `/boot/efi`. Normalmente corresponde a `(hd0,gpt1)`.

---

### 6.3. Entrada correcta de Windows 11

Editar:

```
sudo nano /etc/grub.d/40_custom
```

Añadir:

```
menuentry "Windows 11" --unrestricted {
    insmod part_gpt
    insmod fat
    set root=(hd0,gpt1)
    chainloader /EFI/Microsoft/Boot/bootmgfw.efi
}
```

### Explicación

- `insmod part_gpt` y `insmod fat`: permiten acceder a la ESP.
- `set root`: indica a GRUB dónde buscar.
- `chainloader`: transfiere el control al Windows Boot Manager.

---

## 7. Aplicar la configuración

Siempre que se realicen cambios:

```
sudo update-grub
```

Reiniciar el sistema.

---

## 8. Comportamiento final esperado

Con esta configuración:

- El menú de GRUB se muestra siempre.
- Linux y Windows arrancan sin pedir contraseña.
- No se puede editar entradas ni acceder a la consola sin autenticación.
- El control del arranque está en manos del administrador.

---

## 9. Buenas prácticas profesionales

- Proteger GRUB con usuario y contraseña.
- Desactivar `os-prober` en entornos controlados.
- Definir manualmente las entradas críticas.
- Proteger BIOS/UEFI con contraseña.
- Usar Secure Boot y cifrado de disco cuando sea posible.

---
