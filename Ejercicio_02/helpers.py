from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_and_find_element(driver, by, locator, wait):
    wait = WebDriverWait(driver, wait)
    return wait.until(EC.presence_of_element_located((by, locator)))
