from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
url = "https://hmshop-test.itheima.net/Home/user/reg.html"
driver.get(url)
time.sleep(3)
# 定位复选框元素
box = driver.find_element(By.CLASS_NAME, "J_protocal")
# 判断
print(box.is_selected())
