from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def open_browser():
    options = Options()
    options.add_argument("--user-data-dir=./chrome_profile")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    
    driver = webdriver.Chrome(options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    
    return driver

driver = open_browser()
driver.get("https://www.duolingo.com")

# Type your Username and Password One Time, then close the driver will remember it.