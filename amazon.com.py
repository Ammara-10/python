from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get('https://www.google.com/search?q=amazon&oq=amaz&gs_lcrp=EgZjaHJvbWUqGAgAEAAYQxiDARjjAhixAxjJAxiABBiKBTIYCAAQABhDGIMBGOMCGLEDGMkDGIAEGIoFMhsIARAuGEMYgwEYxwEYsQMYyQMY0QMYgAQYigUyBggCEEUYOTIGCAMQRRg7Mg8IBBAAGEMYsQMYgAQYigUyDQgFEAAYkgMYgAQYigUyDQgGEAAYkgMYgAQYigUyDQgHEAAYgwEYsQMYgAQyDQgIEAAYgwEYsQMYgAQyCggJEAAYsQMYgATSAQk0NTQ0ajBqMTWoAgCwAgA&sourceid=chrome&ie=UTF-8')
# time.sleep(5)
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="search"]')))
element=driver.find_element(By.XPATH,'//*[@id="search"]')
element.click()

time.sleep(5)
print(driver.title)
print(driver.current_url)
driver.close()
