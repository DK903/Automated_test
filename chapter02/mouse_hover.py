import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
url = 'https://www.jd.com'
driver.get(url)
# 定位家用电器元素
house_d = driver.find_element(By.XPATH, "//*[@id='J_cate']/ul/li[1]/a")
# 创建鼠标对象
action = ActionChains(driver)
# 调用鼠标悬停的方法
action.move_to_element(house_d)
time.sleep(3)
# 执行
action.perform()
time.sleep(5)
