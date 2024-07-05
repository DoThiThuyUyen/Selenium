from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get("https://www.google.com.vn/?hl=vi")
title = driver.title
driver.implicitly_wait(0.5)

search_box = driver.find_element(by=By.NAME, value="q")
search_box.send_keys("Hello" )
time.sleep(2)
search_box.send_keys(Keys.ENTER)

time.sleep(10)
driver.quit()