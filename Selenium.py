from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt
import time


service = Service()  
options = webdriver.ChromeOptions()
options.add_argument("--headless")  
driver = webdriver.Chrome(service=service, options=options)


url = "https://www.worldometers.info/world-population/population-by-country/"
driver.get(url)


time.sleep(3)


table = driver.find_element(By.TAG_NAME, "table")
rows = table.find_elements(By.TAG_NAME, "tr")


data = []
for row in rows[1:]:  
    cols = row.find_elements(By.TAG_NAME, "td")
    if len(cols) > 1:
        country = cols[1].text
        population = cols[2].text.replace(",", "")
        try:
            population = int(population)
        except:
            population = 0
        data.append((country, population))

driver.quit()


frame = pd.DataFrame(data, columns=["Country", "Population"])
frame.to_excel("C:/Users/Downloads/population.xlsx", index=False)                #Path must be changed to your own Directory


top10 = frame.sort_values(by="População", ascending=False).head(10)


plt.figure(figsize=(10, 6))
plt.barh(top10["Country"], top10["Population"], color='skyblue')
plt.xlabel("Population")
plt.title("Top 10 Most Populated Countries in the World")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()
