import re
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

## Primer paso

# Inicializamos una instancia de Chrome
driver.maximize_window()
driver.get("https://www.google.com/")

# Buscamos el text area donde escribiremos la palabra que se va a buscar
search_area = driver.find_element(By.CSS_SELECTOR, "[name='q'][type='search']")
search_area.send_keys("automatizacion" + Keys.ENTER)

## Segundo paso: Buscar el link de la Wikipedia resultante

wikipedia_result = driver.find_element(By.CSS_SELECTOR, "a[href*='wikipedia']")
wikipedia_result.click()

## Tercer paso: Comprobar en qué año se hizo el primer proceso automático
article = driver.find_element(By.XPATH, "//*[@id='mw-content-text']/div[1]/p[11]")
article_text = article.text

# Patrón para encontrar cuatro dígitos consecutivos
pattern = r"\b\d{4}\b"  
year = re.search(pattern, article_text)
print("Year: ", year.group())

## Cuarto paso: Realizar un screenshot de la página de la Wikipedia (el cual se guardará en la misma ruta del script)
driver.save_screenshot("Evidencia.png")

driver.quit()