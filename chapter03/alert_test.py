from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get('D:/Automated_testing/alert.html')
driver.set_window_rect(100, 100, 400, 400)
# 获取弹出框的文本信息
driver.find_element(By.ID, 'alert').click()
sleep(2)
alert_message = driver.switch_to.alert
print(alert_message.text)
# 调用accept()方法  -- 确认
alert_message.accept()
# 定位“确认框”按钮
driver.find_element(By.ID, 'confirm').click()
sleep(2)
confirm_message = driver.switch_to.alert
print(confirm_message.text)
alert_message.accept()
# 输入框
driver.find_element(By.ID, 'prompt').click()
sleep(2)
prompt_message = driver.switch_to.alert
print(prompt_message.text)
# prompt_message.send_keys("1234556")
sleep(2)
# 调用dismiss()方法 -- 取消
prompt_message.dismiss()
driver.quit()
