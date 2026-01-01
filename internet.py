from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Setup Chrome browser ---
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/checkboxes")

# Find both checkboxes
checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")

cb1 = checkboxes[0]   # first checkbox
cb2 = checkboxes[1]   # second checkbox


if not cb1.is_selected():
    cb1.click()
print("First checkbox checked")

time.sleep(1)


if cb1.is_selected():
    cb1.click()
print("First checkbox unchecked")

time.sleep(1)


if not cb2.is_selected():
    cb2.click()
print("Second checkbox checked")

time.sleep(1)

if cb2.is_selected():
    cb2.click()
print("Second checkbox unchecked")

driver.quit()
