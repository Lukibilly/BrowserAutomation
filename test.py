import webbrowser
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#os.system("start chrome") OPENS CHROME
driver = webdriver.Chrome()
#driver.get("http://www.python.org")
#chrome_options = Options()
#chrome_options.headless = True
time.sleep(3)
driver.close()