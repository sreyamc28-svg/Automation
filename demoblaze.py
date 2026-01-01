from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# Step 1: Open Demoblaze
driver.get("https://www.demoblaze.com")

time.sleep(2)

# Scroll Down
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
time.sleep(2)

# Scroll Up to Top to avoid clicking wrong product
driver.find_element(By.TAG_NAME, "body").send_keys(Keys.HOME)
time.sleep(2)

# Step 2: Click product (Samsung galaxy s6)
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Samsung galaxy s6']"))
).click()

time.sleep(2)

# Add to Cart
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Add to cart']"))
).click()

# Handle Alert Popup
WebDriverWait(driver, 10).until(EC.alert_is_present())
alert = driver.switch_to.alert
alert.accept()

print("Product added to cart successfully!")

# Open Cart
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Cart']"))
).click()

# Wait for Cart Table to load
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//tbody/tr"))
)

# Get product name from cart
product_in_cart = driver.find_element(By.XPATH, "//tbody/tr[1]/td[2]").text

# Validate name (case-insensitive)
print("DEBUG Product in cart:", product_in_cart)
assert "galaxy" in product_in_cart.lower(), " Product not added properly to cart!"
print(" Product verified in cart:", product_in_cart)

# Click Place Order
WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))
).click()

# Fill Form
WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "name"))
).send_keys("Sreya MC")
driver.find_element(By.ID, "country").send_keys("India")
driver.find_element(By.ID, "city").send_keys("Kochi")
driver.find_element(By.ID, "card").send_keys("1234567890123456")
driver.find_element(By.ID, "month").send_keys("12")
driver.find_element(By.ID, "year").send_keys("2025")

# Click Purchase
driver.find_element(By.XPATH, "//button[text()='Purchase']").click()

# Success Message

success_text = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//h2"))
).text

# Verify success message
clean_text = success_text.lower().strip()
if "Thank you" in clean_text:
    print(" Purchase message verified!")
else:
    print("Wrong purchase message! Actual text:", clean_text)

# Screenshot
driver.save_screenshot("purchase_success.png")
print("Screenshot saved as purchase_success.png")

# Click OK and exit
driver.find_element(By.XPATH, "//button[text()='OK']").click()

driver.quit()
