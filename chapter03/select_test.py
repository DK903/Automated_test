from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
driver = webdriver.Chrome()
driver.get("D:/Automated_testing/chapter03/TestProject/register.html")
driver.maximize_window()
# 定位下拉选择框
element = driver.find_element(By.XPATH, "//*[@id='selectA']")
select = Select(element)
# 根据索引值定位 -- 广州
select.select_by_index(2)
sleep(2)
# 根据value值定位 -- 上海
select.select_by_value("sh")
sleep(2)
# 根据文本定位 -- 深圳
select.select_by_visible_text("深圳")
driver.quit()
