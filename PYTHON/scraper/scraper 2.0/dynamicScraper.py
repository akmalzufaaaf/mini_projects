from selenium import webdriver
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
    driver.get('https://automated.pythonanywhere.com/')
    return driver

def clean_text(text):
    """Extract only temperature from text"""
    output = float(text.split(': ')[1])
    return output

def main():
    driver = get_driver()
    element = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[2]')
    time.sleep(2)
    return element.text

print(clean_text(main()))