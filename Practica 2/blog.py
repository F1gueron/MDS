from selenium import webdriver
import re
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://r2-ctf-vulnerable.numa.host/")

links = driver.find_elements(By.TAG_NAME, "a")
visited = set()
hrefs = []

for link in links:
    if link.get_attribute("href").startswith("https://r2-ctf-vulnerable.numa.host/"):
        hrefs.append(link.get_attribute("href"))

print("Empieza lo bueno")

count_re = 0

while hrefs:
    href = hrefs.pop(0)
    if href not in visited:
        driver.get(href)
        visited.add(href)
        links = driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            if (link.get_attribute("href") not in hrefs
                    and link.get_attribute("href").startswith("https://r2-ctf-vulnerable.numa.host/")
                    and link.get_attribute("href") not in visited):
                hrefs.append(link.get_attribute("href"))
        try:
            page_text = driver.page_source
            count_re += len(re.findall(r"\bURJC\b", page_text))
        except Exception as e:
            pass

print("\nNúmero total de apariciones de \"URJC\": {}".format(count_re))

driver.quit()
