# 📚 Compresión de Videos .MP4 sin perder calidad

Este script en Python permite comprimir videos en formato MP4 utilizando el códec H.265 (HEVC) para reducir el tamaño de los archivos sin comprometer significativamente la calidad del video. La herramienta está diseñada para manejar múltiples archivos dentro de un directorio, incluyendo subcarpetas, y ofrece un informe detallado del ahorro de espacio obtenido tras la compresión.

---

## ⚙️ Requisitos Previos

1. **Python 3:** Asegúrate de tener Python 3 instalado en tu sistema.
2. **FFmpeg:** Descarga e instala FFmpeg desde [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
   - Agrega FFmpeg al PATH o define la variable `FFMPEG_PATH` en el script con la ruta adecuada.

### 🏁 Cómo Configurar FFmpeg en Windows
1. Descarga el archivo comprimido desde el sitio web oficial.
2. Extrae el contenido y copia la ruta del ejecutable `ffmpeg.exe`.
3. Agrega esta ruta al PATH del sistema o define la variable `FFMPEG_PATH` en el script.

---

## 🚀 Cómo Usar el Script

1. Abre una terminal (CMD, PowerShell o terminal en Mac/Linux).
2. Ejecuta el script con el siguiente comando:
   ```bash
   python nombre_del_script.py
   ```
3. **Ingresa el directorio** donde están los archivos de video.
4. Revisa la **información preliminar**:
   - Cantidad de archivos a procesar 🎥
   - Tamaño total de archivos originales 📦
   - Estimación de tamaño comprimido 📉
   - Tiempo estimado de operación ⏱️
5. Confirma si deseas continuar con la compresión (`Y/N`).
6. Decide si deseas guardar los archivos en una nueva carpeta (`Y/N`). Si eliges `Y`, proporciona la ruta donde se creará una subcarpeta llamada `COMPRESSED`.

---

## 🛠️ Funcionalidades

- **Compresión Eficiente:** Utiliza el códec H.265 (HEVC) para una compresión eficiente.
- **Bitrate Ajustado:** Configuración de 322855 bps y 24 fps.
- **Soporte para Subdirectorios:** Procesa todos los archivos `.mp4` dentro de carpetas y subcarpetas.
- **Conservación de Archivos Originales:** No elimina ni modifica los archivos originales.
- **Log Detallado:** Genera un archivo de registro con información detallada de las compresiones realizadas.
- **Resumen Informativo:** Muestra estadísticas de ahorro de espacio.
- **Barra de Progreso:** Indicadores visuales para el progreso de la conversión.

---

## 📄 Ejemplo de Flujo

```bash
Ingresa el directorio donde están los archivos de video: C:\Videos
Cantidad de archivos a procesar: 5
Tamaño total de archivos originales: 1200.00 MB
Estimación de tamaño total comprimido: 780.00 MB
Tiempo estimado de operación: 10.00 minutos
¿Deseas iniciar la compresión? (Y/N): Y
¿Deseas guardar los videos en una nueva carpeta? (Y/N): Y
Ingresa el directorio donde deseas guardar los videos: D:\VideosComprimidos
Procesando archivos: 100% |████████████████████| 5/5 [00:45<00:00, 9.00s/archivo]

=== Resumen de Compresión ===
Archivos leídos: 5
Archivos comprimidos: 5
Tamaño total original: 1200.00 MB
Tamaño total comprimido: 780.00 MB
Has ahorrado 420.00 MB de espacio al comprimir tus videos.
Log generado en: video_compression_log_20250207_123938.txt
```

---

## 📋 Detalles Técnicos

- **FFmpeg Comando:**
  ```bash
  ffmpeg -i input.mp4 -c:v libx265 -crf 28 -preset medium -b:v 322855 -r 24 -c:a aac -b:a 128k output.mp4
  ```
- **Compresión:**
  - Codec de Video: H.265 (HEVC)
  - Calidad CRF: 28 (equilibrio entre calidad y tamaño)
  - Bitrate: 322855 bps
  - FPS: 24
  - Codec de Audio: AAC
  - Bitrate de Audio: 128 kbps

---

## 📝 Estructura del Log
El archivo de log generado tiene el siguiente formato:

```
=== Log de Compresion de Videos ===
Archivo comprimido: C:\Videos\video1.mp4 -> D:\VideosComprimidos\COMPRESSED\video1_Lite.mp4 (150.00 MB)
Archivo comprimido: C:\Videos\video2.mp4 -> D:\VideosComprimidos\COMPRESSED\video2_Lite.mp4 (170.00 MB)
...
=== Resumen ===
Archivos leídos: 5
Archivos comprimidos: 5
Tamaño total original: 1200.00 MB
Tamaño total comprimido: 780.00 MB
Espacio ahorrado: 420.00 MB
```

---

## 🔧 Posibles Errores y Soluciones

1. **FFmpeg no encontrado:**
   - Verifica que `FFMPEG_PATH` apunte correctamente al ejecutable de FFmpeg.
   - Asegúrate de que FFmpeg esté agregado al PATH del sistema.

2. **Permisos Denegados:**
   - Ejecuta la terminal como administrador.

3. **Archivos no encontrados:**
   - Verifica que el directorio ingresado contenga archivos `.mp4`.

4. **Error durante la compresión:**
   - Revisa el archivo de log para identificar el archivo problemático.

---

## 💡 Consejos

- **Optimiza el Bitrate:** Si deseas una compresión aún mayor, ajusta el valor del CRF a un número más alto (30 o superior).
- **Organiza los Archivos:** Mantén los archivos comprimidos en carpetas separadas para una mejor organización.
- **Mantén una Copia de Seguridad:** Asegúrate de conservar una copia de tus archivos originales.

---

## 🌟 ¡Gracias por Usar el Script! 🚀

Si tienes alguna pregunta o sugerencia, no dudes en compartirla. ¡Espero que ahorres mucho espacio y optimices tus videos! 🎥💾
