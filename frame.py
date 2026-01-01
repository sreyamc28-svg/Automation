from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")

frame = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "mce_0_ifr"))
)
driver.switch_to.frame(frame)

editor = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "tinymce"))
)

editor.click()
editor.send_keys(Keys.CONTROL + "a")
editor.send_keys(Keys.DELETE)
editor.send_keys("Hello from iframe!")

driver.switch_to.default_content()
time.sleep(2)
driver.quit()
