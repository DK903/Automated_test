from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.maximize_window()
# 获取当前页面所有的Cookie信息
cookie1 = driver.get_cookies()
# 添加cookie
driver.add_cookie({'name': 'testname', 'value': '123456'})
# 获取指定的cookie
print("获取指定的cookie：", driver.get_cookie('testname'))
# 删除
driver.delete_cookie('testname')
# 删除所有！
driver.delete_all_cookies()
sleep(2)
driver.quit()
