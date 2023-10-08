from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
url = 'https://bbs.itheima.com/?jingjiaczpz-PC-1'
driver.get(url)
# 定位‘签到‘元素
sign_in_button = driver.find_element(By.XPATH, "//*[@id='portal_block_417_content']/div/div/a[2]")
# 判断元素是否可用并输出结果
print(sign_in_button.is_enabled())
