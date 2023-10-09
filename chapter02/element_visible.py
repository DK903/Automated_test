from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
url = "https://bbs.itheima.com/?jingjiaczpz-PC-1"
driver.get(url)
# 定位黑马程序员图标元素
logo = driver.find_element(By.XPATH, "//*[@id='Quater_bar']"
                                     "/div[2]/div[1]/h2/a/img")
print(logo.is_displayed())
