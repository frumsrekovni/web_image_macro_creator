from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
import urllib.request
import time
import os

def main():
    
    filename = "monster_meme_src_image.png"
    image_path = os.path.join(os.getcwd(), filename)

    ############### FETCH USER ARGUMENTS ###############

    google_search_term = input("Enter the Google search term: ")
    how_recent = input("Recent[1] or Past year[2]: ")
    top_text = input("Top text: ")
    bottom_text = input("Bottom text: ")

    ############### OPEN GOOGLE ###############
    # ser = Service("C:\Program Files (x86)\chromedriver.exe")
    ser = Service(ChromeDriverManager().install()) #Need up to date Chromedriver
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    driver = webdriver.Chrome(service=ser,options=options)
    driver.get("https://www.google.com/")
    driver.maximize_window()

    ############### FETCH THE LATEST RELATED IMAGE ###############

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='L2AGLb']"))).click()
    driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys(google_search_term + Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='hdtb-msb']/div[1]/div/div[2]/a"))).click()
    
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='yDmH0d']/div[2]/c-wiz/div[1]/div/div[1]/div[2]/div[2]/div"))).click()
    element = driver.find_element(By.XPATH,"//*[@id='yDmH0d']/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[1]/div/div[4]/div")
    webdriver.ActionChains(driver).move_to_element(element).click(element ).perform()
    if(how_recent == "1"):
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='yDmH0d']/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[3]/div/a[2]"))).click()
    else:
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='yDmH0d']/div[2]/c-wiz/div[2]/div[2]/c-wiz[1]/div/div/div[3]/div/a[5]/div"))).click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='islrg']/div[1]/div[1]/a[1]"))).click()
    
    time.sleep(5) # for some reason using driver.implicitly_wait() here doesnt work and it just downloads the thumbnail
    src = driver.find_element(By.XPATH, "//*[@id='Sva75c']/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img").get_attribute("src")
    urllib.request.urlretrieve(src, image_path)


    ############### USE THE FETCHED IMAGE TO MAKE A MEME ###############

    driver.get("https://clideo.com/meme-maker")

    upload_box = driver.find_element(By.XPATH , "//*[@id='upload-file']")
    upload_box.send_keys(image_path)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='canvas_top']").click() # Cant access the input buffer directly for some reason. Clicks the top canvas instead and actionchains the string.
    webdriver.ActionChains(driver).send_keys(top_text).perform()
    driver.find_element(By.XPATH, "//*[@id='canvas_bottom']").click()
    webdriver.ActionChains(driver).send_keys(bottom_text).perform()
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='editor']/div[4]/div[2]/button"))).click() # Export
    WebDriverWait(driver, 60).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='download-buttons']/a"))).click() # Download exported image

    time.sleep(3)
    driver.quit()


if __name__ == '__main__':
    main()