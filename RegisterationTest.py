#For Registeration Test
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://127.0.0.1:8000/account/register/")
driver.find_element_by_name("first_name").send_keys("Paaaarth")
driver.find_element_by_name("last_name").send_keys("Shaaaah")
driver.find_element_by_name("username").send_keys("imparth0611")
driver.find_element_by_name("email").send_keys("prbshah49@gmail.com")
driver.find_element_by_name("password1").send_keys("@selenium")
driver.find_element_by_name("password2").send_keys("@selenium")
driver.find_element_by_id("submit").click()
print("Test completed registered successfully.")

