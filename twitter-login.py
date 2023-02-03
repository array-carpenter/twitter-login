# Step 1 is to download your desired driver. I used ChromeDriver for this script
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# gather xpaths needed for login
sign_in = "/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span"
username_box = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"
next_button = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div"
password_box = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
login_button = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div"


class twitter_login:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('Your Local Web Driver File Path')

    def log_into_twitter(self):
        self.driver.get('https://twitter.com/')
        time.sleep(5)
        self.driver.find_element_by_xpath(sign_in).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(username_box).click()
        time.sleep(5)
        self.driver.send_keys(self.username)
        time.sleep(5)
        self.driver.find_element_by_xpath(next_button).click()
        time.sleep(5)
        self.driver.find_element_by_xpath(password_box).click()
        time.sleep(5)
        self.driver.send_keys(self.password)
        time.sleep(5)
        self.driver.send_keys(Keys.RETURN)
        # successful login
        time.sleep(10)
    
    def close_window(self):
        self.driver.quit()



login = twitter_login("insert usernamw", "insert password")
login.login()
login.close()
