Para estimar el TDP de tu máquina en Linux utilizando el programa **stress**, puedes seguir estos pasos. Este proceso implicará instalar herramientas para someter a tu CPU a una carga alta, monitorear su consumo energético, y hacer los cálculos necesarios.

---

### **Paso 1: Instala el programa stress y herramientas de monitoreo**
1. **Instala stress** para generar la carga en tu CPU:
   ```bash
   sudo apt update
   sudo apt install stress
   ```
2. **Instala lm-sensors y powertop** para monitorear temperatura y consumo energético:
   ```bash
   sudo apt install lm-sensors powertop
   ```

---

### **Paso 2: Configura el monitoreo de sensores**
1. Configura **lm-sensors**:
   ```bash
   sudo sensors-detect
   ```
   - Responde "yes" a las preguntas para detectar todos los sensores disponibles.
2. Verifica los sensores disponibles:
   ```bash
   sensors
   ```
   - Esto mostrará la temperatura de la CPU, voltaje y otros datos útiles.

---

### **Paso 3: Ejecuta el test de carga**
1. **Genera una carga completa en la CPU con stress**:
   ```bash
   stress --cpu $(nproc) --timeout 300
   ```
   - Este comando utiliza todos los núcleos disponibles (`$(nproc)`) durante 300 segundos (5 minutos).

2. **Monitorea el consumo energético con powertop**:
   - Inicia powertop:
     ```bash
     sudo powertop
     ```
   - Observa el consumo energético en la columna "Power Estimate" mientras ejecutas stress. Toma nota del valor máximo durante la prueba.

---

### **Paso 4: Monitorea el voltaje y la corriente (opcional)**
Si tu hardware lo permite, puedes utilizar herramientas adicionales para obtener el voltaje (V) y la corriente (I) de la CPU. Esto te permitirá calcular manualmente el TDP:

1. Instala y ejecuta i7z para procesadores Intel:
   ```bash
   sudo apt install i7z
   sudo i7z
   ```

2. Observa el voltaje en tiempo real durante la carga.

---

### **Paso 5: Calcula el TDP**
Si obtuviste valores de voltaje (V) y corriente (I), usa la fórmula:

**TDP aprox V x I x {Número de núcleos activos}**


Si no tienes corriente (I), utiliza el consumo total de energía registrado por **powertop** como un proxy del TDP.

---

### **Resultados esperados**
1. **TDP estimado:** El consumo máximo observado durante el test de estrés debe acercarse al valor TDP oficial de tu CPU.
2. **Ajustes:** Si encuentras discrepancias, podrían deberse a:
   - Configuraciones de *Boost Clock* que aumentan temporalmente el consumo.
   - Limitaciones térmicas o de energía.

Este proceso te dará una buena estimación del TDP en tu máquina utilizando Linux y herramientas de código abierto.