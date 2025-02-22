from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

URL = "https://the-internet.herokuapp.com/login"

def test_login_fallido():
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("usuario_invalido")
    driver.find_element(By.ID, "password").send_keys("clave_invalida" + Keys.RETURN)
##Se valida el mensaje del selector .flash.error se pasa el texto
    mensaje = WebDriverWait(driver, 5).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, ".flash.error"))).text
    assert "Your username is invalid!" in mensaje or "Your password is invalid!" in mensaje, "Mensaje incorrecto"
    print("🤓 No se puede iniciar Sesión: Validación Correcta.")

time.sleep(3)

test_login_fallido()


input("Enter para cerrar...")

driver.quit()
