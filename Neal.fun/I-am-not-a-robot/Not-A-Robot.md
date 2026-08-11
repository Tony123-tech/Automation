# Neal.fun - Not A Robot Python Automation Guide

This is a Python script using **Selenium** to automatically complete the first two levels of the CAPTCHA game [Neal.fun - Not a Robot](https://neal.fun/not-a-robot).

---

## 🌟 Key Features
* **Full Automation**: Runs from browser launch to verification without any manual input.
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

Download the file or Copy the code exactly as **`not_a_robot_bot.py`**:

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
