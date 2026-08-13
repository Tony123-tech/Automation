# Phase 4: Advanced User Actions & Deep Customization (Mouse Actions, JS Injection, & Headless Settings)

## 1. The ActionChains Chaining Framework
* **Composite Interactions**: Low-level interactions (like mouse hovers, drag-and-drop, and modifier key holding) require using the specialized `ActionChains` utility framework.
* **Execution Rule**: Interactions are queued up sequentially inside the script memory space and do not execute until you call the `.perform()` method at the very end of the chain.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://example.com")

# Instantiate the ActionChains tracking engine linked to the driver instance
actions = ActionChains(driver)

# Locate target navigation elements
menu_dropdown = driver.find_element(By.ID, "nav-electronics-menu")
sub_category_link = driver.find_element(By.LINK_TEXT, "Smart Home Automation")

# 1. Hover mouse over the menu, pause, move to sub-category item, and execute click
actions.move_to_element(menu_dropdown).move_to_element(sub_category_link).click().perform()

driver.quit()
```

## 2. Advanced Mouse Interactions (Right-Click & Drag-and-Drop)
* **Context Manipulation**: Simulate double clicks, canvas element movement, or context menu right-clicks.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://example.com")
actions = ActionChains(driver)

# Example A: Triggering a custom right-click context menu structure
context_block = driver.find_element(By.ID, "right-click-zone")
actions.context_click(context_block).perform()

# Example B: Dragging an object node source across coordinates into a target landing container box
draggable_item = driver.find_element(By.ID, "source-item")
drop_target = driver.find_element(By.ID, "destination-bucket")

actions.drag_and_drop(draggable_item, drop_target).perform()

driver.quit()
```

## 3. Keyboard Automation & Modifiers
* **Key Holding Layouts**: Hold down tracking keys like `SHIFT`, `CONTROL`, or `COMMAND` to copy, select all, or multi-select items in a menu.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://example.com")
actions = ActionChains(driver)

text_input = driver.find_element(By.ID, "editor-textarea")
text_input.send_keys("Automated text snippet injection payload.")

# Execute a Select-All (Control + A) keyboard sequence pattern directly via the chain script
actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

driver.quit()
```

## 4. Native JavaScript Execution (Bypassing Driver Blockers)
* **Direct DOM Control**: Inject raw synchronous JavaScript directly into the browser context. This is incredibly useful for scrolling infinite-scroll containers or clicking elements obscured by hidden overlaps.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

# Example A: Smoothly scroll down the browser window viewport by 1000 pixels vertical depth
driver.execute_script("window.scrollBy(0, 1000);")

# Example B: Force a direct element click injection bypassing overlapping UI element blockers
hidden_btn = driver.find_element(By.CSS_SELECTOR, "button.hidden-submit")
driver.execute_script("arguments[0].click();", hidden_btn)

# Example C: Read custom execution parameters straight out of the site window context memory
current_user_token = driver.execute_script("return window.localStorage.getItem('auth_token');")
print("Extracted Browser Auth Token:", current_user_token)

driver.quit()
```

## 5. Headless Automation & Enterprise Management Configurations
* **Headless execution**: Run your script completely in the background without launching a physical browser window. This saves system resources and is ideal for web scraping or CI/CD servers.

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()

# Performance configurations flags
chrome_options.add_argument("--headless=new") # Run in background without a UI window canvas
chrome_options.add_argument("--disable-gpu")   # Turn off hardware acceleration for server environments
chrome_options.add_argument("--mute-audio")    # Prevent media sounds from playing during automation runs

# Set standard window tracking aspect ratios even while headless to avoid element clipping errors
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://example.com")

print("Headless Scraper Loaded Title Successfully:", driver.title)
driver.quit()
```
