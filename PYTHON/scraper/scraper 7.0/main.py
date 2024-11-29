# automate download stock data from finance.yahoo.com

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
    ticker = input("Enter Company Ticker (Ex. AAPL, MSFT, etc): ")
    driver = get_driver('https://finance.yahoo.com/')
    time.sleep(2)
    driver.find_element(by='xpath', value='//*[@id="ybar-sbq"]').send_keys(ticker)
    time.sleep(2)
    print(driver.current_url)


main()
