from selenium import webdriver      
import time  
from selenium.webdriver.common.keys import Keys  

#Time to sleep
sleep_time = 1

#Setting up profiles
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "image/png")
fp.set_preference("browser.dowload.dir", "/home/prat/elab/report")

#Taking input
user = input("Enter Uername: ")
passwd = input("Enter PAssword: ")
# user = "RA1711003010588"
# passwd = "Prat1234" 

#Open Website
browser = webdriver.Firefox(fp)
browser.get('https://care.srmist.edu.in/srmos/login')

#Loging in
username = browser.find_element_by_xpath('//*[@id="mat-input-0"]')
username.send_keys(user)
password = browser.find_element_by_xpath('//*[@id="mat-input-1"]')
password.send_keys(passwd)
login_button = browser.find_element_by_xpath('/html/body/app-root/div/app-login/div/mat-card/div[2]/form/button')
login_button.click()
time.sleep(sleep_time)

#Selecting OS
os = browser.find_element_by_xpath('/html/body/app-root/div/app-student-home/div/mat-card/div/div/app-student-home-card/mat-card')
os.click()
time.sleep(sleep_time)

for i in range(100):
    if i == 0:
        #Select 1st question
        question = browser.find_element_by_css_selector('#svgChart g:nth-child(2) g:nth-child(4) path:nth-child(100)')
        question.click()
        time.sleep(sleep_time)
    else:
        next = browser.find_element_by_css_selector('button.mat-raised-button:nth-child(3)')
        next.click()
        time.sleep(sleep_time)

    #Switch to cpp
    lan = browser.find_element_by_xpath('/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[1]/mat-form-field/div/div[1]/div')
    lan.click()
    cpp = browser.find_element_by_css_selector('#mat-option-1 span:nth-child(1)')
    cpp.click()

    #Evaluate
    evaluate = browser.find_element_by_xpath('/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[3]/button[2]')
    evaluate.click()
    time.sleep(sleep_time)

    try:
        result = browser.find_element_by_link_text("RESULT - 100%")
        download = browser.find_element_by_xpath('/html/body/app-root/div/app-student-solve/div[2]/app-solve-question/div/div[2]/div[2]/mat-card/div[4]/a[2]')
        download.click()
    except:
        print("Skipping Question",i+1)
