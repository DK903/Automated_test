from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
el = driver.find_element(By.ID, 'kw')
el.send_keys("测试刷新效果")
sleep(1)
driver.refresh()
sleep(1)
