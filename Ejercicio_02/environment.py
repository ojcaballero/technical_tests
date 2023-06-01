from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def setup():
    # Inicializamos una instancia de Chrome
    ## Se implementó una pequeña actualizacion al instanciar el driver de chrome
    driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()))
    driver.maximize_window()
    return driver

def close(driver):
    # Cerramos la instancia del navegador despues de cada prueba
    if (driver):
        driver.quit()