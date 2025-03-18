from selenium import webdriver
import re
import time

from selenium.webdriver.common.by import By

driver = webdriver.Firefox() # Con firefox hay que meter un try-except en la linea 31, con chrome funciona mejor
driver.get("https://r2-ctf-vulnerable.numa.host/")

links = driver.find_elements(By.TAG_NAME, "a")
visited = set()
hrefs = []

for link in links:
    if link.get_attribute("href").startswith("https://r2-ctf-vulnerable.numa.host/"):
        hrefs.append(link.get_attribute("href"))

print("Empieza lo bueno")

count_re = 0
count_normal = 0

while hrefs:
    href = hrefs.pop(0)
    if href not in visited:
        driver.get(href)

        visited.add(href)
        links = driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            try:
                if (link.get_attribute("href") not in hrefs
                        and link.get_attribute("href").startswith("https://r2-ctf-vulnerable.numa.host/")
                        and link.get_attribute("href") not in visited):
                    hrefs.append(link.get_attribute("href"))
            except:
                pass
        try:
            #page_text = driver.find_element(By.CLASS_NAME, "article-post").text
            page_text = driver.find_element(By.TAG_NAME, "html").text
            count_normal += page_text.count("URJC")
            count_re += len(re.findall(r"\bURJC\b", page_text))
            print(re.findall(r"\bURJC\b", page_text))
            #count_re += len(re.findall(r"\w*URJC[.,!?]*\w*[.,!?]*", page_text))
        except Exception as e:
            pass



print("\nNúmero total de apariciones de \"URJC\": {}".format(count_re))
print("\nNúmero total de apariciones de \"URJC\": {}".format(count_normal))

driver.quit()
