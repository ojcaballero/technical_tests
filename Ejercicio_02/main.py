from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from google_search import search_google
from wikipedia_search import search_wikipedia
from wiki_info import get_year_from_text
from screenshot import take_screenshot
from helpers import wait_and_find_element
import environment

try:
    # Configuración del entorno de prueba: Inicializamos una instancia de Chrome
    driver = environment.setup()

    # Primer paso: Buscar en Google la palabra "automatización"
    search_google(driver, "automatización")

    # Segundo paso: Buscar el link de la Wikipedia resultante
    search_wikipedia(driver)

    # Tercer paso: Comprobar en qué año se hizo el primer proceso automático
    article_text = wait_and_find_element(driver, By.XPATH, "//*[@id='mw-content-text']/div[1]/p[11]", 10).text
    year = get_year_from_text(article_text)
    print("Año del primer proceso automatizado: ", year)

    # Cuarto paso: Realizar un screenshot de la página de la Wikipedia (el cual se guardará en la misma ruta del script)
    take_screenshot(driver, "Evidencia.png")
except WebDriverException as e:
    print("Ocurrió un problema al instanciar el driver de Chrome: ", e)
except Exception as e:
    print("Ocurrió el siguiente problema: ", e)
finally:
    # Limpieza del entorno de prueba: Nos aseguramos de cerrar la instancia de Chrome (si existe)
    if "driver" in locals():
        environment.close(driver)
