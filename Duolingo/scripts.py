import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def open_browser():
    options = Options()
    options.add_argument("--user-data-dir=./chrome_profile")
    driver = webdriver.Chrome(options=options)
    driver.get("https://duolingo.com")
    return driver

def Indonesian():
    open_browser()
    time.sleep(5)


def Chess(): 
    open_browser()
    time.sleep(5)

def English_Legendary():
    open_browser()
    time.sleep(5)

def Chinese():
    pass

choice = int(input("Enter your language: 1: Indonesian, 2: Chess, 3: English (Legendary Lesson), 4: Chinese. : "))

if choice == 1:
    Indonesian()
elif choice == 2:
    Chess()
elif choice == 3:
    English_Legendary()
elif choice == 4:
    Chinese()
else:
    print("❌ Invalid choice!")