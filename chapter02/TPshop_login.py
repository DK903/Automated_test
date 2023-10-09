import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "https://hmshop-test.itheima.net/Home/user/login.html"
driver.get(url)
username = (driver.find_element(By.NAME, "username"))
username.send_keys("13012345678")
time.sleep(0.5)
password = (driver.find_element(By.NAME, "password"))
password.send_keys("123456")
time.sleep(0.5)
driver.find_element(By.ID, "verify_code").send_keys("8888")
time.sleep(0.5)
driver.find_element(By.XPATH, "//*[@id='loginform']/div/div[6]/a").click()
time.sleep(10)
