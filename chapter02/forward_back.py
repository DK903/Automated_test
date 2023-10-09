from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.baidu.com")
driver.get("https://www.jd.com")
driver.back()
print("调用了后退方法")
driver.forward()
print("调用了前进方法")
