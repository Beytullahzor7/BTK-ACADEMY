import selenium
from githubUserinfo import username, password
from selenium import webdriver
import time

class Github:
    def __init__(self, username, password):

        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []
    
    def signIn(self):

        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element_by_xpath("//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element_by_xpath("//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/input[12]").click()

    def getFollowers(self):

        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)

        items = self.browser.find_elements_by_css_selector(".d-table.table-fixed")
        for item in items:
            self.followers.append(item.find_element_by_css_selector(".Link--secondary.pl-1").text)


github = Github(username, password)
github.signIn()
github.getFollowers()
print(github.followers)



