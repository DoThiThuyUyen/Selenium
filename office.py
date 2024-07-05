
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from email.header import decode_header

from imap_tools import MailBox, A


def login_office(email, email_password):
    driver = webdriver.Chrome()
    driver.get("https://www.office.com/")
    
    try:
        # Click on the "Sign In" button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div[7]/div[1]/div[3]/div/div[2]/a[1]"))
        )
        login_button.click()
        
        # Enter email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]"))
        )
        email_input.send_keys(email)
        
        # Click on the "Sign In" button after entering email
        login = driver.find_element(By.XPATH, "/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div[2]/input")
        login.click()

        #click send email
        send_email = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[4]/div/div/div/button"))
        )
        send_email.click()

        # Wait for code input field to appear
        code_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[4]/div/div/input"))
        )
    
        # Retrieve the verification code from email
        code = read_emails(email_user, email_password)
        
        if code:
            code_input.send_keys(code)
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div[2]/div[2]/div/form/div[6]/div/div/div/div/button").click()
            print("Login success")
        else:
            print("Failed to retrieve verification code")
        
    except Exception as e:
        print("Login failed: ", e)
    finally:
        time.sleep(5)
        driver.quit()


def read_emails(email_user: str, email_password: str, limit: int = 1):
    code = None
  
    with MailBox('imap.gmail.com').login(email_user, email_password) as mailbox:
       
        for msg in mailbox.fetch(A(all=True), limit=limit, reverse=True, mark_seen=False):
            print(f"Body: {msg.text}")
          
            match = re.search(r'\b\d{6}\b', msg.text)
            if match:
                code = match.group(0)
                break
    return code

# Replace with your email and app password
email_user = "dothithuyuyen0601@gmail.com"
email_password = "ohuwrsygzwhenhfe"

login_office(email_user, email_password)
# read_emails(email_user, email_password)
time.sleep(10)
