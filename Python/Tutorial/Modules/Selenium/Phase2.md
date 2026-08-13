# Phase 2: User Interactions (Form Handling, Alerts, Windows, & Frames)

## 1. Advanced Form Handling & Element Control
* **Action Pipeline**: Interacting with elements requires finding them first, clearing existing text placeholders, and injecting new string parameters.
* **Keyboard Emulation**: Import the `Keys` engine token package to execute structural hardware actions like hitting Enter, Backspace, or tab sequences.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://example.com")

# Locating fields
email_field = driver.find_element(By.ID, "user-email")

# Interacting with inputs
email_field.clear()                      # Clear default data templates
email_field.send_keys("test@example.com") # Simulate typing keystrokes
email_field.send_keys(Keys.TAB)          # Jump to next field via hardware key

# Extracting element feedback state values
login_button = driver.find_element(By.ID, "submit-btn")
print("Is button interactive?", login_button.is_enabled())
print("Button screen text:", login_button.text)

login_button.click() # Simulate precise mouse click event
```

## 2. Targeting Complex Dropdown Selection Menus
* **Select Class Wrappers**: Standard dropdown elements wrapped inside `<select>` HTML tags cannot be interacted with via simple clicks. You must use Selenium's dedicated `Select` utility wrapper class.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://example.com")

# Bind the target select element node into the Select utility tracker
dropdown_element = driver.find_element(By.ID, "country-select")
select_control = Select(dropdown_element)

# Selection Core Strategies
select_control.select_by_visible_text("Hong Kong") # Match user-facing text string
select_control.select_by_value("HK")               # Match backend HTML attribute value
select_control.select_by_index(3)                  # Match structural index order (0-indexed)

# Reading current selected option state
print("Active Selection:", select_control.first_selected_option.text)
driver.quit()
```

## 3. Handling Browser Native Alert Popups
* **Alert Interception**: Web browser modal alert frames (like `alert()`, `confirm()`, or `prompt()`) do not live inside the page DOM tree. You must explicitly shift the automated focus engine over to capture them.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

# Trigger an alert popup on the page
driver.find_element(By.ID, "trigger-alert-btn").click()

# Shift browser logic context focus over to the alert pop frame modal
alert_window = driver.switch_to.alert

print("Alert text notification message:", alert_window.text)

alert_window.send_keys("Confirmation text parameter payload") # Type into prompts if needed
alert_window.accept()                                         # Confirm choice (Clicks OK)
# alert_window.dismiss()                                      # Reject choice (Clicks Cancel)
```

## 4. Multi-Tab & Window Handles Management
* **Window Identifiers**: Every open browser tab or window is assigned a unique alphanumeric background hash string called a **Window Handle**.
* **Switching Spaces**: Track active handles to bounce back and forth between popups or new windows smoothly.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

# Cache current home window space location point
original_window_handle = driver.current_window_handle

# Trigger action that pops open a brand new display tab window
driver.find_element(By.ID, "open-terms-link").click()

# Loop through all active open tab handles inside the environment window registry
all_open_handles = driver.window_handles

for handle in all_open_handles:
    if handle != original_window_handle:
        driver.switch_to.window(handle) # Shift automation engine over to the new tab
        break

print("New Tab Web Page Title:", driver.title)
driver.close() # Close ONLY the current focused active sub-tab screen window

# Safely route control tracking back to your original workspace window location
driver.switch_to.window(original_window_handle)
```

## 5. Navigating Embedded iFrames
* **Boundary Obstacles**: Inline Frames (`<iframe>`) represent standalone HTML document hierarchies embedded completely within a parent webpage layout. Selenium cannot view inside them until you break through the frame threshold.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://example.com")

# 1. Target the iframe element vehicle box boundary node
embedded_frame = driver.find_element(By.CSS_SELECTOR, "iframe.payment-widget")

# 2. Submerge the driver focus framework completely inside the targeted iframe container
driver.switch_to.frame(embedded_frame)

# Perform inner form text field actions safely inside the iframe DOM bubble boundary
credit_card_input = driver.find_element(By.NAME, "cc_number")
credit_card_input.send_keys("4111222233334444")

# 3. Pull the tracking engine focus all the way back up out to the root primary webpage layer
driver.switch_to.default_content()
driver.quit()
```