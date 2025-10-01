# from selenium import webdriver
# from selenium.webdriver.common.by import By

# browser = webdriver.Chrome()
# browser.get("https://cosmocode.io/automation-practice-webtable/")
# browser.maximize_window()
# browser.execute_script("Window.scrollTo(0,700)")
# table = browser.find_element(By.XPATH,  '//*[@id="countries"]/tbody/tr[1]/td[2]/h3/strong')

#To Run and execute all the test in parallel
#use pytest-xdist
#and "pytest -n 4" in terminal 
#if want to learn specific files: pytest test_login test_cart.py -n 2