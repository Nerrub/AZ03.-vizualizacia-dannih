import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

driver = webdriver.Chrome()
url = "https://www.divan.ru/category/divany-i-kresla"
driver.get(url)
time.sleep(5)
divans = driver.find_elements(By.CLASS_NAME, 'LlPhw')
parsed_data = []

for divan in divans:
    try:
        name = divan.find_element(By.CSS_SELECTOR, '.lsooF').text
        price_element = divan.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH[data-testid="price"]')
        current_price = price_element.text
        current_price = current_price.replace('руб.', '').replace(' ', '').replace('\n', '').strip()
        link = divan.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        parsed_data.append([name, int(current_price), link])
    except Exception as e:
        print(f'Произошла ошибка при парсинге: {e}')
        continue

driver.quit()

with open("divan.csv", 'w', newline='', encoding='utf-8-sig') as file:
    writer = csv.writer(file)
    writer.writerow(['Название', 'Цена', 'Ссылка на товар'])
    writer.writerows(parsed_data)


data = pd.read_csv("divan.csv")
average_price = data['Цена'].mean()
print(f'Средняя цена: {average_price:.2f} рублей')


plt.hist(data['Цена'], bins=20, edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (рубли)')
plt.ylabel('Количество')
plt.show()
