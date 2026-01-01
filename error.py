from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_argument("--incognito")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()

# 1) Open site
driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH, "//input[@id='user-name']").send_keys("locked_out_user")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
time.sleep(2)
driver.find_element(By.XPATH, "//input[@id='login-button']").click()
time.sleep(2)

# Verify error message
error_msg = driver.find_element(By.XPATH, "//h3[@data-test='error']").text

if error_msg == "Epic sadface: Sorry, this user has been locked out.":
    print("✔ Correct error message displayed")
else:
    print("❌ Wrong error message:", error_msg)
    time.sleep(2)
    driver.quit()