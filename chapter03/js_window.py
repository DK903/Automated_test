from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.itcast.cn/")
driver.set_window_size(800, 600)
# 纵向滚动条滚动到底部
DownJs = "window.scrollTo(0,document.body.scrollHeight)"
# 执行脚本
driver.execute_script(DownJs)
sleep(3)
# 纵向滚动条回到最初位置
InitJs = "window.scrollTo(0,0)"
driver.execute_script(InitJs)
sleep(3)
# 横向滚动条滚动到最右侧
DownJs = "window.scrollTo(document.body.scrollWidth,0)"
driver.execute_script(DownJs)
sleep(3)
driver.execute_script(InitJs)
sleep(3)
js = "window.scrollTo(800,800)"
driver.execute_script(js)
sleep(3)
driver.quit()
