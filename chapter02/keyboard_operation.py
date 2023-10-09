from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.jd.com")
# 定位输入框元素并输入内容
input_box = driver.find_element(By.XPATH, "//*[@id='key']")
input_box.send_keys("测试")
time.sleep(3)
# 调用删除键方法
input_box.send_keys(Keys.BACK_SPACE)
input_box.send_keys(Keys.BACK_SPACE)
time.sleep(3)
input_box.send_keys("书籍")
time.sleep(3)
# 调用全选/剪切/粘贴/回车方法
input_box.send_keys(Keys.CONTROL, 'a')
input_box.send_keys(Keys.CONTROL, 'x')
input_box.send_keys(Keys.CONTROL, 'v')
input_box.send_keys(Keys.ENTER)
time.sleep(2)
