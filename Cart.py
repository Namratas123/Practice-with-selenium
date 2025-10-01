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
driver.get("https://www.demoblaze.com/index.html")
time.sleep(5)

#Categories
phones = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Laptops']"))
)
phones.click()
time.sleep(2)
choose_laptop = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="tbodyid"]/div[5]/div/div/h4/a'))
)
choose_laptop.click()
time.sleep(2)

driver.find_element(By.XPATH, "//a[text()='Add to cart']").click()
time.sleep(2)
# Switch to alert
alert = driver.switch_to.alert  
# Accept alert (OK)
alert.accept()
time.sleep(2)

#Navigate to cart

cart = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[text()='Cart']"))
)
cart.click()
time.sleep(5)

place_order = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="page-wrapper"]/div/div[2]/button'))
)
place_order.click()
time.sleep(5)

#Place Order modal/form
name = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="name"]'))
)
name.send_keys("Someone")
time.sleep(2)

country = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="country"]' ))
)
country.send_keys("India")
time.sleep(1)

city = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="city"]'))
)
city.send_keys("Raipur")
time.sleep(1)

credit_card = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="card"]'))
)
credit_card.send_keys("4576454656476")
time.sleep(1)

Month = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="month"]' ))
)
Month.send_keys("09")
time.sleep(1)

Year = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="year"]' ))
)
Year.send_keys("2027")
time.sleep(1)

Purchase = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="orderModal"]/div/div/div[3]/button[2]' ))
)
Purchase.click()
time.sleep(2)

# driver.find_element(By.XPATH, "//div[text()='OK']").click()
# time.sleep(2)
# # Switch to alert
# alert = driver.switch_to.alert  
# # Accept alert (OK)
# alert.accept()
# time.sleep(2)

#Modal for confirmation 

Purchase_ok = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[10]/div[7]/div/button'))
)
Purchase_ok.click()
time.sleep(5)
