from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("D:/Automated_testing/chapter03/TestProject/frameswitch.html")
driver.maximize_window()
# 获取第一个 iframe
first_iframe = driver.find_element(By.ID, "idframe1")
# 切换到第一个 iframe
driver.switch_to.frame(first_iframe)
driver.find_element(By.ID, "AuserA").send_keys("admin")
sleep(2)
# 非常重要！ 需要切换回默认的再进行选择
driver.switch_to.default_content()
s_iframe = driver.find_element(By.ID, 'idframe2')
driver.switch_to.frame(s_iframe)
driver.find_element(By.ID, "BuserA").send_keys("nimda")
sleep(2)
driver.quit()
