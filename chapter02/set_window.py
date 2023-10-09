from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("https://www.jd.com")
# 最大化窗口
driver.maximize_window()
sleep(1)
# 最小化窗口
driver.minimize_window()
sleep(1)
driver.set_window_size(300, 600)
sleep(1)
driver.set_window_position(300, 200)
driver.set_window_rect(600, 400, 500, 800)
sleep(1)
