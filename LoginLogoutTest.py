#Login & Logout Test
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
#Login
driver.get("http://127.0.0.1:8000/account/login/")
driver.find_element_by_name("username").send_keys("iparthh0611")
driver.find_element_by_name("password").send_keys("@selenium")
driver.find_element_by_id("submit").click()
#Logout
driver.find_element_by_class_name("nav-link").click()
print("Test completed registered successfully.")
print("Test successfull.")