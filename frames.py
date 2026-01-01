from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(2)

frame = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "mce_0_ifr"))
)
driver.switch_to.frame(frame)
time.sleep(2)

textbox = driver.find_element(By.ID, "tinymce")
textbox.clear()
textbox.send_keys("Hello Frame!")

driver.switch_to.default_content()

time.sleep(2)
driver.quit()
