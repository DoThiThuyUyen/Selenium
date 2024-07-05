
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from email.header import decode_header

from imap_tools import MailBox, A


def login_amazon(name, phone, password, re_password):
    driver = webdriver.Chrome()
    driver.get("https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3F_encoding%3DUTF8%26adgrpid%3D159651196451%26gad_source%3D1%26hvadid%3D675114638367%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D1028809%26hvnetw%3Dg%26hvpone%3D%26hvpos%3D%26hvptwo%3D%26hvqmt%3De%26hvrand%3D16066795084903745481%26hvtargid%3Dkwd-10573980%26hydadcr%3D2246_13468515%26ref%3Dpd_sl_7nnedyywlk_e%26tag%3Dgoogleglobalp-20%26ref_%3Dnav_newcust&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
    
    try:
        # your name
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/div[2]/div/form/div/div/div[1]/input"))
        )
        name_input.send_keys(name)

        #PHONE
        phone_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/div[2]/div/form/div/div/div[2]/div[2]/span/input"))
        )
        phone_input.send_keys(phone)

        #password
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/div[2]/div/form/div/div/div[3]/div[1]/input"))
        )
        password_input.send_keys(password)


        #re pass
        re_password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/div[2]/div/form/div/div/div[3]/div[2]/input"))
        )
        re_password_input.send_keys(re_password)

        # Click on the "Tiep theo" button after entering email
        # login = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div/div[2]/div[2]/form/button")
        # login.click()

        #click continute
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[2]/div/div[2]/div/form/div/div/div[7]/span/span/input"))
        )
        continue_button.click()
        time.sleep(10)
        # sms = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, ""))
        # )
        # sms.click()


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
name = "UyenDo" 
phone ="17873375275" 
password ="123456789" 
re_password = "123456789"

time.sleep(10)
login_amazon(name, phone, password, re_password)
# read_emails(email_user, email_password)
time.sleep(10)
