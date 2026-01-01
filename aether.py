from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# --- Setup browser ---
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

# --- 1) Open the login page ---
driver.get("https://uat-aether.chisquarelabs.uk/login?redirect=%2Fhome")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/main/div/form/div[1]/div/input").send_keys("admin@aether.com")
time.sleep(1)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/main/div/form/div[2]/div/input").send_keys("admin123@ather")
time.sleep(.5)
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/main/div/form/button").click()
time.sleep(0.5)

otp_digits = "123456"
otp_boxes = WebDriverWait(driver, 10).until(
   EC.presence_of_all_elements_located(
       (By.XPATH, "//input[@inputmode='numeric' and @type='text']")
   )
)

# --- Type 1 digit in each box ---
for box, digit in zip(otp_boxes, otp_digits):
   box.send_keys(digit)

print("OTP entered")
driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/main/div/form/button").click()
time.sleep(0.5)

heading_text = WebDriverWait(driver, 15).until(
   EC.visibility_of_element_located(
       (By.XPATH, "/html/body/div[2]/main/div/main/div/div/div[1]/h1")
   )
).text

if "Clinician" in heading_text and "Patient List" in heading_text:
   print("Landed on Clinician · Patient List page")
else:
   print("Wrong page, heading is:", heading_text)

allpatients_btn = WebDriverWait(driver, 10).until(
   EC.element_to_be_clickable(
       (By.XPATH, "/html/body/div[2]/main/div/main/div/div/div[2]/div[1]/div/div/button[2]")
   )
)
allpatients_btn.click()
print("Clicked all patients button")
time.sleep(0.5)

view_btn = WebDriverWait(driver, 10).until(
   EC.element_to_be_clickable(
       (By.XPATH, "/html/body/div[2]/main/div/main/div/div/div[3]/div[1]/table/tbody/tr[1]/td[6]/div/a")
   )
)
view_btn.click()
print("Clicked view button")
time.sleep(0.5)

startencounter_btn = WebDriverWait(driver, 10).until(
   EC.element_to_be_clickable(
       (By.XPATH, "/html/body/div[2]/main/div/main/div/div[2]/div[2]/div[3]/button[1]")
   )
)
startencounter_btn.click()
print("Clicked start encounter button")
time.sleep(0.5)

# -------- tick the first checkbox --------
checkbox =driver.find_element(By.XPATH,"(//button[@value='on'])[1]").click()
time.sleep(0.5)
checkbo=driver.find_element(By.XPATH,"(//button[@value='on'])[2]").click()
time.sleep(0.5)
checkb =driver.find_element(By.XPATH,"(//button[@value='on'])[3]").click()
time.sleep(0.5)
twocheckbox =driver.find_element(By.XPATH,"(//button[@value='on'])[4]").click()
time.sleep(0.5)
twocheckbo = driver.find_element(By.XPATH,"(//button[@value='on'])[5]").click()
time.sleep(0.5)
twocheckb =driver.find_element(By.XPATH,"(//button[@value='on'])[6]").click()
time.sleep(0.5)
twcheckb =driver.find_element(By.XPATH,"(//button[@value='on'])[7]").click()
time.sleep(0.5)



driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbox)
driver.execute_script("arguments[0].click();", checkbox)

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkbo)
driver.execute_script("arguments[0].click();", checkbo)

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", checkb)
driver.execute_script("arguments[0].click();", checkb)

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", twocheckbox)
driver.execute_script("arguments[0].click();", twocheckbox)

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", twocheckb)
driver.execute_script("arguments[0].click();", twocheckb)

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", twocheckb)
driver.execute_script("arguments[0].click();", twocheckb)

driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", twcheckb)
driver.execute_script("arguments[0].click();", twcheckb)


# driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", confirm_btn)
# driver.execute_script("arguments[0].click();", confirm_btn)
# confirm_btn=driver.find_element(By.XPATH,"(/html/body/div[4]/div[2]/div[2]/div/div[8]/button[2]").click()
# time.sleep(1)


confirm_btn = WebDriverWait(driver, 20).until(
    lambda d: d.find_element(
        By.XPATH, "//button[normalize-space()='Confirm Consent' and not(@aria-disabled='true')]"
    )
)
driver.execute_script(
    "arguments[0].scrollIntoView({block:'center'});", confirm_btn
)
time.sleep(1.5)

driver.execute_script("arguments[0].click();", confirm_btn)

print("Confirm Consent clicked")


driver.quit()
