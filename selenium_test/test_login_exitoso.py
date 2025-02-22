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

##Se definen constantes para las URL de Login y la esperada despues del Login
URL = "https://the-internet.herokuapp.com/login"
URL_ESPERADA = "https://the-internet.herokuapp.com/secure"

'''Función credenciales busqueda de elementos de la WEB ID'''
def test_login_exitoso():
    driver.get(URL)
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!" + Keys.RETURN)



##Confirme que el usuario es redirigido correctamente después de un inicio de sesión exitoso
    WebDriverWait(driver, 5).until(EC.url_to_be(URL_ESPERADA))
    assert driver.current_url == URL_ESPERADA, "💣 Error en la redirección"
    print("🏁 Redirección correcta, Login esperado OK.")

time.sleep(3)

test_login_exitoso()

input("Enter para cerrar...")
driver.quit()
