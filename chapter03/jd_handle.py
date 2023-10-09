from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# 实现切换窗口
driver = webdriver.Chrome()
driver.get('https://www.jd.com')
driver.maximize_window()
# 当前窗口的句柄  -- 用于切换的标记
handle1 = driver.current_window_handle
print('输出当前窗口的句柄：', handle1)
# 定位并单击 京东超市 链接
driver.find_element(By.PARTIAL_LINK_TEXT, "京东超市").click()
# 所有窗口的句柄
handle2 = driver.window_handles
print('输出所有窗口的句柄：', handle2)
sleep(3)
# 切换到指定窗口
driver.switch_to.window(handle2[0])
sleep(3)
