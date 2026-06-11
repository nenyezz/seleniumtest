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
EMAIL = "chinenye.o@irecharge.ng"
PASSWORD = "2A99w+A>dJ4$;v%"

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
    time.sleep(3)

    # If Enter didn't work, click the login button manually
    if "/auth/login" in driver.current_url:
        print("Enter key didn't work, trying the login button...")
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        login_button.click()
        time.sleep(3)

    # Check if login was successful
    if "/auth/login" not in driver.current_url:
        if "dashboard" in driver.current_url.lower() or driver.title == "Dashboard | Accelerate" or driver.title == "Device Verification | Accelerate":
            print("Test Passed: Login worked and the Dashboard loaded.")
        else:
            print(f"Login worked but landed on an unexpected page: {driver.current_url}")
    else:
        print("Test Failed: Still on the login page after submitting.")
        print("Double check that your email and password are correct.")

except Exception as e:
    print(f"Something went wrong: {e}")
    print(f"URL at time of error: {driver.current_url}")

finally:
    time.sleep(2)
    driver.quit()