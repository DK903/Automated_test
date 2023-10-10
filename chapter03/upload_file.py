from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver import ActionChains
import os
driver = webdriver.Chrome()
driver.get('D:/Automated_testing/chapter03/TestProject/upload.html')
button = driver.find_element(By.NAME, 'uploadFile')
ActionChains(driver).click(button).perform()
os.system("D:/AutoIt3/SciTE/test.exe")
sleep(2)
driver.quit()
