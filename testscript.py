from time import time

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path=r"C:\Users\Chinenye Obasi\Desktop\selenium testing project\geckodriver.exe")
options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(service=service, options=options)

driver.implicitly_wait(30)
driver.maximize_window()

driver.get("https://staging--accelerate-02-web.netlify.app/auth/login")


username_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#_r_q_-form-item"))
)

password_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#_r_r_-form-item"))
)

login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
)
username_input.send_keys("chinenye.o@irecharge.ng")
password_input.send_keys("2&d""x?9-_Vs3Ahp")
login_button.click()
#time.sleep(10)
actual_title = driver.title
expected_title = "Dashboard | Accelerate"
if actual_title == expected_title:
    print("Test Passed: Login successful, Dashboard page loaded.")
else:
    print("Test Failed: Login failed or incorrect page loaded.")

driver.quit()