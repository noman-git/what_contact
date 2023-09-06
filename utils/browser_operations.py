from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def setup_browser(wait_time=30):
    browser = webdriver.Chrome()
    
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--user-data-dir=/dev/null")

    browser = webdriver.Chrome(options=chrome_options)

    browser.get('https://web.whatsapp.com/')
    wait = WebDriverWait(browser, wait_time)
    return browser, wait