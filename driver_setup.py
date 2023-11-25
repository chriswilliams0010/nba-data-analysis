#!/usr/bin/env python3

from selenium import webdriver
import time
import logging

driver = webdriver.Safari()

driver.get("https://www.basketball-reference.com")
logging.warning(driver.title)
time.sleep(3)

driver.quit()
