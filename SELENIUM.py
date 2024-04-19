from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.google.com/search?q=acadamicaally&oq=acadamicaally&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQABgNGIAEMgkIAhAAGA0YgAQyDAgDEC4YDRjUAhiABDIJCAQQABgNGIAEMgkIBRAuGA0YgAQyCQgGEAAYDRiABDIJCAcQABgNGIAEMgkICBAAGA0YgATSAQoyMjMyMWowajE1qAIAsAIA&sourceid=chrome&ie=UTF-8')
print(driver.title)
print(driver.current_url)