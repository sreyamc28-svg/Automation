from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# open browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# open google
driver.get("https://www.google.com")

# find the search box (name="q")
search_box = driver.find_element(By.NAME, "q")

# type text
search_box.send_keys("selenium with python tutorial")

# press Enter
search_box.send_keys(Keys.RETURN)

# wait 5 seconds so you can see results
time.sleep(5)

# close browser
driver.quit()