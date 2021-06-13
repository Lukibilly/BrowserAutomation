import webbrowser
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
#chrome_options.headless = True
driver = webdriver.Chrome(options=chrome_options)
#driver.get("http://www.python.org")
time.sleep(3)
driver.close()