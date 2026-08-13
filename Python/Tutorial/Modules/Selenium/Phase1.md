# Phase 1: Setup & Basic Locators (Driver Setup, DOM Parsing, & Core Locators)

## 1. WebDriver Architecture & Environment Setup
* **Package Management**: Install the official Selenium package directly via pip tool strings. 
* **Automated Drivers**: Selenium 4 handles browser drivers natively in the background, eliminating the need to download or link external webdriver files manually.

```bash
pip install selenium
```

### Basic Browser Initialization Script
```python
from selenium import webdriver

# Initialize a clean Google Chrome browser window instance
driver = webdriver.Chrome()

# Navigate to a secure web coordinate destination
driver.get("https://example.com")

# Read metadata attributes directly from the current view context
print("Active Webpage Title:", driver.title)
print("Current Loaded URL:", driver.current_url)

# Always close the active tab and tear down the background process memory
driver.quit()
```

## 2. Browser DevTools & DOM Parsing Basics
* **The DOM Tree**: The Document Object Model represents the hierarchical structural layout of an HTML page.
* **Inspecting Elements**: Press `F12` or right-click any element on a website and select **Inspect** to analyze its HTML attributes (tags, IDs, classes).
* **Target Identification**: Before writing a line of selector script, pinpoint unique identifier markers on an target element like:
  ```html
  <input type="text" id="user-email" name="login_email" class="input-field dynamic-box">
  ```

## 3. Core Static Locators (`By` Mapping Strategies)
* **Strategy Module**: Import the `By` class to explicitly define the lookup type wrapper used to scan the page elements tree.
* **Single Element Retrieval**: Use `.find_element()` to return the very first element matching the search criteria.
* **Array Element Retrieval**: Use `.find_elements()` to return a list of all matching items in order across the DOM.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://wikipedia.org")

# 1. By ID: The fastest and most reliable locator strategy (IDs must be unique)
search_box = driver.find_element(By.ID, "searchInput")

# 2. By NAME: Commonly found on form fields and input layout items
form_language = driver.find_element(By.NAME, "language")

# 3. By CLASS_NAME: Grabs elements based on CSS styling class tags
footer_links_box = driver.find_element(By.CLASS_NAME, "footer-sidebar")

# 4. By TAG_NAME: Locates structural HTML node categories (perfect for counting elements)
all_links = driver.find_elements(By.TAG_NAME, "a")
print("Total links found on page:", len(all_links))

driver.quit()
```

## 4. Hyperlink Locator Strategies
* **Exact Text Matching**: Use `By.LINK_TEXT` to anchor onto precise string text wrapped within anchor `<a>` tags.
* **Partial Text Matching**: Use `By.PARTIAL_LINK_TEXT` to catch links containing a specific sub-string block.

```python
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://wikipedia.org")

# Locate using the exact visible link name text
english_site_link = driver.find_element(By.LINK_TEXT, "English")

# Locate using a fragment of the link name text
portal_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Terms of")

driver.quit()
```

## 5. Core Operational Options Configurations
* **Chrome Options**: Pass argument payloads to modify how your automation browser loads and operates right when it boots up.

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Create a configuration container instance
options = Options()

# Add performance or view arguments
options.add_argument("--start-maximized") # Force screen to open full size
options.add_argument("--incognito")       # Avoid saving cookie data caches

# Pass custom options profiles into the initial engine wrapper
driver = webdriver.Chrome(options=options)
driver.get("https://example.com")

driver.quit()
```
