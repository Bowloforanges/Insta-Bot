from selenium import webdriver
from time import sleep

from AccountData import username, password

class InstaBot():

    def __init__(self):

        self.driver = webdriver.Chrome()

    def login(self):

        self.driver.get("https://www.instagram.com/")
        sleep(2)

        loginLink = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
        loginLink.click()
        sleep(1)

        usernameField = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input')
        passwordField = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')

        usernameField.send_keys(username)
        passwordField.send_keys(password)

        loginBtn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
        loginBtn.click()
        sleep(5)

        notNowBtn = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[3]/button[2]')
        notNowBtn.click()
        sleep(2)

        try:

            loadNewBtn = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div[2]/div/button/div')
            loadNewBtn.click()
            sleep(0.5)
        
        except Exception:

            print("nothing new!")
