# Step 1 is to download your desired driver. I used ChromeDriver for this script
import selenium
from selenium import webdriver
import time

driver = webdriver.Chrome('Your Local Web Driver File Path')

username = 'Insert Your Twitter Username or Email for Login'
password = 'Insert Twitter Password, encryption recommended'

def log_into_twitter(username, password):
    driver.get('twitter.com')
    time.sleep(5)
    # click sign in button
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div/div[1]/div/div/div/div[2]/div[2]/div/div/div[1]/a/div/span/span").click()
    # click username box
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input").click()
    # enter username
    driver.send_keys(username)
    time.sleep(5)
    # click next
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div").click()
    # click password box
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").click()
    time.sleep(5)
    # enter password
    driver.send_keys(password)
    time.sleep(5)
    #click login
    driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div").click()
    # successful login



log_into_twitter(username, password)
