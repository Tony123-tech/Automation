# Phase 5: Architecture, Page Object Model (POM), & Test Framework Scale

## 1. The Page Object Model (POM) Design Pattern
* **The Structural Pattern**: Avoid writing element locators directly inside your test validation scripts. Instead, isolate every distinct web page into its own dedicated Python class representation.
* **Maintenance Advantage**: If a developer changes a button ID from `submit-btn` to `confirm-button`, you only have to update it once inside the page object file rather than correcting hundreds of distinct script files.

### The Page Object File (`pages/login_page.py`)
```python
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
	def __init__(self, driver):
		self.driver = driver
		self.wait = WebDriverWait(driver, 10)
		
		# Define clean locator tuples up top
		self.username_input = (By.ID, "user-email")
		self.password_input = (By.ID, "user-pass")
		self.submit_btn = (By.CSS_SELECTOR, "button[type='submit']")
		self.error_banner = (By.CLASS_NAME, "alert-danger")

	def navigate(self):
		self.driver.get("https://example.com")

	def login(self, username, password):
		# Intelligently wait and interact with abstract method wrappers
		u_field = self.wait.until(EC.visibility_of_element_located(self.username_input))
		u_field.clear()
		u_field.send_keys(username)
		
		p_field = self.driver.find_element(*self.password_input) # Asterisk unpacks the tuple
		p_field.clear()
		p_field.send_keys(password)
		
		self.wait.until(EC.element_to_be_clickable(self.submit_btn)).click()

	def get_error_message(self):
		return self.wait.until(EC.visibility_of_element_located(self.error_banner)).text
```

## 2. Testing Framework Integration via PyTest
* **Test Runner Architecture**: Use **PyTest** to add assertions, group test variants cleanly, run assertions smoothly, and handle automatic browser setup and teardown tasks via fixtures.

```bash
pip install pytest
```

### The Test Execution Script File (`tests/test_auth.py`)
```python
import pytest
from selenium import webdriver
from pages.login_page import LoginPage # Import our POM class

# Define a shared execution routine (Fixture) for setup and automatic cleanup teardown
@pytest.fixture
def driver_setup():
	driver = webdriver.Chrome()
	driver.maximize_window()
	yield driver # Pass this active initialization state down into the test case
	driver.quit() # Tethers to teardown framework cleanup when the test finishes

def test_invalid_login_credentials(driver_setup):
	driver = driver_setup
	login_page = LoginPage(driver)
	
	# Execute actions via clean abstract layer keywords
	login_page.navigate()
	login_page.login("fakeuser@example.com", "WrongPassword123")
	
	# Verify output explicitly using standardized PyTest assertions
	expected_error = "Invalid username or password."
	assert login_page.get_error_message() == expected_error
```

## 3. Data-Driven Testing (Parameters Injection)
* **Scale Execution Validation**: Feed an external dictionary array straight into your test framework routines to validate dozens of input scenarios automatically using a single structural block.

```python
import pytest
from pages.login_page import LoginPage

# Inject structured test criteria rows natively inside the engine run loop
@pytest.mark.parametrize(
	"username, password, expected_error",
	[
		("", "Pass123!", "Username field is required."),
		("test@user.com", "", "Password field is required."),
		("banned@user.com", "Pass123!", "This account has been suspended.")
	]
)
def test_validation_rules(driver_setup, username, password, expected_error):
	driver = driver_setup
	login_page = LoginPage(driver)
	
	login_page.navigate()
	login_page.login(username, password)
	
	assert login_page.get_error_message() == expected_error
```

## 4. Professional Execution & Reporting
* **Parallel Performance Runs**: Scale test runtime footprints across multiple native threads to speed up long integration pipelines.
* **Visual Summary Generation**: Create highly readable HTML report files with pass/fail timing logs.

```bash
pip install pytest-xdist pytest-html
```

### Command-Line Suite Execution Variations
```bash
# Run all tests located in the directory tree cleanly
pytest

# Execute tests in parallel across 4 matching CPU execution tracks
pytest -n 4

# Run all test variants and output a detailed visual execution report
pytest --html=reports/test_summary_report.html --self-contained-html
```

## 5. Enterprise Exceptions & Failure Capture Handling
* **Resilient Audits**: Configure your framework to dynamically capture full-page screenshot verification evidence whenever a test hits a system road-block or validation failure.

```python
import os
import pytest

# Example of embedding failure tracking directly inside a test layout configuration
def test_dashboard_access(driver_setup):
	driver = driver_setup
	driver.get("https://example.com")
	
	try:
		assert "Dashboard" in driver.title
	except AssertionError as failure:
		# Create an output repository directory path
		os.makedirs("reports/screenshots", exist_ok=True)
		
		# Save exact window context data state evidence directly to a file
		driver.save_screenshot("reports/screenshots/dashboard_failure.png")
		raise failure # Rethrow the error so the tracking runner scores it accurately
```
