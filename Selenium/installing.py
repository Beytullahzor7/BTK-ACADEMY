from selenium import webdriver

driver = webdriver.Chrome()
#driver = webdriver.Firefox()

url = "https://github.com"

driver.get(url)
