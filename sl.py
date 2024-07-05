from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from email.header import decode_header
from imap_tools import MailBox
import imaplib
import email

def login_slack(email, email_password):
    driver = webdriver.Chrome()
    driver.get("https://slack.com/")
    
    try:
        # Click on the "Sign In" button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
        )
        login_button.click()
        
        # Enter email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_input.send_keys(email)
        
        # Click on the "Next" button after entering email
        next_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        next_button.click()
        
        # Wait for password input field to appear
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys(email_password)
        
        # Click on the "Sign In" button after entering password
        signin_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        signin_button.click()
        
        # Wait for code input field to appear
        code_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/form/div/fieldset"))
        )
        
        # Retrieve the verification code from email
        code = read_emails(email, email_password)
        print("Login ")
        if code:
            code_input.send_keys(code)
            driver.find_element(By.XPATH, "//button[contains(text(), 'Verify')]").click()
            print("Login success")
        else:
            print("Failed to retrieve verification code")
        
    except Exception as e:
        print("Login failed: ", e)
    finally:
        time.sleep(5)
        driver.quit()

# def read_emails(email_user: str, email_password: str, limit: int = 1):
#     try:
#         with MailBox("imap.gmail.com").login(email_user, email_password) as mb:
#             for msg in mb.fetch(limit=limit, reverse=True, mark_seen=False):
#                 print(f"CODE: {msg.uid}\n")
#                 return msg.uid
#     except Exception as e:
#         print(f"Failed to fetch emails: {e}")
#         return None

def read_emails(email_user: str, email_password: str, limit: int = 1):
    try:
        # Connect to Gmail IMAP server
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(email_user, email_password)
        mail.select('inbox')

        # Search for the most recent emails
        result, data = mail.search(None, 'ALL')
        ids = data[0].split()

        messages = []

        # Fetch the emails
        for i in range(len(ids)-1, len(ids)-1-limit, -1):
            result, data = mail.fetch(ids[i], '(RFC822)')
            raw_email = data[0][1]
            msg = email.message_from_bytes(raw_email)
            messages.append(msg)

        mail.close()
        mail.logout()

        return messages

    except Exception as e:
        print(f"Failed to fetch emails: {e}")
        return None


# def read_emails(email_user, email_password, limit=1):
#     with MailBox("imap.gmail.com").login(email_user, email_password) as mb:
#         for msg in mb.fetch(limit=limit, reverse=True, mark_seen=False):
#             # Assuming the verification code is in the subject or body of the email
#             code = extract_verification_code(msg)
#             if code:
#                 return code
#             else:
#                 print("Failed to extract verification code from email.")
#         return None

# def extract_verification_code(email_message):
#     # Implement your logic to extract the verification code from the email message
#     # Example logic:
#     import re
#     pattern = r'(\d{6})'  # Assuming the verification code is 6 digits
#     match = re.search(pattern, email_message.subject)
#     if match:
#         return match.group(1)
#     else:
#         match = re.search(pattern, email_message.body)
#         if match:
#             return match.group(1)
#     return None


# Replace with your email and app password
email_user = "dothithuyuyen0601@gmail.com"
email_password = "ohuwrsygzwhenhfe"

login_slack(email_user, email_password)
read_emails(email_user, email_password)
