from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Constante URL
URL = "https://the-internet.herokuapp.com/upload"
driver.get(URL)

# Se interactua con el SO para seleccionar el fichero
file_path = os.path.abspath("H:\Prueba Desarrollador QA\Selenium.jpg")  #Validar que el archivo exista

# Cargar el archivo
upload_input = driver.find_element(By.ID, "file-upload")
upload_input.send_keys(file_path)

# Clic boton UPLOAD
driver.find_element(By.ID, "file-submit").click()


# Time para ver el resultado
time.sleep(3)

# Se valida el mensaje obtenido del h3
mensaje = driver.find_element(By.TAG_NAME, "h3").text
assert "File Uploaded!" in mensaje, "😒Error al subir el Archivo"

print("👍Archivo cargado exitosamente")

input("Enter para cerrar...")

# Cerrar navegador
driver.quit()
