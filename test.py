import webbrowser
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

extensionpath = "E:\\PythonProjects\\BrowserAutomation\\uBlock-Origin_v1.35.2.crx"
chrome_options = Options()
#chrome_options.headless = True
chrome_options.add_extension(extensionpath)
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.youtube.com")
wait = WebDriverWait(driver,10)

consent = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button.VfPpkd-LgbsSe.VfPpkd-LgbsSe-OWXEXe-k8QpJ.VfPpkd-LgbsSe-OWXEXe-dgl2Hf.nCP5yc.AjY5Oe.DuMIQc.IIdkle')))
consent.click()

searchbar = wait.until(EC.visibility_of_element_located((By.ID,"search")))
searchbar.send_keys("Rick Roll")
searchbar.send_keys(Keys.ENTER)

firstvideo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'div#contents ytd-item-section-renderer>div#contents a#thumbnail')))
firstvideo.click()

fullscreen = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'button.ytp-fullscreen-button.ytp-button')))
fullscreen.click()

time.sleep(90)
driver.close()