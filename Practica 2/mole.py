from selenium import webdriver
import re
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://192.168.59.128/") # Esto se puede poner creo como file://tal/tal/index.html pero no lo tengo claro


while int(driver.find_element(By.ID, 'score').text) <= 10000:
    try:
        mole = driver.find_element(By.CLASS_NAME, 'mole')
        mole.click()
    except:
        pass

time.sleep(10)

driver.quit()
