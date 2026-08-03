from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://google.com")

search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("poki" + Keys.ENTER)

first_result = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "h3"))
)
first_result.click()

time.sleep(3)

poki_search_btn = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label*='search']"))
)
actions = ActionChains(driver)
actions.move_to_element(poki_search_btn).click().perform()

search_input = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='search'], input[type='text']"))
)

game_name = "level devil"
for letter in game_name:
    search_input.send_keys(letter)
    time.sleep(random.uniform(0.08, 0.18))

search_input.send_keys(Keys.ENTER)

time.sleep(3)

level_devil_tile = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "img[alt*='Level Devil']"))
)

actions.reset_actions()  
actions.move_to_element(level_devil_tile).click().perform()

fullscreen_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "span[aria-label='ui-icons-fullscreen']"))
)
fullscreen_button.click()
