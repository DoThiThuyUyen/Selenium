import time
import imaplib
import email
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_slack(email_user, email_password):
    driver = webdriver.Chrome()
    driver.get("https://slack.com/")

    try:
        # Click on the "Sign In" button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
        )
        login_button.click()

        # Enter email and click "Continue"
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        email_input.send_keys(email_user)
        driver.find_element(By.ID, "submit_btn").click()

        # Wait for password input field to appear
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_input.send_keys(email_password)

        # Click on the "Sign in" button after entering password
        driver.find_element(By.ID, "signin_btn").click()

        # Wait for code input field to appear
        code_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "code"))
        )

        # Retrieve the verification code from email
        code = get_verification_code_from_email(email_user, email_password)

        if code:
            code_input.send_keys(code)

            # Click on the "Continue" button after entering the code
            driver.find_element(By.ID, "verify_btn").click()
            print("Login success")
        else:
            print("Failed to retrieve verification code")

    except Exception as e:
        print("Login failed:", e)
    finally:
        time.sleep(5)
        driver.quit()

def get_verification_code_from_email(email_user, email_password):
    # Connect to Gmail IMAP server
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(email_user, email_password)
    mail.select('inbox')

    # Search for the most recent email from Slack
    result, data = mail.search(None, '(FROM "noreply@slack.com" SUBJECT "Your Slack Verification Code")')
    latest_email_id = data[0].split()[-1]

    # Fetch the email body
    result, data = mail.fetch(latest_email_id, '(RFC822)')
    raw_email = data[0][1]
    msg = email.message_from_bytes(raw_email)

    # Extract the verification code (assuming it's in the email body)
    code = extract_code_from_email(msg)
    mail.close()
    mail.logout()

    return code

def extract_code_from_email(msg):
    # Extract the verification code from the email body
    # Example: Extract 6-digit code
    import re
    pattern = r'(\d{6})'  # Assuming the verification code is 6 digits
    match = re.search(pattern, msg.get_payload())
    if match:
        return match.group(1)
    else:
        return None

# Example usage:
email_user = "dothithuyuyen0601@gmail.com"
email_password = "ohuwrsygzwhenhfe"
login_slack(email_user, email_password)
