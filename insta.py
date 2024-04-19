import driver as driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://www.instagram.com/accounts/login/")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')))
username_ele =driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
print(username_ele.is_displayed())
print(username_ele.is_enabled())
username_ele.send_keys('ammara.royal1@gmail.com')
password_ele = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
print(username_ele.is_displayed())
print(username_ele.is_enabled())
password_ele.send_keys('appsamle10')
login_button = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div')
login_button.click()
#wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mount_0_0_Nj"]/div/div/di//*[@id="mount_0_0_Nj"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/buttonv[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')))
#safe_info= driver.find_element(By.XPATH,'//*[@id="mount_0_0_Nj"]/div/div/di//*[@id="mount_0_0_Nj"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/buttonv[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')
#safe_info.click()
driver.get('https://www.instagram.com/direct/inbox/')
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_ly"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div/div/span/img')))

chat_box=driver.find_element(By.XPATH,'//*[@id="mount_0_0_ly"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div/div/span/img').click()
wait.until(EC.presence_of_element_located((By.XPATH,'//*[@id="mount_0_0_ly"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p')))
text_input=driver.find_element(By.XPATH,'//*[@id="mount_0_0_ly"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]/p').click()
text_input.send_keys('HELLO,this is me ammara!')
send_button = driver.find_element(By.XPATH,'//*[@id="mount_0_0_ly"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div/div/div[2]/div/div/div[3]').click()

driver.quit()
