import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from email.header import decode_header
from imap_tools import MailBox, AND



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
        
        # Click on the "Sign In" button after entering email
        login = driver.find_element(By.XPATH, "//button[@type='submit']")
        login.click()
        
        # Wait for code input field to appear
        code_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "code"))
        )
        
        # Retrieve the verification code from email
        code = read_emails(email_user, email_password)
        
        if code:
            code_input.send_keys(code)
            
            print("Login success")
        else:
            print("Failed to retrieve verification code")
        
    except Exception as e:
        print("Login failed: ", e)
    finally:
        time.sleep(5)
        driver.quit()


# def read_emails(email_user: str, email_password: str,  limit: int = 1):
#     with MailBox("imap.gmail.com").login(email_user, email_password) as mb:
    
#         for msg in mb.fetch(limit=limit, reverse=True, mark_seen=False):
#             print(f"CODE: {msg.uid}\n")
#             return msg.uid

# def read_emails(email_user, email_password):
#   verification_code = ""
#   def extract_verification_code(text):
#     """Trích xuất mã xác minh từ nội dung email."""
#     match = re.search(r'\b\d{6}\b', text)
#     return match.group() if match else None
#   with MailBox("imap.gmail.com").login(email_user, email_password, "INBOX") as mailbox:
#     # Search for emails from Facebook
#     emails = mailbox.fetch(criteria=AND(from_="no-reply-OszyJqf7aCmW9IZUrP898oKc@slack.com"), limit=1, reverse=True, mark_seen=False)
    
#     for msg in emails:
        
#         # Extract the verification code from the email body
#         verification_code = extract_verification_code(msg.subject)
#         if verification_code:
#             print(f"Verification code: {verification_code}")
#             return verification_code
#         else:
#             print("Not found.")
#   return verification_code


def read_emails(email_user, email_password):
    def extract_verification_code(text):
        """Extracts a 6-digit verification code from text."""
        match = re.search(r'\b\d{6}\b', text)
        return match.group() if match else None

    verification_code = ""

    try:
        with MailBox("imap.gmail.com").login(email_user, email_password, "INBOX") as mailbox:
            # Search for emails from Slack
            emails = mailbox.fetch(criteria=AND(from_="no-reply@slack.com"), limit=1, reverse=True, mark_seen=False)
            
            for msg in emails:
                # Extract the verification code from the email subject or body
                verification_code = extract_verification_code(msg.subject)
                if verification_code:
                    print(f"Verification code found: {verification_code}")
                    return verification_code
                else:
                    verification_code = extract_verification_code(msg.body)
                    if verification_code:
                        print(f"Verification code found in body: {verification_code}")
                        return verification_code
                    else:
                        print("No verification code found in email.")
    
    except Exception as e:
        print(f"Failed to fetch or process emails: {e}")
    
    return verification_code


# Replace with your email and app password
email_user = "dothithuyuyen0601@gmail.com"
email_password = "ohuwrsygzwhenhfe"

login_slack(email_user, email_password)
read_emails(email_user, email_password)

