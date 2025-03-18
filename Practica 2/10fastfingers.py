from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://192.168.59.128/")

text_input = driver.find_element(By.ID, 'textInput')

for i in range(1, 21):
    word = driver.find_element(By.ID, f"word_{i}").text
    text_input.send_keys(word + " ")


time.sleep(30) # Sleep para ver la flag

driver.quit()

# Flag => URJC{f1ng3rs_tr41n3d!}
