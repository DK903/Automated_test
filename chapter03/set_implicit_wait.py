# 隐式等待  所有元素等待同一时间
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
# 设置隐式等待为10秒
driver.implicitly_wait(10)
driver.get("https://fe-xianyun-web.itheima.net")
driver.maximize_window()
city = driver.find_element(By.XPATH, "//*[@id='__layout']/div/"
                                     "section/div[2]/div/div[2]/input")
city.send_keys("广州")
driver.find_element(By.CLASS_NAME, 'ell-icon-search').click()
driver.quit()
# 抛出异常： NoSuchElementException: Message: no such element
