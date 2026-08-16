from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def open_browser():
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    driver = webdriver.Chrome(options=options)
    return driver

def Indonesian():
    print("🇮🇩 Starting Indonesian...")
    driver = open_browser()
    driver.get("https://www.duolingo.com")
    time.sleep(5)

def Chess():
    print("♟️ Starting Chess...")
    driver = open_browser()
    driver.get("https://www.duolingo.com")
    time.sleep(5)

def English_Legendary():
    print("⭐ Starting English Legendary...")
    driver = open_browser()
    driver.get("https://www.duolingo.com")
    time.sleep(5)

def Chinese():
    print("🇨🇳 Starting Chinese...")
    driver = open_browser()
    driver.get("https://www.duolingo.com")
    time.sleep(5)

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