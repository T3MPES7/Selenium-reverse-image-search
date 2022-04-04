
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os,time
import tkinter as tk
from tkinter import filedialog
root= tk.Tk()
TK_SILENCE_DEPRECATION=1
root.withdraw
file_path=filedialog.askopenfilename()
#file_path= the path to the picture 
root.destroy()
file_path=Service(file_path)
import time

# Using Chrome to access web
s=Service('PATH/TO/CHROMEDRIVER')#add your chrome driver paths
op=webdriver.ChromeOptions()
driver = webdriver.Chrome(service=s, options=op)



    # Open the website
driver.get('https://images.google.com/')

agree = driver.find_elements(By.XPATH, "//*[contains(text(), 'I agree')]")[-1]
agree.click()

# Find cam button
cam_button = driver.find_elements_by_xpath("//div[@aria-label=\"Search by image\" and @role=\"button\"]")[0]
cam_button.click()
time.sleep(1)
# Find upload tab
upload_tab = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/div[1]/div/a")
upload_tab.click()
time.sleep(1)
#adds your image
upload_tab = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div/div[2]/form/div[2]/div[2]/input").send_keys(os.getcwd()+file_path)
time.sleep(2)

#opens images
upload_tab = driver.find_element(By.XPATH, "//*[@id='hdtb-msb']/div[1]/div/div[2]/a")
upload_tab.click()
print(driver.page_source)

#driver.quit()
