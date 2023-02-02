# Step 1 is to download your desired driver. I used ChromeDriver for this script
import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome('Your Local Web Driver File Path')

username = 'Insert Your Twitter Username or Email for Login'
password = 'Insert Twitter Password, encryption recommended'

# gather xpaths needed for login
sign_in = "/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span"
username_box = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input"
next_button = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div"
password_box = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input"
login_button = "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div"

def log_into_twitter(username, password):
    driver.get('twitter.com')
    time.sleep(5)
    driver.find_element_by_xpath(sign_in).click()
    time.sleep(5)
    driver.find_element_by_xpath(username_box).click()
    time.sleep(5)
    driver.send_keys(username)
    time.sleep(5)
    driver.find_element_by_xpath(next_button).click()
    time.sleep(5)
    driver.find_element_by_xpath(password_box).click()
    time.sleep(5)
    driver.send_keys(password)
    time.sleep(5)
    driver.find_element_by_xpath(login_button).click()
    # successful login



log_into_twitter(username, password)
