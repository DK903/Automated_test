from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# 加载用户配置，绕开登录功能
options = webdriver.ChromeOptions()
# 页面中禁止弹出窗口 且设置了默认的下载路径
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': 'D:/Automated_testing/downloadFile'}
# 把设置的 prefs 对象添加到 options对象中
options.add_experimental_option('prefs', prefs)
driver = webdriver.Chrome(options=options)
driver.get("https://manager-health-test.itheima.net/")
sleep(5)
driver.find_element(By.CLASS_NAME, "el-button").click()
driver.find_element(By.LINK_TEXT, "预约管理").click()
driver.find_element(By.LINK_TEXT, "预约设置").click()
# 表单切换到 预约设置
driver.switch_to.frame("right")
driver.find_element(By.CSS_SELECTOR, ".el-button").click()
sleep(2)
driver.quit()
