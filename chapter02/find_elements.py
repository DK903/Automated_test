import random
import time
from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()
url = "https://www.itcast.cn/"
driver.get(url)
# 获取首页头部横向所有链接
elements = driver.find_elements(By.CLASS_NAME, "a2_js")
length = len(elements)
# 随机获取一个链接
Random_selection = random.randint(0, length - 1)
elements[Random_selection].click()
time.sleep(3)
