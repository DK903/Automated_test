from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
url = "https://www.itcast.cn/"
driver.get(url)
# 定位图标元素并使用size属性
element = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[2]/div[1]/h1/a/img").size
print(element)
