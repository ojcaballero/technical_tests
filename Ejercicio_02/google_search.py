from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from helpers import wait_and_find_element

def search_google(driver, keyword):
    driver.get("https://www.google.com/")
    search_area = wait_and_find_element(driver, By.CSS_SELECTOR, "[name='q'][type='search']", 10)
    search_area.send_keys(keyword + Keys.ENTER)
