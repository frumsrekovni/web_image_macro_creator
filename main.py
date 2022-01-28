from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

ser = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=ser)
driver.get("https://imgur.com/")
driver.maximize_window()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='qc-cmp2-ui']/div[2]/div/button[3]"))).click()
driver.find_element(By.CLASS_NAME, "Searchbar-textInput").send_keys("monster energy" + Keys.ENTER)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='sort']/div[1]"))).click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='sort']/div[2]/ul/li[2]/a"))).click()




#driver.execute_script('window.open("https://clideo.com/meme-maker","_blank");')
time.sleep(2)