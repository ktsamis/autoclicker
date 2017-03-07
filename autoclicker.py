# pip requirements:
#requests (2.12.3)
#selenium (3.0.2)
#pip (9.0.1)
#stem
#!/usr/bin/env python
import os
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
CONTROL = u'\ue009'

count = 0
for x in range(0, 5):
	with open('urls','r') as f:
		for line in f:
			print line
			chrome_options = webdriver.ChromeOptions()
			# Just for fun some extra options for chrome
			chrome_options.add_argument('--disable-extensions')
			chrome_options.add_argument('--profile-directory=Default')
			chrome_options.add_argument("--incognito")
			chrome_options.add_argument("--disable-plugins-discovery");
			chrome_options.add_argument("--start-maximized")
			driver = webdriver.Chrome(chrome_options=chrome_options)
			driver.delete_all_cookies()
			driver.get(line)
			WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, "skip_button"))) # waits till the element with the specific id appears
			print "Page opened"
			element = driver.find_element_by_id("skip_button")
			element.click()
			# optional quit of the browser
			# driver.quit()
			count += 1

# optional count print just to see how many items we have opened
# print "The total number of views should be: %d" % count
