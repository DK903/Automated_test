from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.find_element(By.PARTIAL_LINK_TEXT, '新闻').click()
sleep(3)
print("当前页面的标题是：%s" % driver.title)
print("当前页面的url是：%s" % driver.current_url)
