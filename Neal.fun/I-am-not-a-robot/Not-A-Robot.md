# Neal.fun - Not A Robot Python Automation Guide

This is a Python script using **Selenium** to automatically complete the first two levels of the CAPTCHA game [Neal.fun - Not a Robot](https://neal.fun/not-a-robot).

---

## 🌟 Key Features
* **Full Automation**: Runs from browser launch to verification without any manual input.
* **Dynamic Waiting**: Uses `WebDriverWait` to ensure elements are fully loaded before clicking, preventing race conditions and script crashes.
* **Modular Structure**: Separates logic into `level1()` and `level2()` functions for easy future expansion.

---

## 🛠️ Environment Setup

Before running the Python script, make sure your system has the required package installed.

### 1. Install Dependencies
Open your Terminal or Command Prompt (CMD) and execute the following command:
```bash
pip install selenium
```

### 2. Browser Driver
The script targets Google Chrome. Ensure Chrome is installed on your computer; Selenium will automatically manage the WebDriver binaries.

---

## 📄 Complete Python Source Code

Save the code below exactly as **`not_a_robot_bot.py`**:

```python
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://neal.fun")

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

try:
    level1()
    level2()
    time.sleep(5)

finally:
    driver.quit()
```

---

## 🛑 Execution and Termination

### How to Run
Navigate to the directory containing your script using the terminal, then run:
```bash
python not_a_robot_bot.py
```

### How to Stop
* If the script is actively running, press **`Ctrl + C`** in your terminal window to force terminate it.
* Once the script finishes `level2()`, it will sleep for 5 seconds and automatically close the browser window.
