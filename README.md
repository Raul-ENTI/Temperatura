# ☁️ Consulta el Tiempo en unas de estas Ciudades

Este sencillo script en Python te permite conocer el tiempo actual (temperatura, velocidad del viento y humedad relativa) en una de estas tres ciudades españolas:

-  **Barcelona**
-  **Madrid**
-  **Palencia**

## ¿Cómo funciona?

1. El usuario elige una ciudad introduciendo un número.
2. El programa hace una solicitud a la **API de Open-Meteo** según las coordenadas de la ciudad seleccionada.
3. Se muestra la temperatura actual, la velocidad del viento y la humedad relativa.

## Tecnologías usadas

- `Python`
  - `urllib` para acceder a la API
  - `json` para procesar los datos de la respuesta
