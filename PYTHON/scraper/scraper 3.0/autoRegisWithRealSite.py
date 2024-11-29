from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    # Set options
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver =  webdriver.Chrome(options=options)
    driver.get('https://codepen.io/')
    return driver

# Scraper terblokir cloudflare, how to bypass it(?)
def main():
    driver = get_driver()
    driver.find_element(by='xpath', value='//*[@id="react-page"]/div/div/div[2]/a[1]').click()
    time.sleep(2)
    #driver.find_element(by='xpath', value='//*[@id="main"]/div/div[1]/div/label').click()
    print(driver.current_url)
    time.sleep(2)
    
print(main())