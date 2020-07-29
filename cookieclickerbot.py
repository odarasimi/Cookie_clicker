from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.implicitly_wait(30)
driver.get("https://orteil.dashnet.org/cookieclicker/")

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)

for i in range(1000):
	actions.perform()
	count = int(cookie_count.text.split(" ")[0])
	print (count)
	for item in items:
		value = int(item.text)
		if value <= count:
			upgrade_action = ActionChains(driver)
			upgrade_action.move_to_element(item)
			upgrade_action.click()
			upgrade_action.perform()


