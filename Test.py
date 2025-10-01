import time
import random
from pywinauto import Application
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
# driver.set_window_size(2000, 1150)
# driver.set_window_position(600, -1000)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#Email
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'))
)
username.send_keys("Admin")
time.sleep(2)

Passward = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'))
)
Passward.send_keys("admin123")
time.sleep(2)

login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button' ))
    
)
login_button.click()
time.sleep(5)
#Admin Page 
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
time.sleep(10)
print("Navigated to the Admin Page")

#Add or search for the user 
add = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'))
)
add.click()
time.sleep(5)

User = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]'))
)
User.click()
time.sleep(2)

#Use Index to locate
options = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)
index = 2
if index < len(options):
    options[index].click()
else:
    print(f"Index {index} out of range. Found {len(options)} options.")

emp_name = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]'))
    )
emp_name.send_keys("someone")
time.sleep(2)

status = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div'))
)
status.click()

#Use Index to locate
options = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@role="option"]'))
)
index = 1
if index < len(options):
    options[index].click()
else:
    print(f"Index {index} out of range. Found {len(options)} options.")

print("Status enable successfuly")
time.sleep(2)

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input'))
)
username.send_keys("Someone's Name")

Passward = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input'))
)
Passward.send_keys("Test@pass123")

confirm_passward = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input'))
)
confirm_passward.send_keys("Test@pass123")

save_button = WebDriverWait(driver,10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]' ))
)
save_button.click()
time.sleep(2)


