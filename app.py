# Libraries :
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
import pywhatkit
import math
# ماخليت مكتبة ماضفتها احتياط

# The message - editing it to what u need
message = "مبارك عليكم العيد، وكل عام وأنتم في خير وصحة وسلامة 🌹"



# Using whatsapp web
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")
print("Scan the QR code")

# انتظار المستخدم لمسح كود QR
input("press enter after qr code scanning")

contacts = [
    # Editing the contacts to ur contacts in whatsapp
]

for contact in contacts:
    try:
        search_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='3']")
        search_box.clear()
        search_box.send_keys(contact)
        time.sleep(2)

      
        search_box.send_keys(Keys.ENTER)
        time.sleep(1)



      # To send the message
        msg_box = driver.find_element(By.XPATH, "//div[@contenteditable='true'][@data-tab='10']")
      
        msg_box.send_keys(message)
        msg_box.send_keys(Keys.ENTER)
        print(f"I send the message to {contact}")
        time.sleep(1)



  
    except Exception as e:
        print(f"The send was failed")
        continue

print("Done...")
