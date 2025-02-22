# 🚀 PRUEBA TÉCNICA QA

## 📌 Descripción
Este proyecto contiene pruebas automatizadas con **Selenium en Python** para validación de autenticación y carga de archivos, junto con una prueba de carga utilizando **Locust** para evaluar el rendimiento del sitio web [The Internet Herokuapp](https://the-internet.herokuapp.com/).

## 📂 Estructura del Proyecto
```
proyecto/
│-- selenium_test/                  # Incluye los casos de prueba automatizados con Selenium
│   ├── test_file_upload.py          # Cargar archivos
│   ├── test_login_exitoso.py        # Login exitoso y fallido
│   ├── test_login_fallido.py        # Login con diferentes credenciales
│-- performance_test/                # Contiene el script de pruebas de carga con Locust
│   ├── stress_test.py              # Simulación de 200 usuarios concurrentes
│-- requirements.txt              # Dependencias del proyecto
│-- README.md                     # Documentación del proyecto
```

## 📦 Instalación

Clona este repositorio en tu máquina local:
```sh
git clone https://github.com/Maicol1315/Prueba-Tecnica-QA.git
cd tu_repositorio
```

Instala las dependencias con:
```sh
pip install -r requirements.txt
```

## 🖥️ Ejecución de Pruebas con Selenium

Para ejecutar los casos de prueba automatizados con **Selenium**, usa:
```sh
pytest tests/test_login_exitoso.py
pytest tests/test_login_fallido.py
pytest tests/test_file_upload.py
```

## 🌐 Ejecución de Pruebas de Carga con Locust

Ejecuta Locust con el siguiente comando:
```sh
locust -f stress_test.py --host=https://the-internet.herokuapp.com --users 200 --spawn-rate 10 --run-time 60s
```

🔹 **Explicación de los parámetros:**
- `-u 200` → 200 usuarios concurrentes
- `-r 10` → 10 usuarios nuevos por segundo
- `-t 60s` → La prueba durará 60 segundos

Luego, abre el navegador en `http://localhost:8089` para monitorear la prueba en tiempo real.

📊 Métricas a Medir

- Tiempo de respuesta promedio: Tiempo medio que tardan las solicitudes en completarse.
- Tasa de éxito y fallos: Cantidad de solicitudes exitosas y fallidas durante la prueba.
- Rendimiento bajo carga: Cómo responde el sitio con 200 usuarios concurrentes.

## 🛠️ Tecnologías Utilizadas
- **Selenium** (para pruebas funcionales)
- **Locust** (para pruebas de carga)
- **Python** (como lenguaje de programación).

📖 Fuentes de Información y Apoyo
Este proyecto fue desarrollado con apoyo de la documentación oficial de Selenium y Locust, así como asistencia de IA.

## 📜 Autor
🚀 MAICOL ENRIQUE PEÑA CUBILLOS, para la prueba como aspirante al cargo de QA en ADRES. (Toda retroalimentación es Bienvenida)

