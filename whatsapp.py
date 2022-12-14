import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

#
contactName="Me"
message="message"

#
service=Service(ChromeDriverManager().install())
driver= webdriver.Chrome(service = service)
driver.get("https://web.whatsapp.com/")
#
print("scan le QR code")

##
input_path_searchContact='//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]'
input_box_searchContact=driver.find_element(by=By.XPATH, value=input_path_searchContact)
input_box_searchContact.click()
time.sleep(4)

#
input_box_searchContact.send_keys(contactName)
time.sleep(4)
selected_contact=driver.find_element(by=By.XPATH,value="//span[@title='"+contactName+"']")
selected_contact.click()
#
#//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p
input_path_messageBox='//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p'
input_messageBox=driver.find_element(by=By.XPATH, value=input_path_messageBox)
time.sleep(4)
#
input_messageBox.send_keys(message+Keys.ENTER)
time.sleep(4)
driver.quit()
quit()
##

