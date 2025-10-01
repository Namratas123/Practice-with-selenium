from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Step 1: Open the browser
driver = webdriver.Chrome()

# Step 2: Go to the login page
driver.get("https://example.com/login")

# Step 3: Enter username
username = driver.find_element(By.ID, "username")
username.send_keys("test_user")

# Step 4: Enter password
password = driver.find_element(By.ID, "password")
password.send_keys("secure_password")

# Step 5: Click login button
login_button = driver.find_element(By.ID, "loginBtn")
login_button.click()

# Step 6: Validate login success
try:
    dashboard = driver.find_element(By.XPATH, "//h1[text()='Dashboard']")
    print("✅ Test Passed: Login successful")
except:
    print("❌ Test Failed: Login not successful")

# Step 7: Close the browser
driver.quit()
