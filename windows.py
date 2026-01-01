from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(2)
main_window = driver.current_window_handle

driver.find_element(By.LINK_TEXT, "Click Here").click()
time.sleep(2)

all_windows = driver.window_handles

for win in all_windows:
    if win != main_window:
        driver.switch_to.window(win)
        break

print("New window title:", driver.title)
print("Text:", driver.find_element(By.TAG_NAME, "h3").text)

driver.close()
driver.switch_to.window(main_window)

time.sleep(2)
driver.quit()
