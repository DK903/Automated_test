from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.12306.cn/")
driver.maximize_window()
driver.find_element(By.ID, "train_date").clear()
# 使用Javascript脚本处理日期控件
DateJs = "document.getElementById('train_date').value='2023-11-11'"
driver.execute_script(DateJs)
sleep(3)
driver.find_element(By.ID, "search_one").click()
sleep(3)
driver.quit()
