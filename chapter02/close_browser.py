from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element(By.PARTIAL_LINK_TEXT, '贴吧').click()
sleep(2)
# 关闭浏览器当前窗口
driver.close()
sleep(2)
# 关闭浏览器所有窗口
driver.quit()
