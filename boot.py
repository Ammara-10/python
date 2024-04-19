import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://docs.python.org/3/py-modindex.html")
elements = driver.find_elements(By.XPATH, '//code')
file = open("mytext.txt", 'a')

for element in elements:
    text = element.text
    print(text)
    file.write(text + '\n')

file.close()
driver.quit()

