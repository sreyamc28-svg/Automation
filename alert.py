import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
time.sleep(2)

alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
print(alert.text)

alert.accept()

driver.quit()
