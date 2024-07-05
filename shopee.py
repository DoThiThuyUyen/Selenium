
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from email.header import decode_header

from imap_tools import MailBox, A


def login_shopee(email):
    driver = webdriver.Chrome()
    driver.get("https://shopee.vn/buyer/signup?gad_source=1&gclid=CjwKCAjwkJm0BhBxEiwAwT1AXE64ywdrWY08zlsc1eHqJMnYDEI1Ztpg-4B49ruLH-og0Qm-K1d1KBoCz5cQAvD_BwE&next=https%3A%2F%2Fshopee.vn%2Fm%2F7-7%3Fgad_source%3D1%26gclid%3DCjwKCAjwkJm0BhBxEiwAwT1AXE64ywdrWY08zlsc1eHqJMnYDEI1Ztpg-4B49ruLH-og0Qm-K1d1KBoCz5cQAvD_BwE")
    
    try:
        # Click on the "Sign In" button
        # login_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/header/div[1]/nav/ul/a[2]"))
        # )
        # login_button.click()
        
        # Enter number phone
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[2]/form/div/div[1]/input"))
        )
        email_input.send_keys(email)
        
        # Click on the "Tiep theo" button after entering email
        login = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[2]/form/button")
        login.click()

        #click chosse
        send_email = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/aside/div[1]/div/div[2]/button[2]"))
        )
        send_email.click()

        sms = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/button[2]"))
        )
        sms.click()


        # sms
        # code_input = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[2]/div/button[2]"))
        # )
    
        # # Retrieve the verification code from email
        # code = read_emails(email_user, email_password)
        
        # if code:
        #     code_input.send_keys(code)
        #     driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[6]/div/div/div/div/button").click()
        #     print("Login success")
        # else:
        #     print("Failed to retrieve verification code")
        
    except Exception as e:
        print("Login failed: ", e)
    finally:
        time.sleep(5)
        driver.quit()


# def read_emails(email_user: str, email_password: str, limit: int = 1):
#     code = None
  
#     with MailBox('imap.gmail.com').login(email_user, email_password) as mailbox:
       
#         for msg in mailbox.fetch(A(all=True), limit=limit, reverse=True, mark_seen=False):
#             print(f"Body: {msg.text}")
          
#             match = re.search(r'\b\d{6}\b', msg.text)
#             if match:
#                 code = match.group(0)
#                 break
#     return code

# Replace with your email and app password
email_user = "012018577757"
# email_password = "ohuwrsygzwhenhfe"

login_shopee(email_user)
# read_emails(email_user, email_password)
time.sleep(10)
