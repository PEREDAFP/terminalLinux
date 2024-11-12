
### Sesión : Monitorizar Procesos en Windows con PowerShell

#### Objetivo:
Aprender a monitorizar procesos en Windows utilizando PowerShell.

#### Contenido:
1. **Listar todos los procesos en ejecución:**
   ```powershell
   Get-Process
   ```

2. **Filtrar procesos por nombre:**
   ```powershell
   Get-Process -Name "notepad"
   ```

3. **Obtener información detallada de un proceso:**
   ```powershell
   Get-Process -Name "notepad" | Format-List *
   ```

4. **Monitorizar el uso de CPU y memoria de un proceso:**
   ```powershell
   Get-Process -Name "notepad" | Select-Object Name, CPU, PM, WS
   ```

### Sesión 2: Parar Procesos en Windows con PowerShell

#### Objetivo:
Aprender a parar procesos en Windows utilizando PowerShell.

#### Contenido:
1. **Parar un proceso por nombre:**
   ```powershell
   Stop-Process -Name "notepad"
   ```

2. **Parar un proceso por ID:**
   ```powershell
   Stop-Process -Id 1234
   ```

3. **Parar todos los procesos con un nombre específico:**
   ```powershell
   Get-Process -Name "notepad" | Stop-Process
   ```

### Sesión 3: Lanzar Procesos en Segundo Plano en Windows con PowerShell

#### Objetivo:
Aprender a lanzar procesos en segundo plano en Windows utilizando PowerShell.

#### Contenido:
1. **Lanzar un proceso en segundo plano:**
   ```powershell
   Start-Process -FilePath "notepad.exe" -NoNewWindow
   ```

2. **Lanzar un proceso en segundo plano y redirigir la salida:**
   ```powershell
   Start-Process -FilePath "ping" -ArgumentList "localhost" -NoNewWindow -RedirectStandardOutput "output.txt" -RedirectStandardError "error.txt"
   ```

3. **Lanzar un proceso en segundo plano y esperar a que termine:**
   ```powershell
   $process = Start-Process -FilePath "ping" -ArgumentList "localhost" -NoNewWindow -PassThru
   $process.WaitForExit()
   ```

### Sesión 4: Ejecutar Procesos en Tiempo Diferido en Windows con PowerShell

#### Objetivo:
Aprender a ejecutar procesos en tiempo diferido en Windows utilizando PowerShell, similar a `at` o `crontab` en Linux.

#### Contenido:
1. **Ejecutar un proceso en un tiempo específico:**
   ```powershell
   $action = { Start-Process -FilePath "notepad.exe" }
   $trigger = New-JobTrigger -At "2023-10-01T14:30:00"
   Register-ScheduledJob -Name "OpenNotepad" -Trigger $trigger -ScriptBlock $action
   ```

2. **Ejecutar un proceso de forma recurrente (diaria, semanal, etc.):**
   ```powershell
   $action = { Start-Process -FilePath "notepad.exe" }
   $trigger = New-JobTrigger -Daily -At "14:30"
   Register-ScheduledJob -Name "OpenNotepadDaily" -Trigger $trigger -ScriptBlock $action
   ```

3. **Ejecutar un proceso en un intervalo de tiempo específico:**
   ```powershell
   $action = { Start-Process -FilePath "notepad.exe" }
   $trigger = New-JobTrigger -Once -At "2023-10-01T14:30:00" -RepetitionInterval (New-TimeSpan -Minutes 30) -RepetitionDuration ([TimeSpan]::MaxValue)
   Register-ScheduledJob -Name "OpenNotepadInterval" -Trigger $trigger -ScriptBlock $action
   ```
