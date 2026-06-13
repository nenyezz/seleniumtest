from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

# Setup
service = Service(executable_path=r"C:\Users\Chinenye Obasi\Desktop\selenium testing project\geckodriver.exe")
driver = webdriver.Firefox(service=service, options=webdriver.FirefoxOptions())
driver.maximize_window()

# Credentials
EMAIL = "youremail"
PASSWORD = "yourpassword"

# Open the login page
driver.get("https://staging--accelerate-02-web.netlify.app/auth/login")
time.sleep(3)  # Give the page time to load

try:
    wait = WebDriverWait(driver, 20)

    # Find and fill in the username
    username_field = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
    username_field.click()
    username_field.clear()
    username_field.send_keys(EMAIL)
    time.sleep(1)

    # Find and fill in the password
    password_field = wait.until(EC.element_to_be_clickable((By.NAME, "password")))
    password_field.click()
    password_field.clear()
    password_field.send_keys(PASSWORD)
    time.sleep(1)

    # Submit the form by pressing Enter
    password_field.send_keys(Keys.RETURN)
    time.sleep(10)

    # Check if login was successful
    if driver.current_url == "https://staging--accelerate-02-web.netlify.app/auth/login/device-verification" or driver.title == "Device Verification | Accelerate":
        print("Test Passed: Login worked and Device Verification loaded.")
    else:
        print(f"Login worked but landed on an unexpected page: {driver.current_url}")

except Exception as e:
    print(f"Something went wrong: {e}")
    print(f"URL at time of error: {driver.current_url}")

finally:
    time.sleep(5)
    driver.quit()
