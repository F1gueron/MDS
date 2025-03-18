from selenium import webdriver
import re

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://r2-ctf-vulnerable.numa.host/")

links = driver.find_elements(By.TAG_NAME, "a")
visited = set()
hrefs = []

for link in links:
    if link.get_attribute("href").startswith("https://r2-ctf-vulnerable.numa.host/"):
        hrefs.append(link.get_attribute("href").rstrip("#"))

print("Empieza lo bueno")

count = 0

while hrefs:
    href = hrefs.pop(0)
    if href not in visited:
        driver.get(href)
        visited.add(href)
        links = driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            new_href = link.get_attribute("href").rstrip("#")
            if (new_href not in hrefs
                    and new_href.startswith("https://r2-ctf-vulnerable.numa.host/")
                    and new_href not in visited):
                hrefs.append(link.get_attribute("href"))
        try:
            #page_text = driver.page_source # Descomentar esto para buscar en el código fuente de cada página
            page_text = driver.find_element(By.CLASS_NAME, "article-post").text # Para buscar únicamente en el cuerpo del post
            count += len(re.findall(r"\bURJC\b", page_text)) # Para buscar sólo lo que tenga URJC o URJC.
            #count += len(re.findall(r"\w*URJC\w*[.,]*", page_text)) # Para buscar URJC y otras variaciones como asdasdURJC o URJCasdad
        except Exception as e:
            pass

print(f"\nNúmero total de apariciones de \"URJC\": {count}")

driver.quit()

# Usando la regex más amplia y el page_source = 280 -> INCORRECTO en ctfd
# Regex menos amplia y page_source = 273 -> INCORRECTO en ctfd
# Regex menos amplia y solo cuerpo del post = 271 -> no lo sabemos aun
# Regex más amplia y solo cuerpo del post = 278 -> no lo sabemos aun
