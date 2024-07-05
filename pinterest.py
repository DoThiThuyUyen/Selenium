import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions


driver = webdriver.Chrome()
driver.get("https://www.pinterest.com/")

driver.implicitly_wait(0.5)

login_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div[1]/div/div[1]/div/div[2]/div[2]/button/div")
login_button.click()
time.sleep(2)
driver.get("https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Faccounts.google.com%2Fgsi%2Fselect%3Fclient_id%3D694505692171-31closf3bcmlt59aeulg2j81ej68j6hk.apps.googleusercontent.com%26auto_select%3Dtrue%26ux_mode%3Dpopup%26ui_mode%3Dcard%26context%3Duse%26as%3Dm%2FymcvSpOGF6kxok63t53Q%26channel_id%3D3d5aa117bb3229095ca405c89b29b90d54b1c63922103a4fb7e59dffe5b64a1b%26origin%3Dhttps%3A%2F%2Fwww.pinterest.com&faa=1&ifkv=AS5LTAR8edKvO6qs7_syvd9NoroMIyymgW_l8gyGNFelc19pYqO9ymlD_NhLhQYTNayv-5FEts43&ddm=0&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
time.sleep(2)

email_input = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input")
email_input.send_keys("dothithuyen0601@gmail.com")
email_input.send_keys(Keys.RETURN)


time.sleep(10)


