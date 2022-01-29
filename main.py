from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import urllib.request
import time

ser = Service("C:\Program Files (x86)\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
driver = webdriver.Chrome(service=ser,options=options)
driver.get("https://www.google.com/")
driver.maximize_window()

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='L2AGLb']"))).click()
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("monster energy meme" + Keys.ENTER)
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='hdtb-msb']/div[1]/div/div[2]/a"))).click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='yDmH0d']/div[2]/c-wiz/div[1]/div/div[1]/div[2]/div[2]/div/div"))).click()
element = driver.find_element(By.XPATH,"//*[@id='yDmH0d']/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[1]/div/div[4]/div")
webdriver.ActionChains(driver).move_to_element(element).click(element ).perform()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='yDmH0d']/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[3]/div/a[2]"))).click()
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='islrg']/div[1]/div[1]"))).click()
src = driver.find_element(By.XPATH, "//*[@id='Sva75c']/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")
urllib.request.urlretrieve(src, "monster_meme_src_image.png")
print(src)
#driver.implicitly_wait(1)
#driver.execute_script('window.open("https://clideo.com/meme-maker","_blank");')
time.sleep(2)