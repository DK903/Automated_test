from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
url = 'https://bbs.itheima.com/?jingjiaczpz-PC-1'
driver.get(url)
# 定位元素并调用get_attribute方法 -- 获取元素属性名的属性值
post_button = driver.find_element(By.XPATH, "//*[@id='portal_block_417_content']/"
                                            "div/div/a[1]").get_attribute("title")
print(post_button)

