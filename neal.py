import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://neal.fun/not-a-robot/")

def level1():
    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "checkmark-spinner-container"))
    )
    checkbox.click()
    print("[Level 1] Checkbox clicked.") 

def level2():
    print("[Level 2] Waiting for tiles to load...")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "grid-item"))
    )

    tiles = driver.find_elements(By.CLASS_NAME, "grid-item")
    print(f"[Level 2] Found {len(tiles)} tiles.")

    target_indexes = [2, 3, 6, 7]
    for idx in target_indexes:
        tiles[idx].click()
        print(f"[Level 2] Tile {idx} clicked.")
        time.sleep(0.3)

    verify_btn = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Verify')]"))
    )
    verify_btn.click()
    print("[Level 2] Verify button clicked.")

level1()
level2()