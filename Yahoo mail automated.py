# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:54:13 2020
Yahho mail automated 
@author: Puruboi
"""


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import logging
import time
import Inputhandler


# initializing logging file
logging.basicConfig(format='%(asctime)s: %(levelname)s:%(message)s', filename='Gmail.log', level=logging.INFO)

# setting options for chrome driver
options = Options()

#options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument('--disable-infobars')
options.add_argument('--start-fullscreen')
options.add_argument("--disable-popup-blocking")

def info(msg1='',msg2='',msg3=''):
    logging.info(str(msg1)+str(msg2)+str(msg3))
    print(msg1,msg2,msg3)
    
    
info("<Gmail>  trying to connecting to url", ' at ',time.ctime())

path = r"C:\Users\Anonymous\Desktop\Puruboi\chromedriver.exe"
driver = webdriver.Chrome(path)
url='https://mail.yahoo.com/d/folders/1?.intl=in&.lang=en-IN&.partner=none&.src=fp&guce_referrer=aHR0cHM6Ly9sb2dpbi55YWhvby5jb20v&guce_referrer_sig=AQAAAK1SXjQIewQJRHr8dzFp1UUaNUFpSRsVJXnvGpQgTHrhq4VE4PBOOI8Ar-RkN_3v8ui2exQEz6dq8OB6mwrXaH2Jhy_q14uFAjS-2Xxt-8-jwFF4Nwf7JdqKS-TLnAQPjSqACcgY-4PanwZr-7JyK_iUL6IanZg2ypoglmG3jzfm'
driver.get(url)
time.sleep(5)
# driver.close()

email_id_Xpath = '(//*[@id="login-username"])'

Inputhandler.mouseClickSendKeyandEnter(driver,email_id_Xpath,'**********@yahoo.com')
time.sleep(2)

password_Xpath = '(//*[@id="login-passwd"])'
    
Inputhandler.mouseClickSendKeyandEnter(driver,password_Xpath,'************')
time.sleep(2)

compose_button_xpath = '//*[@id="app"]/div[2]/div/div[1]/nav/div/div[1]/a'
Inputhandler.mouseClick(driver,compose_button_xpath)
time.sleep(2)

to_xpath = '//*[@id="message-to-field"]'
Inputhandler.mouseClickSendKeyandEnter(driver,to_xpath,'************@gmail.com')
time.sleep(2)

sub_xpath = '//*[@id="mail-app-component"]/div/div/div[1]/div[3]/div/div/input'
Inputhandler.mouseClickSendKeyandEnter(driver,sub_xpath,'Automated message')
time.sleep(2)

body_xpath = '//*[@id="editor-container"]/div[1]'
Inputhandler.mouseClickSendKeyandEnter(driver,body_xpath,'Hy this is auotmated bot texting u ')
time.sleep(2)

send_xpath = '//*[@id="mail-app-component"]/div/div/div[2]/div[2]/div/button/span'
Inputhandler.mouseClick(driver,send_xpath)
time.sleep(2)

driver.close()