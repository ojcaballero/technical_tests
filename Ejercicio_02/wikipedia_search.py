from selenium.webdriver.common.by import By
from helpers import wait_and_find_element

def search_wikipedia(driver):
    wikipedia_result = wait_and_find_element(driver, By.CSS_SELECTOR, "a[href*='wikipedia']", 10)
    wikipedia_result.click()
