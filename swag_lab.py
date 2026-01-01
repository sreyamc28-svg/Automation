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

# 2) Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# 3) Scroll down
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
time.sleep(1)

# 4) Scroll up
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_UP)
time.sleep(1)

# 5) Add item to cart
driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
time.sleep(1)

# 6) Open cart
driver.find_element(By.ID, "shopping_cart_container").click()
time.sleep(1)

# 7) Checkout
driver.find_element(By.ID, "checkout").click()
time.sleep(1)

# 8) Fill checkout details
driver.find_element(By.ID, "first-name").send_keys("Sreya")
driver.find_element(By.ID, "last-name").send_keys("MC")
driver.find_element(By.ID, "postal-code").send_keys("567890")
time.sleep(1)

# 9) Continue
driver.find_element(By.ID, "continue").click()
time.sleep(1)

# 10) Finish
driver.find_element(By.ID, "finish").click()
time.sleep(2)
success_text = driver.find_element(By.CLASS_NAME, "complete-header").text

if success_text != "Thank you for your order!":
    print(" BUG: Wrong success message:", success_text)
else:
    print(" Success message correct")
driver.find_element(By.ID, "back-to-products").click()
time.sleep(2)

# 12) Logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(1)
driver.find_element(By.ID, "logout_sidebar_link").click()

print("Order completed and logged out")

time.sleep(2)
driver.quit()

