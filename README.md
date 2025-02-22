# 🚀 PRUEBA TÉCNICA QA

## 📌 Descripción
Este proyecto busca resolver la prueba técnica para QA. El repositorio incluye las automatizaciones de los casos de prueba de 1. autenticación (Form Authentication) y 2. carga de archivos (b.	File Upload), realizadas Selenium en Python, así como una prueba de estrés con los diferentes escenarios utilizando Locust.

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

Si se requiere instalar webdriver-manager
```sh
pip install webdriver-manager
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

🖥️ Escenarios de la prueba de Carga
  - i.	Usuarios Simulados: 200 usuarios concurrentes
  - ii.	Comportamiento del Usuario:
    - 1.	Acceder a la página de inicio
    - 2.	Acceder a la sección Form Authentication y realice un intento de inicio de sesión (usuario: tomsmith, contraseña: SuperSecretPassword!)
    - 3.	Acceder a la sección File Download y realice una descarga de archivo


📊 Métricas a Medir

- Tiempo de respuesta promedio: Tiempo medio que tardan las solicitudes en completarse.
- Tasa de éxito y fallos: Cantidad de solicitudes exitosas y fallidas durante la prueba.
- Rendimiento bajo carga: Cómo responde el sitio con 200 usuarios concurrentes.

## 🛠️ Tecnologías Utilizadas
- **Selenium** (para pruebas funcionales)
- **Locust** (para pruebas de carga)
- **Python** (como lenguaje de programación).

## 📖 Fuentes de Información y Apoyo
- Este proyecto fue desarrollado con apoyo de la documentación oficial de Selenium y Locust, así como asistencia de IA.

## 📜 Autor
🚀 MAICOL ENRIQUE PEÑA CUBILLOS, para la prueba como aspirante al cargo de QA en ADRES. (Toda retroalimentación es Bienvenida)

##

¡Estaré muy atento! 🎯

