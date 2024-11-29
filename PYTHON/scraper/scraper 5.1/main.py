from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime as dt
import csv

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.get('https://automated.pythonanywhere.com/')
    return driver

def clean_text(text):
    """Extract only temperature from text"""
    output = float(text.split(": ")[1])
    return output

def get_list(text):
    """Make a list format to append to the CSV file"""
    date = f"{dt.now().strftime('%Y-%b-%d')}"
    hour = f"{dt.now().strftime('%H-%M-%S')}"
    output = [date, hour, text]
    return output

def write_file(text):
    """Write input text into text file"""
    filename = f"./scraper 5.1/output.csv"
    data = get_list(text)
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

def main():
    driver = get_driver()
    while True:
        time.sleep(2)
        element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
        text = str(clean_text(element.text))
        write_file(text)

print(main())
