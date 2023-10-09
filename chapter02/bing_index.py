from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
url = 'https://cn.bing.com'
driver.get(url)
# 定位搜索框并输入内容
cin = driver.find_element(By.XPATH, "//input[@id='sb_form_q']")
cin.send_keys("软件")
time.sleep(3)
cin.clear()
cin.send_keys("软件测试")
time.sleep(3)
# 提交表单
cin.submit()
time.sleep(2)
