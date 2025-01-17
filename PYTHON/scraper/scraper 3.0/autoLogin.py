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
    driver.get('https://automated.pythonanywhere.com/login/')
    return driver

def main():
    driver = get_driver()
    driver.find_element(by='id', value='id_username').send_keys('automated')
    time.sleep(2)
    driver.find_element(by='id', value='id_password').send_keys('automatedautomated')# + Keys.ENTER)
    driver.find_element(by='xpath', value='/html/body/div[1]/div/div/div[3]/form/button').click() #try to use click() because not all website support enter to login/send request login.
    time.sleep(2)
    driver.find_element(by='xpath', value='/html/body/nav/div/a').click()
    print(driver.current_url)
    time.sleep(3)
    
print(main())