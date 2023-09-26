from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random

# Inicializar el navegador Firefox
options = webdriver.FirefoxOptions()
options.add_argument("--start-maximized")  # Maximizar la ventana para una apariencia más natural
options.add_argument("--disable-infobars")  # Deshabilitar las barras de información
driver = webdriver.Firefox(options=options)

# Simular movimientos del mouse
def simulate_mouse_movement(element):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()

# Abrir el sitio web
url = "https://soysocio.bocajuniors.com.ar/"
driver.get(url)

# Esperar de manera más natural
time.sleep(random.uniform(4, 6))

# Encontrar el botón de "Iniciar Sesión" y hacer clic en él
inicio_sesion_btn = driver.find_element(By.CSS_SELECTOR, "#loginButton2")
simulate_mouse_movement(inicio_sesion_btn)  # Simular movimiento del mouse
inicio_sesion_btn.click()

# Esperar de manera más natural
time.sleep(random.uniform(2, 4))

# Esperar a que el formulario de inicio de sesión cargue completamente
wait = WebDriverWait(driver, 20)
email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))

# Encontrar el campo de email y llenarlo
email_input.send_keys("donofriomanuel1@gmail.com")

# Esperar un poco antes de llenar la contraseña
time.sleep(random.uniform(1, 2))

# Encontrar el campo de contraseña y llenarlo
contrasenia_input = driver.find_element(By.NAME, "j_password")
contrasenia_input.send_keys("JRoman12")

# Esperar antes de enviar el formulario
time.sleep(random.uniform(1, 2))

# Encontrar el botón de "ENTRAR" y hacer clic en él
entrar_btn = driver.find_element(By.CSS_SELECTOR, "#btnEntrar button")
simulate_mouse_movement(entrar_btn)  # Simular movimiento del mouse
entrar_btn.click()

# Esperar a que inicie sesión
time.sleep(5)

# Navegar a la sección de compras (ajusta el XPath según tu página)
compras_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Compras')]")
simulate_mouse_movement(compras_link)  # Simular movimiento del mouse
compras_link.click()

# Esperar a que la página de compras cargue (ajusta el tiempo según sea necesario)
time.sleep(5)

# Cerrar el navegador
driver.quit()
