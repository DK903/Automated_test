# 显示等待： 找不到定位元素 则等待
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://fe-xianyun-web.itheima.net/")
driver.maximize_window()
# 定位 旅游 链接元素并单击
driver.find_element(By.PARTIAL_LINK_TEXT, '旅游攻略').click()
# 使用显式等待 -- 定位 写游记 的button
element = WebDriverWait(driver, 5, 0.5).until(lambda p: p.find_element(
                                                                    By.CLASS_NAME, 'el-button'))
driver.find_element(By.CLASS_NAME, 'el-button').click()
sleep(2)
driver.quit()
