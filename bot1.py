from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random


# To initialize the Firefox browser
options = webdriver.FirefoxOptions()
options.add_argument("--start-maximized")  # Maximizar la ventana para una apariencia más natural
options.add_argument("--disable-infobars")  # Deshabilitar las barras de información
driver = webdriver.Firefox(options=options)

# To simulate mouse movements
def simulate_mouse_movement(element):
    actions = ActionChains(driver)
    actions.move_to_element(element)
    actions.perform()

# Open the website
url = "https://page.../"
driver.get(url)

# Wait more naturally
time.sleep(random.uniform(4, 6))

# Find the 'Log In' button and click it
inicio_sesion_btn = driver.find_element(By.CSS_SELECTOR, "#loginButton2")
simulate_mouse_movement(inicio_sesion_btn)  # Simular movimiento del mouse
inicio_sesion_btn.click()

# Wait mpre naturally
time.sleep(random.uniform(2, 4))

# Wait for the login form to load completely
wait = WebDriverWait(driver, 20)
email_input = wait.until(EC.visibility_of_element_located((By.ID, "email")))

# Find the email/username field and fill it in
email_input.send_keys("mail or username")

# Wait a little before to fill password field
time.sleep(random.uniform(1, 2))

# Find password field and fill it 
contrasenia_input = driver.find_element(By.NAME, "j_password")
contrasenia_input.send_keys("JRoman12")

# Wait before submitting the form
time.sleep(random.uniform(1, 2))

# Find the 'LOGIN' button and click on it
entrar_btn = driver.find_element(By.CSS_SELECTOR, "#btnEntrar button")
simulate_mouse_movement(entrar_btn)  # Simular movimiento del mouse
entrar_btn.click()

# Wait for the login to complete
time.sleep(5)

# To close the navegator
driver.quit()
