#!/usr/bin/env python3
# coding: utf-8

import sys
import os
import requests
import json
from requests import Request, Session

api = 'https://api.shorte.st/v1/data/url'
for x in range(1,91):
    long = '{}'.format(x)
    #print (shorten)
    payload = {'urlToShorten': long}
    # print (payload)
    headers = {'public-api-token': '965c926b3b9b1e9ac442ef7475278c08','content-type': 'application/json'}
    print (json.dumps(payload))
    try:
        r = requests.put(url=api, data=json.dumps(payload), headers=headers)
        #print (r)
    except raise_for_status():
        raise http_error

    #print (r)
    data = r.json()
    print (data)
    shortened = data.get("shortenedUrl")

    code = requests.get (shortened)
    print (code.status_code)

    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.webdriver.common.action_chains import ActionChains

    count = 0
    chrome_options = webdriver.ChromeOptions()
    # Just for fun some extra options for chrome
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--profile-directory=Default')
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-plugins-discovery");
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-infobars")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.delete_all_cookies()
    driver.get(shortened)
    WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.ID, "skip_button"))) # waits till the element with the specific id appears
    print ("Page opened")
    element = driver.find_element_by_id("skip_button")
    element.click()
    # optional quit of the browser
    driver.quit()
    count += 1

# optional count print just to see how many items we have opened
print ("The total number of views should be: %d" % count)
