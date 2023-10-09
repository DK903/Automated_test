import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get('https://fe-xianyun-web.itheima.net/')
driver.maximize_window()
# 点击旅游攻略链接
driver.find_element(By.PARTIAL_LINK_TEXT, '旅游攻略').click()
sleep(2)
# 保存为图片
driver.get_screenshot_as_file("D:/Automated_testing/travel.png")
# 单击 写游记 按钮
driver.find_element(By.CLASS_NAME, 'el-button').click()
sleep(2)
# 保存截图的二进制数据
screenshot_first = driver.get_screenshot_as_png()
print('输入二进制数据：%s' % screenshot_first)
# 单击 国内机票 链接
driver.find_element(By.PARTIAL_LINK_TEXT, '国内机票').click()
# base64编码字符串
screenshot_second = driver.get_screenshot_as_base64()
print('输出base64编码字符串：%s' % screenshot_second)
sleep(2)
# 单击登录
driver.find_element(By.PARTIAL_LINK_TEXT, '登录').click()
sleep(2)
# 以时间命名截图
image_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
driver.save_screenshot(image_time + '.png')
driver.quit()
