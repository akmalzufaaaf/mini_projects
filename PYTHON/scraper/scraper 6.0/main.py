# Accessing online retailer (titan22.com)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt

def get_driver(url):
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars') 
    options.add_argument('start-maximized') 
    options.add_argument('disable-dev-shm-usage') 
    options.add_argument('no-sandbox') 
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-feature=AutomationControlled') 
    
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    return driver

def main():
    driver = get_driver('https://titan22.com/account/login?return_url=%2Faccount')
    time.sleep(2)
    driver.find_element(by='xpath', value='/html/body/main/article/section/div/div[1]/form/div[1]/input').send_keys('codelearner360@gmail.com')
    time.sleep(2)
    driver.find_element(by='xpath', value='/html/body/main/article/section/div/div[1]/form/div[2]/input').send_keys('blablabla')
    time.sleep(2)
    driver.find_element(by='xpath',  value='/html/body/main/article/section/div/div[1]/form/button').click()
    time.sleep(2)
    driver.find_element(by='xpath', value='/html/body/footer/div/section/div/div[1]/div[1]/div[1]/nav/ul/li[1]/a').click()
    time.sleep(5)
    print(driver.current_url())
    
main()
