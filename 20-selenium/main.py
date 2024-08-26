# python -m pip install selenium

from selenium import webdriver
import time
firefox_driver_path = 'selenium/geckodriver.exe'

driver = webdriver.Firefox()

driver.get('https://www.toplearn.com')
time.sleep(10)

# driver.quit()


