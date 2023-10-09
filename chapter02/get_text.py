from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
url = 'https://www.itcast.cn'
driver.get(url)
# 定位元素并使用text属性
element = driver.find_element(By.PARTIAL_LINK_TEXT, "关于传智").text
print(element)
