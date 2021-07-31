from twitterUserinfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', options=self.browserProfile)
        self.username = username
        self.password = password

    def Login(self):
        self.browser.get("https://twitter.com/login")
        time.sleep(2)

        usernameInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
        passwordInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
        
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)

        buttonSubmit = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div")
        buttonSubmit.click()
        time.sleep(2)

    def search(self, hashtag):
        searchInput = self.browser.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
        searchInput.send_keys(hashtag)
        time.sleep(2)
        
        searchInput.send_keys(Keys.ENTER)
        time.sleep(2)

        results = []

        list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]/div[1]")
        time.sleep(2)
        print("count: "+str(len(list)))

        for i in list:
            results.append(i.text)

        loop_counter = 0
        last_height = self.browser.execute_script("return document.documentElement.scrollHeight")
        while True:
            if loop_counter > 3:
                break
            self.browser.execute_script("window.scrollTo(0, document.documentElement.scrollHeight)")
            time.sleep(2)
            new_height = self.browser.execute_script("return document.documentElement.scrollHeight")
            
            if last_height == new_height:
                break
            last_height = new_height
            loop_counter+=1

            list = self.browser.find_elements_by_xpath("//div[@data-testid='tweet']/div[2]/div[2]/div[1]/div[1]")
            time.sleep(2)
            print("count: "+str(len(list)))

            for i in list:
                results.append(i.text)

        count = 1
        with open("tweets.txt", "w", encoding='UTF-8') as file:
            for item in results:
                file.write(f"{count} - {item}\n")
                count+=1

        # count = 1 
        # for item in results:
        #     print(f"{count}-{item}")
        #     count+=1
        #     print("******")


twitter = Twitter(username, password)
#login
twitter.Login()
#search 
twitter.search("python")