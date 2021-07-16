from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Firefox()

url = "http://github.com"
driver.get(url)

# searchInput = driver.find_element_by_name("q")
searchInput = driver.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/div[1]/div/div/form/label/input[1]")
time.sleep(1)

searchInput.send_keys("python") #aramak istedigimiz kelimeyi belirttik
time.sleep(2)

searchInput.send_keys(Keys.ENTER) #input üzerinden enter tusuna basılır
time.sleep(4)

# result = driver.page_source

result = driver.find_elements_by_css_selector(".repo-list-item div a")

for element in result:
    print(element.text)

driver.close()